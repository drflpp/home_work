def task_1() -> str:
    a: int = 2
    b: float = 3.45
    c: str = "trying"
    d: list = [3, 4, 5, 6]
    e: bool = False
    for el in a, b, c, d, e:
        return type(el)
print(task_1())
