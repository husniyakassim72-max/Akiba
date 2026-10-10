class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
              return False
        number =str(x)
        reversed_number=number[::-1]
        return number==reversed_number

         