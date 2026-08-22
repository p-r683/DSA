class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum=0
        digit_pro=1
        num=n
        for i in range(len(str(num))):
            digit=num%10
            num=num//10
            digit_sum+=digit
            digit_pro*=digit
        return n%(digit_sum+digit_pro)==0       