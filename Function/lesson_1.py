from typing import Union


def summa(a, b):
    return a + b


print(summa(15, 30))


def difference(x: Union[float, int], y: Union[float, int]) -> Union[float, int]:
    return x - y


print(difference(60, 5))


def factorial(r: int) -> int:
    """
    возвращает значение факториала. r! = r * (r -1) * ... * 1
    Parameters
    ----------
    r: int
        аргумент функции факториала

    Returns
    -------
    c: int
        целое число, значение факториала
    """
    c = 1
    for i in range(1, r + 1):
        c = c * i
    return c


print('3! =', factorial(3))
print('0! =', factorial(0))
print('9! =', factorial(9))
