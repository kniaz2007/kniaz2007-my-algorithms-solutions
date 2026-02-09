__all__ = ("even_odd",)


def even_odd(numbers: list[int]) -> float:
    ch=n=0
    for i in range(len(numbers)):
        if numbers[i]%2==0: ch+=numbers[i]
        else: n+=numbers[i]
    return ch/n
