# Код для файла graph.py
__all__ = ("Node", "Graph")


class Node:
    def __init__(self, value):
        self._value = value
        self.outbound = []
        self.inbound = []

    @property
    def value(self):
        return self._value

    def point_to(self, other):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f"Node({repr(self._value)})"

    __repr__ = __str__


class Graph:
    def __init__(self, root):
        self._root = root

    def dfs(self):
        """Depth-First Search (поиск в глубину)"""
        visited = []
        stack = [self._root]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                # Важно: reversed для соответствия тестам
                for neighbor in reversed(node.outbound):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return visited

    def bfs(self):
        """Breadth-First Search (поиск в ширину)"""
        visited = []
        queue = [self._root]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                for neighbor in node.outbound:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return visited
