__all__ = ("seconds_to_str",)


def seconds_to_str(seconds: int) -> str:
    days = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    # Просто всегда показываем всё с нулями
    result = ""
    if days < 10: result += "0"
    result += str(days) + "d"
    if hours < 10: result += "0"
    result += str(hours) + "h"
    if minutes < 10: result += "0"
    result += str(minutes) + "m"
    if seconds < 10 and (days > 0 or hours > 0 or minutes > 0): result += "0"
    result += str(seconds) + "s"
    return result
print(seconds_to_str(93600))
