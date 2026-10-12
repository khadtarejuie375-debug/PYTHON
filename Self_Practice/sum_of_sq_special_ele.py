# An element is special if its 1-based position divides the length of the list.
# For example, [1, 2, 3, 4] has a length of 4. The special positions are 1, 2, and 4.
# Therefore, the answer is 1² + 2² + 4² = 21.

class Solution:
    def sumOfSquares(self, nums):
        total = 0
        n = len(nums)

        for i in range(len(nums)):
            if n % (i + 1) == 0:
                total = total + nums[i] * nums[i]

        return total


nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

obj = Solution()
print("Sum of squares:", obj.sumOfSquares(nums))