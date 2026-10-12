class Solution:
    def returnLargestDigit(self, n):
        largest = 0

        while n > 0:
            digit = n % 10

            if digit > largest:
                largest = digit

            n = n // 10

        return largest


n = int(input("Enter a number: "))

obj = Solution()
print("Largest digit:", obj.returnLargestDigit(n))