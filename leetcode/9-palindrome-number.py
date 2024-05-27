class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        else:
            initial_number = x
            reversed_num = 0
            while x != 0:
                last_digit = x % 10
                reversed_num = reversed_num * 10 + last_digit
                x //= 10

            if initial_number - reversed_num == 0:
                return True
            else:
                return False
