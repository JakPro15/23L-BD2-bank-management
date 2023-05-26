from typing import Optional


def set_optional_str(value: Optional[str]) -> str:
    return value if value is not None else "N/A"
