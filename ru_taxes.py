import pandas as pd


def tax_salary_per_worker(salary: int) -> pd.DataFrame:
    """
    Функция возвращает таблицу с налогами. Принимает всегда на вход целую
    зар. плату. Данные взяты с сайта
    https://delo.modulbank.ru/all/zarplatnye-nalogi

    Parameters
    ----------
    salary : int
        DESCRIPTION.

    Returns
    -------
    table : TYPE
        DESCRIPTION.

    """

    ndfl = salary * 0.13
    pfr = salary * 0.22
    ffoms = salary * 0.051
    fss = salary * 0.029
    table = pd.DataFrame({'Налог': ['НДФЛ', 'Взносы на пенсионное страхование',
                                    'Взносы на медицинское страхование',
                                    'Взносы на социальное страхование'],
                          'Сумма налога': [ndfl, pfr, ffoms, fss, ]})

    return table


if __name__ == '__main__':
    taxes = tax_salary_per_worker(100_000)
    print(taxes)
