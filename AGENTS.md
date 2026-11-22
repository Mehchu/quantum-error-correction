# Repository instructions

## Mission

Build a reproducible quantum error correction (QEC) simulation and decoder benchmarking library, demonstrating the transition from mathematical theory to robust scientific software. Prioritise correctness, understanding and measurable results over breadth. The intended audience includes quantum software and fault-tolerant computing engineers.

## Working with the maintainer

The maintainer is a UK mathematics undergraduate with strong linear algebra and probability foundations, experience in Python, and introductory experience in quantum circuits. They are studying IBM's Basics of Quantum Information course. Explain unfamiliar quantum and software concepts without unnecessarily revisiting elementary mathematics.

- Default to mentoring: provide mathematical definitions, implementation contracts, hints, small examples, and acceptance tests. Let the maintainer attempt meaningful implementation first.
- When asked to review code, identify correctness issues, edge cases, numerical stability, complexity, and improvements. Explain why they matter.
- Provide complete implementations when explicitly requested, but explain the important design choices.
- Never invent experimental results, proficiency, employment experience or completed milestones.
- Protect the maintainer's study time; prefer the smallest useful milestone. Do not add unrelated functionality.

## Session workflow

1. Read `docs/ROADMAP.md` and `docs/PROGRESS.md`.
2. Inspect actual files, Git status and existing tests. Progress notes are not proof that code works.
3. Identify the current milestone and propose a small concrete task with acceptance criteria.
4. Preserve existing work; implement only the authorised scope.
5. Run relevant tests, report actual results, and update PROGRESS after substantive changes, including outstanding work and the next task.
6. Suggest a focused commit message; never push or change remote settings unless requested.

## Architecture

- `src/qec/`: reusable Python package; NumPy mathematical primitives, Qiskit reference circuits and simulation, noise channels and stabiliser operations.
- `src/qec/codes/`: repetition, Steane and surface-code implementations as milestones mature.
- `src/qec/decoders/`: syndrome decoders, eventually matching-based decoding.
- `tests/`: deterministic unit and integration tests.
- `experiments/`: executable reproducible simulations that import the package.
- `benchmarks/`: performance methodology and scripts.
- `results/`: selected plots and small reproducibility data.
- `docs/`: derivations, conventions, limitations, roadmap and progress.

Avoid unnecessary abstractions and empty features. Use the existing src layout and pyproject configuration. Inspect dependency versions before suggesting API calls. Prefer established libraries (Qiskit, NumPy, SciPy; later Stim and PyMatching) to unnecessary reimplementations. Educational reference implementations should remain clearly labelled and small.

## Mathematical conventions and quality

- Explicitly document qubit ordering, tensor product ordering, complex dtype, state/density-matrix shapes, syndrome ordering and bit significance. Initially adopt Qiskit's convention: qubit 0 is the least significant bit; computational basis kets for n qubits are labelled |q[n-1]...q[0]>.
- Pure states are normalised complex vectors, density matrices are Hermitian positive semidefinite with trace one, and gates are unitary. Never silently discard imaginary components.
- State comparisons must account for global phase where appropriate. Measurement probabilities alone cannot prove quantum-state equivalence.
- State assumptions when deriving results; distinguish independent data-qubit noise, phenomenological measurement noise and circuit-level noise. Do not claim fault tolerance or thresholds beyond the model tested.
- Define logical failure using the residual error's logical action (or a suitable basis/observable). Do not confuse state-specific fidelity with a general logical error probability.
- Use type hints, concise docstrings with shape/units/ordering, input validation, clear names and explicit numerical tolerances.
- Use pytest for analytical cases, boundary cases, invalid input, regression tests, and independent comparisons with trusted libraries. Make stochastic tests reproducible and avoid flaky statistical assertions.
- Use local virtual environments, editable installation, Ruff and GitHub Actions. Do not commit credentials, virtual environments, caches or oversized raw experiment data.

## Experiments

Separate experiment configuration, simulation and plotting. Record noise model, decoder, code distance, seed, number of trials, package versions and commit reference. Report uncertainty (e.g. Wilson or exact binomial intervals); zero observed failures is not proof that the true rate is zero. For benchmarks, report hardware, versions, workloads, timing method and repeated measurements. Optimise only after establishing correctness and profiling.

## Public repository presentation

Keep README concise, with a working install/run example, implemented features, a reproducible key result, limitations and references. Clearly distinguish planned and completed capabilities. Do not include private personal information or application records.
