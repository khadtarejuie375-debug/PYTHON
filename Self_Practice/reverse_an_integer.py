class Solution:
    def reverseInteger(self, n):
        rev = 0

        while n > 0:
            digit = n % 10
            rev = rev * 10 + digit
            n = n // 10

        return rev


n = int(input("Enter a number: "))

obj = Solution()
print("Reversed number:", obj.reverseInteger(n))