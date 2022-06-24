from inspect import signature
from types import ModuleType


def check_function(scope: ModuleType, func_name: str, params_qty: int = 0):
    """Checks if scope has a function with specific name and params with qty"""
    assert hasattr(scope, func_name), (
        f'Не найдена функция `{func_name}`. '
        'Не удаляйте и не переименовывайте её.'
    )

    func = getattr(scope, func_name)

    assert callable(func), (
        f'`{func_name}` должна быть функцией'
    )

    sig = signature(func)
    assert len(sig.parameters) == params_qty, (
        f'Функция `{func_name}` должна принимать '
        f'количество аргументов: {params_qty}'
    )


def check_default_var_exists(scope: ModuleType, var_name: str) -> None:
    """
    Checks if precode variable exists in scope with a proper type.
    :param scope: Module to look for a variable
    :param var_name: Variable you want to check
    :return: None. It's an assert
    """
    assert hasattr(scope, var_name), (
        f'Не найдена переменная `{var_name}`. Не удаляйте и не переименовывайте ее.'
    )
    var = getattr(scope, var_name)
    assert not callable(var), (
        f'{var_name} должна быть переменной, а не функцией.'
    )

