class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numSet = sorted(set(nums))

        longest = 1
        length = 1

        for i in range(len(numSet)-1):
            if numSet[i]+1 == numSet[i+1]:
                length += 1
                longest = max(longest, length)
            else:
                length = 1
        return longest
        