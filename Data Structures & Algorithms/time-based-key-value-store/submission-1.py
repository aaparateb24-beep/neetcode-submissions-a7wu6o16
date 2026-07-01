class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Timestamps are guaranteed
        # to come in increasing order.
        #
        # So simply append.
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        # Key never existed.
        if key not in self.store:
            return ""

        values = self.store[key]

        left = 0
        right = len(values) - 1

        # Best value found so far.
        answer = ""
        while left <= right:

            mid = (left + right) // 2

            current_time = values[mid][0]
            current_value = values[mid][1]

            # This timestamp works.
            if current_time <= timestamp:

                # Save it.
                answer = current_value

                # Try finding
                # an even later timestamp.
                left = mid + 1

            else:

                # Timestamp is too large.
                right = mid - 1

        return answer
        
