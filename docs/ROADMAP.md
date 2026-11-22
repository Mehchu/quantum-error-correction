# Quantum error correction: development roadmap

Goal: a tested and reproducible QEC simulation and decoder benchmarking project. The first few milestones build understanding; the later milestones provide the distinctive portfolio evidence. Time estimates are planning estimates, not deadlines. Target roughly 8–10 hours a week when academic workload permits.

## Milestone 1 — Quantum information foundations (8–10 hours)

Study IBM's [Basics of Quantum Information](https://learning.quantum.ibm.com/course/basics-of-quantum-information), initially single and multiple systems. Use [Qiskit documentation](https://quantum.cloud.ibm.com/docs) as a programming reference.

Files: `src/qec/states.py`, `gates.py`, `circuits.py`; matching tests.

### 1A — Single qubits

- Implement basis_state(bit), is_normalised(state), measurement_probabilities(state), elementary Pauli I/X/Y/Z and H matrices, is_unitary(gate), apply_gate(gate, state).
- Use 1D complex arrays of shape (2,) and matrices of shape (2,2); specify accepted inputs and rejection of invalid shapes, values and non-normalised states.
- Write tests for basis vectors, X and H action on both basis states, Pauli/H squares, unitarity, probabilities, invalid input and complex relative phases.
- Compare with Qiskit Statevector on deterministic single-qubit circuits.

### 1B — Multiple systems

- Study tensor products, controlled gates and entanglement. Implement small-system tensor products and gate application consistent with Qiskit ordering; test asymmetric computational basis cases so ordering bugs cannot hide.
- Construct Bell and GHZ states in NumPy and Qiskit. Compare full vectors up to global phase, not just probabilities.
- Implement pure-state density matrices and partial trace for small systems. Test Hermiticity, trace, Bell marginal I/2 and product-state marginals.

Acceptance: deterministic tests pass; maintainer can derive the outputs by hand and explain the Born rule, phase, tensor ordering and why Bell states are entangled. No large general-purpose simulator required.

## Milestone 2 — Three-qubit repetition code (6–8 hours)

Study bit-flip correction and IBM's [Foundations of Quantum Error Correction](https://learning.quantum.ibm.com/course/foundations-of-quantum-error-correction).

Files: `codes/repetition.py`, `decoders/lookup.py`, repetition tests, a reproducible experiment and short derivation.

- Encode alpha|0> + beta|1> into alpha|000> + beta|111>.
- Inject each physical X error independently of recovery, and measure parity checks Z0 Z1 and Z1 Z2 using ancillary qubits or a clearly documented coherent reference circuit.
- Define syndrome as an ordered two-bit tuple (s01,s12); no error gives (0,0), X0 gives (1,0), X1 gives (1,1), X2 gives (0,1). Decode using only the syndrome, not the injected error labels.
- Correct and decode; compare the recovered logical state with the original using a partial trace and fidelity.
- Test all four correctable patterns on |0>, |1>, |+>, and a state with complex relative phase. Test multi-error patterns and demonstrate limitations for phase errors.
- Enumerate all eight independent X-error patterns and verify p_L = 3p²(1-p) + p³ = 3p² - 2p³ under perfect correction. Plot the analytical curve and numerical estimates, with clear labels.

Acceptance: all single X errors corrected, all uncorrectable patterns classified by logical action; limitations documented. Produce a first independently reproducible figure.

## Milestone 3 — Noise channels (8–10 hours)

Files: `noise.py`, `test_noise.py`.

- Implement bit-flip, phase-flip, depolarising, amplitude damping and phase damping channels using Kraus operators. Explicitly state parameter conventions; depolarising conventions vary.
- Implement small-system density-matrix evolution E(rho) = sum K rho K†.
- Verify completeness sum K†K = I for supported parameter ranges, trace preservation, Hermiticity, positivity within numerical tolerance, identity limits and analytical cases; compare with Qiskit quantum information channels.

