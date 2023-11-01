def print_list(lst: list) -> int:
    result = 0
    for num in lst:
        result = result * 10 + num
    print(result)
