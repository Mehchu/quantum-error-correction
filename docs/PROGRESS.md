# Progress log

## Current status — 22 November 2026

The maintainer reports that the local repository `quantum-error-correction` is set up, its GitHub remote is connected, and dependencies/directory structure have been prepared. Actual repository contents and test execution have not been independently inspected. Check these before marking tasks as verified.

An earlier illustrative reference project was generated separately; do not assume any of its implementation or test results are present in this repository or claim them as the maintainer's work.

### Milestones

| Milestone | Status |
|---|---|
| Repository and environment | Reported set up; verify locally |
| 1. Quantum information foundations | Next: begin single-qubit learning and implementation |
| 2. Three-qubit repetition code | Planned |
| 3. Noise channels | Planned |
| 4. Generalised repetition codes | Planned |
| 5. Stabilisers and Steane code | Planned |
| 6. Surface codes | Planned |
| 7. Performance engineering | Planned |

### Next task

1. Study the single-system portion of IBM's Basics of Quantum Information.
2. Inspect the existing package and verify environment: activate .venv, install in editable mode if needed, inspect imports and run pytest (an empty suite legitimately reports no tests).
3. Implement basis_state, is_normalised and measurement_probabilities in `src/qec/states.py`, with corresponding tests.
4. Implement elementary gates, then compare single-qubit circuit outputs against Qiskit.
5. Commit each verified milestone, and update this file with actual evidence.

### Initial decisions

- Python src layout, package name qec.
- NumPy reference mathematics, Qiskit circuit construction/independent checks; defer Stim/PyMatching until relevant.
- Qiskit-compatible little-endian convention; document all syndrome ordering separately.
- Tests are mandatory before claiming a milestone complete.
- No claims about results until generated and verified in this repository.
- Educational reference code should remain limited; prioritise QEC and benchmarking.

## Update template

Append an entry after meaningful work; keep previous decisions unless superseded explicitly.

- Date and milestone:
- Commit (if available):
- Implemented:
- Tests run and actual results:
- Experimental output and reproduction command (if applicable):
- Decisions and limitations:
- Open issues:
- Next small task:

## 22 November 2026 — Milestone 1A, single-qubit states

- Implemented `basis_state`, `is_normalised`, and `measurement_probabilities`.
- States use shape `(2,)`, complex128 amplitudes, and computational basis order `|0>, |1>`. Normalisation uses an absolute squared-norm tolerance of `1e-8`. Measurement rejects invalid states and returns the squared amplitude magnitudes.
- Verified the local editable package and ran `.venv/bin/python -m pytest -q -W error`. All 19 tests passed, including a complex-state probability comparison with Qiskit 2.6.2.
- Next small task: implement and test elementary gates, then compare full single-qubit circuit statevectors with Qiskit.
