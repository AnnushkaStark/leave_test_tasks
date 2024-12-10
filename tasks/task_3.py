from typing import List


def sum_of_interval_lengths(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0
    # Сортируем интервалы по начальному значению
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    current_start, current_end = sorted_intervals[0]
    total_length = 0

    for start, end in sorted_intervals[1:]:
        # Если текущий интервал не пересекается
        # с предыдущим, добавляем его длину
        if start > current_end:
            total_length += current_end - current_start
            current_start, current_end = start, end
        # Если текущий интервал частично или полностью перекрывает предыдущий,
        # обновляем конечную точку, если она больше
        elif end > current_end:
            current_end = end
    # Добавляем длину последнего интервала
    total_length += current_end - current_start
    return total_length
