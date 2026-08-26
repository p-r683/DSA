class Solution:
    def solve(self,index,Flag,numbers,result):
        if index>=len(numbers):
            result.append("".join(numbers))
            return
        numbers[index]="1"
        self.solve(index+1,False,numbers,result)
        if Flag==False:
            numbers[index]="0"
            self.solve(index+1,True,numbers,result)    
        
    def validStrings(self, n: int) -> List[str]:
        numbers=["0"]*n
        result=[]
        self.solve(0,False,numbers,result)
        return result
