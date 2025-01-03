def validate_string(value: str) -> bool:
    """Проверяет, является ли значение строкой и не пустое."""
    return isinstance(value, str) and bool(value.strip())
