def max_num(a: float, b:float) -> float:
    return max(a, b)

print(max_num(5, 4))


def more_than_135(a:float, b:float) -> str:
    c = a - b
    d = b - a
    if (c == 135 or d == 135):
        result = "yes"
    else:
        result = "no"
    return result

print(more_than_135(1, 135))

def season(month:int) -> str:
    if month in [12, 1, 2]:
        season = 'winter'
    elif month in [3, 4, 5]:
        season = 'spring'
    elif month in [6, 7, 8]:
        season = 'summer'
    elif month in [9, 10, 11]:
        season = 'autumn'
    else:
        season = 'season is not defined'
    return season

print(season(8))

def more_than_10(a:float, b:float, c:float) -> str:
    if (a > 10 and b > 10 and c > 10):
        res = 'yes'
    else:
        res = 'no'
    return res
print(more_than_10(17, 11, 12))

def positive(l:list) -> int:
    res = []
    for el in l:
        if el > 0:
            res.append(el)
    return len(res)

print(positive([-1, 2, 3, 4, 5]))

def num_days(years:int, months:int) -> int:
    return (years*365 + months*29)

print(num_days(1, 1))