
import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time


# 1. DELIVERY CHARGE TESTS

def test_invalid_zero_distance():
    with pytest.raises(ValueError):
        delivery_charge(0, 200, False)


def test_invalid_distance_above_limit():
    with pytest.raises(ValueError):
        delivery_charge(16, 200, False)


def test_free_delivery():
    assert delivery_charge(5, 500, False) == 0


def test_nearby_delivery():
    assert delivery_charge(2, 200, False) == 20


def test_medium_distance_delivery():
    assert delivery_charge(5, 200, False) == 40


def test_long_distance_delivery():
    assert delivery_charge(10, 200, False) == 60


def test_rain_surcharge():
    assert delivery_charge(2, 200, True) == 50


# 2. COUPON TESTS

def test_no_coupon():
    assert apply_coupon(300, None, False) == 300


def test_invalid_coupon():
    with pytest.raises(ValueError):
        apply_coupon(300, "INVALID", True)


def test_welcome_coupon_not_first_order():
    with pytest.raises(ValueError):
        apply_coupon(300, "WELCOME", False)


def test_order_below_minimum():
    assert apply_coupon(150, "SAVE50", True) == 150


def test_save50_coupon():
    assert apply_coupon(300, "SAVE50", True) == 250


def test_welcome_coupon():
    assert apply_coupon(300, "WELCOME", True) == 200


# 3. ESTIMATED DELIVERY TIME TESTS

def test_normal_delivery_time():
    assert estimated_time(5, False, False) == 35


def test_peak_hour():
    assert estimated_time(5, True, False) == 45


def test_restaurant_busy():
    assert estimated_time(5, False, True) == 50


def test_busy_during_peak_hour():
    assert estimated_time(5, True, True) == 65
