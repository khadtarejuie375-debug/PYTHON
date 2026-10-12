class Solution:
    def factorial(self, n):
        fact = 1

        for i in range(1, n + 1):
            fact = fact * i

        return fact


n = int(input("Enter a number: "))

obj = Solution()
print("Factorial:", obj.factorial(n))