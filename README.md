## Окружение
IDE - Visual Studio Code с расширениями:
Python extension for Visual Studio Code - https://marketplace.visualstudio.com/items?itemName=ms-python.python
Ruff extension for Visual Studio Code - https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff
Интерпретатор Python - версия 3.10/3.11/3.12
Виртуальное окружение Python - создается любым удобным инструментом
Линтер - Ruff с настройками, аналогичными black + isort

# Вариант 2 - задачи
## Задача 1 - маскировка строки

Создать функцию string_masked для маскировки исходной строки - замены всех символов указанным символом, за исключением указанного числа
видимых символов, расположенных слева, справа или по краям результирующей строки.
Функция принимает следующие параметры:
string - исходная строка
visible_symbols - количество видимых символов, по умолчанию 4
mask_position - позиция маскированной части строки, допустимые значения left/right/middle (слева/справа/в центре)
mask_symbol - символ для маскирования, по умолчанию "*"
Примеры:
("1234567890", 4, "left", "*") => "******7890"
("1234567890", 4, "right", "*") => "1234******"
("1234567890", 4, "middle", "*") => "12******90"

## Задача 2 - преобразования наименования метода или класса
Создать функции для преобразования наименования метода или класса из одного формата в другой:
to_camel_case - из формата snake_case в формат CamelCase
to_lower_camel_case - из формата snake_case в формат camelCase
to_snake_case - из формата camelCase/CamelCase в формат snake_case
Примеры:
snake_case - my_first_function
camelCase - myFirstFunction
CamelCase - MyFirstFunction

## Задача 3 - получение суммы длин всех интервалов
Создать функцию sum_of_interval_lengths , которая принимает массив интервалов и возвращает сумму длин всех интервалов. При этом
перекрывающиеся интервалы должны учитываться только один раз.
Интервалы представлены парой целых чисел в виде массива, в котором первое значение интервала всегда будет меньше второго значения.
Пример интервала:
[1, 5] - это интервал от 1 до 5, его длина равна 4
[2, 12] - это интервал от 2 до 12, его длина равна 10
Пример списка, содержащего перекрывающиеся интервалы:
[[1, 4], [7, 10], [3, 5]] - сумма длин этих интервалов равна 7:
длина интервала [7, 10] равна 3
интервалы [1, 4], [3, 5] перекрываются и можно рассматривать как один интервал [1, 5] с длиной 4
Примеры:
sum_of_interval_lengths([[1, 2], [6, 10], [11, 15]]) => 9
sum_of_interval_lengths([[1, 4], [7, 10], [3, 5]]) => 7
sum_of_interval_lengths([[1, 5], [10, 20], [1, 6], [16, 19], [5, 11]]) => 19
sum_of_interval_lengths([[0, 20], [-100000000, 10], [30, 40]]) => 100000030