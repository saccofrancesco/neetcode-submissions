class TimeMap:

    def __init__(self):
        self.store: dict[int, dict[str, str]] = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp in self.store:
            self.store[timestamp][key] = value
        else:
            self.store[timestamp] = {key: value}

    def get(self, key: str, timestamp: int) -> str:
        if timestamp in self.store:
            return self.store[timestamp][key]
        elif self.store:
            return self.store[max(self.store.keys())][key]
        return ""
