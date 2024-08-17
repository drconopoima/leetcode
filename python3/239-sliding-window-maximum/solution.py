from collections.abc import Iterable
from collections import deque

class Solution:
    def slidingWindowNext(self, input: list, window_size: int) -> Iterable[deque]:
        if window_size <= 0:
            raise ValueError("Couldn't divide in windows of size lower of equals to '0'")
        input_len: int = len(input)
        max: int
        min, max = 0, window_size
        idx = deque()
        first: bool = True
        while max <= input_len:
            if first:
                first = False
                for pos in range(min,max):
                    while idx and input[idx[-1]] < input[pos]:
                        idx.pop()
                    idx.append(pos)
            else:
                while idx and input[idx[-1]] < input[max-1]:
                    idx.pop()
                idx.append(max-1)
            try:
                yield idx
            except:
                raise StopIteration
            if idx and idx[0] == min:
                idx.popleft()
            min += 1
            max += 1
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        windows = self.slidingWindowNext(nums, k)
        output: list = []
        for window in windows:
            output.append(nums[window[0]])
        return output
