class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow_recursion(x: float, n: int) -> float:
            # Main idea: use recursion to calculate the power of x. THe main idea
            # is to use the fact that x^n = x^(n/2) * x^(n/2) if n is even, and
            # x^n = x^(n/2) * x^(n/2) * x if n is odd.
            # Time complexity: O(logn)
            if n == 0:
                return 1
            # n is not 0
            temp = pow_recursion(x, n // 2)
            if n % 2 == 0:
                # n is even
                return temp * temp
            else:
                if n > 0:
                    # n is odd and positive
                    return temp * temp * x
                else:
                    # n is odd and negative
                    return (temp * temp) / x
        return pow_recursion(x, n)
         
        