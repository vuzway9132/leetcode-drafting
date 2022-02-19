class NumArray:
    
    def __init__(self, nums: List[int]):
        self.nums = nums
        for i in range(len(self.nums)):
            if i > 0:
                self.nums[i] += self.nums[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j] - self.nums[i-1] if i > 0 else self.nums[j]
