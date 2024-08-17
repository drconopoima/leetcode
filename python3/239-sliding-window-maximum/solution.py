from collections.abc import Iterable

class Solution:
    def slidingWindowNext(self, input: list, window_size: int) -> Iterable[list]:
        if window_size <= 0:
            raise ValueError("Couldn't divide in windows of size lower of equals to '0'")
        input_len: int = len(input)
        max: int
        min, max = 0, window_size
        while max <= input_len:
            try:
                yield input[min:max]
            except:
                raise StopIteration
            max += 1
            min += 1
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        windows: list = self.slidingWindowNext(nums, k)
        output: list = []
        for window in windows:
            output.append(max(window))
        return output
