class DatabaseConnectionError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class DatabaseTransactionError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class NoneValueError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
