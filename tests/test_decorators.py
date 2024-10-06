from typing import Union, Any

from src.decorators import log


def test_log(capsys: Any) -> None:
    @log(filename="test_log.txt")
    def my_function(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        return x + y

    # Проверка корректного выполнения функции
    my_function(5, 4)
    captured = capsys.readouterr()
    assert "my_function called with args: (5, 4), kwargs:{}. Result: 9\n" in captured.out
    # Проверка ошибки
    try:
        my_function(0, 2)
    except TypeError:
        captured = capsys.readouterr()
        assert "my function error: " in captured.out
