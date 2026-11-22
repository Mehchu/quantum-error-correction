"""Single-qubit statevectors in computational basis order (|0>, |1>)."""

import numpy as np
from numpy.typing import ArrayLike, NDArray


_NORMALISATION_ATOL = 1e-8


def basis_state(bit: int | np.integer) -> NDArray[np.complex128]:
    """Return the computational basis ket for integer 0 or 1 as a (2,) vector.

    Raise ValueError for other inputs, including booleans.
    """
    if (
        isinstance(bit, (bool, np.bool_))
        or not isinstance(bit, (int, np.integer))
        or bit not in (0, 1)
    ):
        raise ValueError("bit must be the integer 0 or 1")

    state = np.zeros(2, dtype=np.complex128)
    state[bit] = 1
    return state


def _statevector(state: ArrayLike) -> NDArray[np.complex128]:
    amplitudes = np.asarray(state)
    if amplitudes.shape != (2,) or amplitudes.dtype.kind not in "iufc":
        raise ValueError("state must be a numeric vector of shape (2,)")

    with np.errstate(over="ignore"):
        amplitudes = amplitudes.astype(np.complex128, copy=False)
    if not np.all(np.isfinite(amplitudes)):
        raise ValueError("state amplitudes must be finite in complex128")
    return amplitudes


def _has_unit_norm(amplitudes: NDArray[np.complex128]) -> bool:
    with np.errstate(over="ignore"):
        squared_norm = np.vdot(amplitudes, amplitudes).real
    return bool(np.isclose(squared_norm, 1.0, rtol=0.0, atol=_NORMALISATION_ATOL))


def is_normalised(state: ArrayLike) -> bool:
    """Test whether a finite numeric (2,) vector has squared norm within 1e-8 of 1.

    Return False for invalid inputs.
    """
    try:
        amplitudes = _statevector(state)
    except (TypeError, ValueError, OverflowError):
        return False

    return _has_unit_norm(amplitudes)


def measurement_probabilities(state: ArrayLike) -> NDArray[np.float64]:
    """Return Born probabilities [P(0), P(1)] as a (2,) float64 array.

    Raise ValueError unless state is a finite numeric (2,) vector with squared
    norm within 1e-8 of 1.
    """
    amplitudes = _statevector(state)
    if not _has_unit_norm(amplitudes):
        raise ValueError("state must be normalised")
    return np.abs(amplitudes) ** 2
