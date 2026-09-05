import pytest

def calculator(op, a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Numbers required")

    if op == "add":
        return a + b
    if op == "subtract":
        return a - b
    if op == "multiply":
        return a * b
    if op == "divide":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    raise ValueError("Invalid operation")


def converter(value, unit):
    if not isinstance(value, (int, float)):
        raise TypeError("Number required")

    if unit == "km_to_miles":
        return value * 0.621371

    if unit == "celsius_to_fahrenheit":
        return value * 9/5 + 32

    raise ValueError("Invalid unit")


products = {
    "laptop": {"price": 75000, "stock": 10},
    "phone": {"price": 45000, "stock": 20},
    "mouse": {"price": 1200, "stock": 50},
    "keyboard": {"price": 2500, "stock": 30},
    "monitor": {"price": 18000, "stock": 15},
    "tablet": {"price": 30000, "stock": 12},
    "printer": {"price": 12000, "stock": 8},
    "webcam": {"price": 5000, "stock": 20},
    "speaker": {"price": 4000, "stock": 25},
    "headphones": {"price": 3500, "stock": 40}
}


def lookup_product(name):
    if not isinstance(name, str):
        raise TypeError("Name must be text")

    if name == "":
        raise ValueError("Empty name")

    if name.lower() not in products:
        raise KeyError("Product not found")

    return products[name.lower()]


# ---------- TESTS ----------

def test_add():
    assert calculator("add", 10, 5) == 15

def test_subtract():
    assert calculator("subtract", 10, 5) == 5

def test_multiply():
    assert calculator("multiply", 10, 5) == 50

def test_divide():
    assert calculator("divide", 10, 5) == 2

def test_negative():
    assert calculator("add", -5, 5) == 0

def test_zero():
    assert calculator("multiply", 10, 0) == 0

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        calculator("divide", 10, 0)

def test_text():
    with pytest.raises(TypeError):
        calculator("add", "10", 5)

def test_invalid_operation():
    with pytest.raises(ValueError):
        calculator("power", 2, 3)

def test_km():
    assert converter(1, "km_to_miles") == pytest.approx(0.621371)

def test_100km():
    assert converter(100, "km_to_miles") == pytest.approx(62.1371)

def test_celsius():
    assert converter(0, "celsius_to_fahrenheit") == 32

def test_100_celsius():
    assert converter(100, "celsius_to_fahrenheit") == 212

def test_converter_text():
    with pytest.raises(TypeError):
        converter("100", "km_to_miles")

def test_invalid_unit():
    with pytest.raises(ValueError):
        converter(10, "invalid")

def test_laptop():
    assert lookup_product("laptop")["price"] == 75000

def test_phone():
    assert lookup_product("phone")["stock"] == 20

def test_mouse():
    assert lookup_product("mouse")["price"] == 1200

def test_keyboard():
    assert lookup_product("keyboard")["stock"] == 30

def test_monitor():
    assert lookup_product("monitor")["price"] == 18000

def test_uppercase():
    assert lookup_product("LAPTOP")["price"] == 75000

def test_missing():
    with pytest.raises(KeyError):
        lookup_product("watch")

def test_empty():
    with pytest.raises(ValueError):
        lookup_product("")

def test_wrong_type():
    with pytest.raises(TypeError):
        lookup_product(123)