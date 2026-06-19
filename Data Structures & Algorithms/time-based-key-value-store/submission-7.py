class TimeMap:
    # each index of the list is the timestamp
    
    def __init__(self):
        self.timemap = defaultdict(list) # { "alice": [(1, "happy"), (2, "stf"), ...], ... }

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # get timestamp that is bigger than what i have -> return most recent timestamp
        # get timestamp that is smaller than what i have -> return ""
        # get timestamp but array empty for key -> return ""
        res = ""

        for t, v in self.timemap[key]:
            if t <= timestamp:
                res = v
            else:
                break
        return res
