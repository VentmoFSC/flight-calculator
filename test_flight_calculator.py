import pytest

from flight_calculator import calculate_flight_time


def test_calculate_flight_time_returns_expected_time_for_typical_weight():
    assert calculate_flight_time(500) == 130


def test_calculate_flight_time_returns_expected_time_for_small_weight():
    assert calculate_flight_time(100) == 170


def test_calculate_flight_time_supports_fractional_weight():
    assert calculate_flight_time(125.5) == pytest.approx(167.45)


def test_calculate_flight_time_raises_error_for_zero_weight():
    with pytest.raises(ValueError, match="Weight must be a positive number."):
        calculate_flight_time(0)


def test_calculate_flight_time_raises_error_for_negative_weight():
    with pytest.raises(ValueError, match="Weight must be a positive number."):
        calculate_flight_time(-100)


def test_calculate_flight_time_clamps_negative_result_to_zero():
    assert calculate_flight_time(2000) == 0


def test_calculate_flight_time_returns_zero_at_clamping_boundary():
    assert calculate_flight_time(1800) == 0