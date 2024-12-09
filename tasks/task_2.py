def to_camel_case(snake_case: str) -> str:
    snake_case_list = snake_case.split("_")
    result_list = [word.capitalize() for word in snake_case_list]
    return "".join(result_list)


def to_camel_case_lower(snake_case: str) -> str:
    snake_case_list = snake_case.split("_")
    result_list = [snake_case_list[0]]
    changed_list = [
        word.capitalize()
        for word in snake_case_list
        if snake_case_list.index(word) > 0
    ]
    return "".join(result_list + changed_list)


def to_snake_case(camel_case: str) -> str:
    snake_str = ""
    for char in camel_case:
        if char.isupper():
            snake_str += "_" + char.lower()
        else:
            snake_str += char
    return snake_str.strip("_")
