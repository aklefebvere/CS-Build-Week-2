def twoSum(self, nums: List[int], target: int) -> List[int]:
    d = {}
    for i, v in enumerate(nums):
        next_num = target - v

        if next_num in d:
            return [d[next_num], i]
        else:
            d[v] = i
