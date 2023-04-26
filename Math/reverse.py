class Solution:
    def reverse(self, x: int) -> int:
        copy_x = x
        result = 0
        if x < 0:
            copy_x *= -1
        upper_range = pow(2, 31) -1
        lower_range = - pow(2, 31)
        while copy_x:
            copy_x, rem = divmod(copy_x, 10)
            result = result * 10 + rem
            if result >= upper_range or result <= lower_range:
                return 0
        return result * -1 if x < 0 else result

print(Solution().reverse(123))