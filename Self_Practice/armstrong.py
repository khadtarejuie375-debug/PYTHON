#An Armstrong number equals the sum of its digits, each raised to the power of the number of digits.
class Solution:
    def isArmstrong(self, n):
        original = n
        count = len(str(n))
        total = 0

        while n > 0:
            digit = n % 10
            total = total + digit ** count
            n = n // 10

        return total == original


n = int(input("Enter a number: "))

obj = Solution()
print(obj.isArmstrong(n))