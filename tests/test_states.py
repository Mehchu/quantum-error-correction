import numpy as np
import pytest
from qiskit.quantum_info import Statevector

from qec.states import basis_state, is_normalised, measurement_probabilities


@pytest.mark.parametrize(("bit", "expected"), [(0, [1, 0]), (np.int64(1), [0, 1])])
def test_basis_state(bit, expected):
    state = basis_state(bit)
    assert state.dtype == np.complex128
    np.testing.assert_array_equal(state, expected)
    assert is_normalised(state)
    np.testing.assert_array_equal(measurement_probabilities(state), expected)


@pytest.mark.parametrize("bit", [-1, 2, 0.0, True, np.bool_(False), "1"])
def test_basis_state_rejects_invalid_bits(bit):
    with pytest.raises(ValueError, match="integer 0 or 1"):
        basis_state(bit)


def test_probabilities_for_complex_relative_phase():
    state = [0.5, 1j * np.sqrt(3) / 2]
    assert is_normalised(state)
    probabilities = measurement_probabilities(state)
    assert probabilities.dtype == np.float64
    np.testing.assert_allclose(probabilities, [0.25, 0.75], rtol=0, atol=1e-15)
    np.testing.assert_allclose(
        probabilities, Statevector(state).probabilities(), rtol=0, atol=1e-15
    )


@pytest.mark.parametrize(
    "state",
    [
        [1],
        [[1], [0]],
        [1, 0, 0, 0],
        ["1", "0"],
        [np.nan, 0],
        [0, np.inf],
        [0, 0],
        [2, 0],
        [1e308, 0],
    ],
)
def test_invalid_states(state):
    assert not is_normalised(state)
    with pytest.raises(ValueError, match="state"):
        measurement_probabilities(state)


def test_normalisation_tolerance_is_absolute():
    assert is_normalised([np.sqrt(1 + 5e-9), 0])
    assert not is_normalised([np.sqrt(1 + 2e-8), 0])
