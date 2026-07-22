from bisect import bisect_right
from collections import defaultdict
from typing import DefaultDict, List, Tuple


class TimeMap:

    def __init__(self):
        self.store: DefaultDict[str, List[Tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key)
        if not values:
            return ""
        index = bisect_right(values, timestamp, key=lambda item: item[0])
        if index == 0:
            return ""
        return values[index - 1][1]