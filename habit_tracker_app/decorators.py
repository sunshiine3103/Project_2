def validate_string(func):
    """Декоратор для валидации строковых значений."""

    def wrapper(value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Значение должно быть непустой строкой.")
        return func(value)

    return wrapper
