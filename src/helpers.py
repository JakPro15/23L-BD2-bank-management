from typing import Any, Optional


def set_optional_str(value: Optional[Any]) -> str:
    return str(value) if value is not None else "N/A"
