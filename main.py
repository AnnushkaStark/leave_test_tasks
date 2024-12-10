from tasks.task_1 import Position, masked_string
from tasks.task_2 import to_camel_case, to_camel_case_lower, to_snake_case
from tasks.task_3 import sum_of_interval_lengths

# task_1

print(
    masked_string(
        strng="1234567890",
        mask_position=Position.LEFT,
        mask_symbol="*",
        visible_symbols=4,
    )
)
print(
    masked_string(
        strng="1234567890",
        mask_position=Position.RIGHT,
        mask_symbol="*",
        visible_symbols=4,
    )
)
print(
    masked_string(
        strng="1234567890",
        mask_position=Position.MIDDLE,
        mask_symbol="*",
        visible_symbols=4,
    )
)


# task_2

print(to_camel_case("my_first_function"))
print(to_camel_case_lower("my_first_function"))
print(to_snake_case("MyFirstFunction"))
print(to_snake_case("myFirstFunction"))


# task_3

print(sum_of_interval_lengths([[1, 4], [7, 10], [3, 5]]))
print(sum_of_interval_lengths([[1, 2], [3, 5], [6, 9]]))
print(sum_of_interval_lengths([]))
print(sum_of_interval_lengths([[1, 5]]))
print(sum_of_interval_lengths([[1, 5], [2, 3], [4, 6]]))
