from collections import defaultdict

# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.secrets_store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.secrets_store[key] += [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if not self.secrets_store.get(key):
            return ""

        for idx in range(len(self.secrets_store[key]) - 1, -1, -1):
            secret, timest = self.secrets_store[key][idx]
            if timest <= timestamp:
                return secret
        else:
            return ""