Acceptance: parameter boundaries and invalid input tested; demonstrate how different error channels affect the repetition code and why it is not a full single-qubit-error-correcting quantum code.

## Milestone 4 — Generalised repetition codes (6–8 hours)

- Extend to odd lengths n = 3, 5, 7, 9, 11. Implement adjacent parity syndromes and a decoder selecting the smaller-weight error representative for p < 1/2 (with documented tie and model assumptions).
- Derive the majority-vote failure formula sum from k=(n+1)/2 to n of binom(n,k)p^k(1-p)^(n-k).
- Separate classical error-pattern simulation from quantum-state reference checks; avoid exponential statevector storage for Monte Carlo.
- Implement seeded simulation with trial count, failure count and binomial uncertainty; compare against exact probabilities across suitable p values. Handle zero failures with an upper interval bound.

Acceptance: exhaustive small-code verification, scalable experiments for all specified lengths, reproducible plots and a discussion of finite-sample limitations.

## Milestone 5 — Stabiliser formalism and Steane code (10–15 hours)

- Represent multi-qubit Pauli operators, phases, commutation, binary symplectic vectors and stabiliser generators. Work over GF(2); clearly distinguish Pauli phases and stabiliser signs.
- Compute syndromes using the symplectic inner product. Validate commuting and independent generators and distinguish stabilisers from nontrivial logical operators.
- Implement lookup-table decoding for the seven-qubit Steane code. Test each single-qubit X/Y/Z error and compare known small cases against an independent reference.
- Compare storage and operation costs with dense statevector methods, documenting exactly which operations the representation supports.

Acceptance: all 21 nonidentity single-qubit Pauli errors are corrected up to stabiliser equivalence; logical states/observables preserved in the stated ideal model.

## Milestone 6 — Surface-code simulation (20–30+ hours)

- Start with one small rotated planar memory experiment at distance 3; use Stim as a trusted circuit and detection-event simulator. Understand boundary checks, rounds and logical observables before extending to larger distances.
- Define the decoder interface and detection-event format. Use PyMatching as a matching decoder baseline. Do not attempt a production general-purpose MWPM implementation as a prerequisite; an independently implemented small-case decoder or graph exercise is optional.
- Extend to distances 3, 5, 7 and 9 only after validating small cases and model definitions. Explore ideal, phenomenological and circuit-level noise separately if time permits.
- Estimate logical failure with confidence intervals and interpret trends honestly. Do not infer a universal threshold from a few curves.

Acceptance: reproducible end-to-end memory experiment from circuit through detection events to predicted logical flips, tests against trusted tools, and a documented noise-dependent scaling study.

## Milestone 7 — Performance engineering (15–25 hours)

- Profile a real bottleneck (e.g. syndrome generation, batch decoding interface or Monte Carlo analysis).
- Compare baseline Python, vectorised NumPy and an appropriate sparse/binary representation; use a compiled C++ component only if profiling justifies it and tests can verify equivalent results.
- Benchmark throughput, latency and/or memory versus problem size. Separate setup and execution times. Report repetitions, variability, hardware and versions.

Acceptance: correctness preserved, reproducible benchmarks, measured performance trade-offs; if speedup is absent, report that too.

## Releases and portfolio

| Target | Deliverable |
|---|---|
| Week 1 | Foundations, basic tests and documented conventions |
| Week 2 | Repetition code and first result |
| Weeks 3–4 | Channels and generalised repetition experiments |
| Weeks 5–6 | Stabiliser interface and Steane code |
| Weeks 7–9+ | Validated surface-code study |
| Weeks 10–12+ | Profiling, benchmarks and documentation polish |

These targets are flexible. Prefer a smaller verified project over incomplete ambitious features.

For each release: install from a clean environment, run pytest and CI, provide a runnable example, record dependencies and reproduce key figures. Keep the README honest about actual implemented features. Cite learning materials and technical references. The final showcase should highlight a substantive QEC experiment plus a measured engineering result.
