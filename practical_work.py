"""
Практическая работа: unit-тесты на pytest.
Запуск: pytest practical_work.py -v
"""

import pytest


# ============================================================
# ЧАСТЬ 1: ФУНКЦИИ (НЕ МЕНЯТЬ)
# ============================================================

def add(a, b):
    """Сложение двух чисел."""
    return a + b


def is_even(n):
    """True, если число чётное."""
    return n % 2 == 0


def max_of_two(a, b):
    """Наибольшее из двух чисел."""
    return max(a, b)


def divide(a, b):
    """Деление. Если b == 0 — ошибка."""
    if b == 0:
        raise ValueError("Деление на ноль")
    return a / b


# ============================================================
# ЧАСТЬ 2: ТЕСТЫ (ВАША РАБОТА)
# ============================================================

# ---------- ПРИМЕР ----------

def test_add_example():
    assert add(2, 3) == 5


# ---------- ЗАДАНИЕ 1: add (2 теста) ----------

def test_add_positive():
    """2 + 2 = 4."""
    assert add(2, 2) == 4


def test_add_negative():
    """-5 + (-3) = -8."""
    assert add(-5, -3) == -8
    

# ---------- ЗАДАНИЕ 2: is_even (2 теста) ----------

def test_is_even_true():
    """4 — чётное."""
    assert is_even(4) is True
    


def test_is_even_false():
    """7 — нечётное."""
    assert is_even(7) is False


# ---------- ЗАДАНИЕ 3: max_of_two (2 теста) ----------

def test_max_first():
    """max(10, 5) = 10."""
    assert max_of_two(10, 5) == 10


def test_max_second():
    """max(1, 9) = 9."""
    assert max_of_two(1, 9) == 9


# ---------- ЗАДАНИЕ 4: divide (2 теста) ----------

def test_divide_simple():
    """10 / 2 = 5.0."""
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    """Деление на 0 → ValueError."""
    with pytest.raises(ValueError):
        divide(10, 0)



# ============================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
