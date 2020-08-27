def findDuplicate(self, nums: List[int]) -> int:
      nums.sort()

      for i in range(len(nums)):
          if i == 0:
              pass
          else:
              if nums[i] == nums[i - 1]:
                  return nums[i]
