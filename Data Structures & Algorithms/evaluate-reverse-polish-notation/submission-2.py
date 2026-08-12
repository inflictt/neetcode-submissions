class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calc (n1, n2 , opr,stack) :
            result = 0
            if opr =="+":
                result = n1 + n2
            elif opr =="-":
                result = n1  - n2
            elif opr =="*":
                result = n1  * n2
            elif opr =="/":
                result = int(n1  / n2)
            return result # (n1 opr n2 )  
        
        stack = []
        res= []
        for i in range(len(tokens)):
            curr = tokens[i] #got 1 with me
            if curr not in ["+", "-", "/", "*"]:#toh number hai chalne do add tostack 
                stack.append(int(curr))
            else: #koi operand hai toh ab perform kro prev 2 par
                n2 = stack.pop() #2
                n1 = stack.pop() #1
                val = calc(n1, n2 , curr, stack) #got 3 back with me
                stack.append(val)
                res.append(val)
        return stack[-1]