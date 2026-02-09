from typing import TypeVar, Generic

__all__ = ("Node", "Graph")

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value
        self.outbound: list["Node"] = []
        self.inbound: list["Node"] = []

    @property
    def value(self) -> T:
        return self._value

    def point_to(self, other: "Node") -> None:
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self) -> str:
        return f"Node({repr(self._value)})"

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node) -> None:
        self._root = root

    def dfs(self) -> list[Node]:
        visited: list[Node] = []
        stack: list[Node] = [self._root]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                for neighbor in reversed(node.outbound):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return visited

    def bfs(self) -> list[Node]:
        visited: list[Node] = []
        queue: list[Node] = [self._root]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                for neighbor in node.outbound:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return visited
