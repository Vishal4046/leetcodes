class Solution:
    def moveZeroes(self, nums):
        zero = []
        non_zero = []

        for i in nums:
            if i == 0:
                zero.append(i)
            else:
                non_zero.append(i)

        nums[:] = non_zero + zero


s = Solution()
l = [0, 1, 0, 3, 12]

s.moveZeroes(l)
print(l)