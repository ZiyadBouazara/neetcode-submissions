class TimeMap:

    def __init__(self):
        self.timemap = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        array = self.timemap[key]
        l, r = 0, len(array) - 1
        res = ""
        while l <= r:
            mid = (l+r) // 2

            if timestamp >= array[mid][0]:
                res = array[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return res
