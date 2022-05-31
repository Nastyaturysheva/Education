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


def is_leap_year(y: int) -> None:
    if (y % 4 == 0) and (y % 100 != 0):
        print('високосный год')
        print('делится на четыре и не делится на 100')
    elif y % 400 == 0:
        print('високосный год')
        print('делится на 400')
    else:
        print('не високосный год')
        if y % 4 != 0:
            print('не делится 4')
        elif y % 100 == 0:
            print('делится на 100 и не делится на 400')


is_leap_year(2020)
is_leap_year(2100)
is_leap_year(2800)
is_leap_year(2677)

def annuity_credit(body: float, month_number: int, rate: float) -> float:
    """
    Расчет потребительского кредита с % ставкой, который вернет ежемесячный аннуитетнтный платеж
    Parameters
    ----------
    body
    month_number
    rate

    Returns
    -------

    """

