# No.1/2019-06-17/24 ms/13.2 MB

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result=0
        sign=(dividend>0) is (divisor>0)
        dividend=abs(dividend)
        div=abs(divisor)
        Q=1
        while dividend>=div:
            dividend-=div
            div+=div
            result+=Q
            Q+=Q
            if dividend < div:
                div=abs(divisor)
                Q=1
        if not sign:
            return max(-result, -2147483648)
        else:
            return min(result, 2147483647)
