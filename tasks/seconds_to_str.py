__all__ = ("seconds_to_str",)


def seconds_to_str(seconds: int) -> str:
    days = seconds // 86400
    seconds %= 86400

    hours = seconds // 3600
    seconds %= 3600

    minutes = seconds // 60
    seconds %= 60


    result = ""
    if days > 0:
        if days < 10:
            result += "0" + str(days) + "d"
        else:
            result += str(days) + "d"


    if hours > 0 or days > 0:
        if hours < 10:
            result += "0" + str(hours) + "h"
        else:
            result += str(hours) + "h"


    if minutes > 0 or hours > 0 or days > 0:
        if minutes < 10:
            result += "0" + str(minutes) + "m"
        else:
            result += str(minutes) + "m"


    if seconds < 10:
        result += "0" + str(seconds) + "s"
    else:
        result += str(seconds) + "s"

    return result
