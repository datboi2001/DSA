class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        m = len(a)
        n = len(b)
        if m > n:
            b = "0" * (m-n) + b
        elif n > m:
            a = "0" *(n-m) + a
        result = ""
        for i in range(len(a) - 1, -1, -1):
            a_digit = a[i]
            b_digit = b[i]
            if a_digit == "0" and b_digit == "1" or a_digit == "1" and b_digit == "0":
                if carry == 0:
                    result = "1" + result
                else:
                    result ="0" + result
                    carry = 1
            elif a_digit == b_digit == "0":
                if carry == 0:
                    result = "0" + result
                else:
                    result = "1" + result
                    carry = 0
            elif a_digit == b_digit == "1":
                if carry == 0:
                    result = "0" + result
                else:
                    result = "1" + result
                carry = 1
        if carry == 1:
            result = "1" + result
        return result

print(Solution().addBinary("11", "1"))