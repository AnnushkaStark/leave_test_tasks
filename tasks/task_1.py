import enum


class Position(enum.StrEnum):
    LEFT = "left"
    RIGHT = "right"
    MIDDLE = "middle"


def masked_string(
    strng: str, mask_position: Position, mask_symbol="*", visible_symbols=4
) -> str:
    total_length = len(strng)
    if total_length <= visible_symbols:
        return strng
    masked_length = total_length - visible_symbols
    if mask_position == Position.LEFT:
        return mask_symbol * masked_length + strng[-visible_symbols:]
    if mask_position == Position.RIGHT:
        return strng[:visible_symbols] + mask_symbol * masked_length
    if mask_position == Position.MIDDLE:
        left_part = strng[: visible_symbols // 2]
        right_part = strng[-(visible_symbols - visible_symbols // 2) :]
        return left_part + mask_symbol * masked_length + right_part
