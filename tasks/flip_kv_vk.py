from typing import TypeVar

__all__ = (
    "flip_kv_vk",
    "flip_kv_vk_safe",
)


KT = TypeVar("KT")
KV = TypeVar("KV")


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:
    rez = {}
    for key in d:
        rez[d[key]]=key
    return rez

def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:
    rez={}
    for key in d:
        val=d[key]
        if val not in rez:
            rez[val]=[]
        rez[val].append(key)
    return rez

