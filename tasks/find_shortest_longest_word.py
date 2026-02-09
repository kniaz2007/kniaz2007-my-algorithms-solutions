__all__ = ("find_shortest_longest_word",)


def find_shortest_longest_word(text: str):
    splitext=text.split()
    if len(splitext)==0: return (None, None)
    splitext=sorted(splitext, key=len)
    return (splitext[0], splitext[-1])
