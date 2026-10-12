class Solution:
    def digitCounts(self, n: int) -> int:
        count = 0

        if n == 0:
            return 1

        while n > 0:
            count += 1
            n = n // 10

        return count

n = int(input("Enter number : "))
obj = Solution()
print(obj.digitCounts(n))