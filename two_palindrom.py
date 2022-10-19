"""Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

 One way would be to extract the digits and add them,

 else convert into string and reverse

 """

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        sum = 0

        while x > 0 and num != 0:
            sum = sum * 10 + num % 10
            num //= 10
        print(sum)

        return sum == x

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]
