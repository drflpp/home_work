def task_1() -> list:
    a: int = 2
    b: float = 3.45
    c: str = "trying"
    d: list = [3, 4, 5, 6]
    e: bool = False
    l = [a, b, c, d, e]
    result = []
    for el in l:
        result.append(type(el))
    return result


print(task_1())


def task_2() -> list:
    a = [1, 2, 3, 5, 8, 13, 21]
    return a[0:3]

print(task_2())
#Числа Фибоначии

def task_3(a: float) -> float:
    return a**2
print(task_3(8.8))
