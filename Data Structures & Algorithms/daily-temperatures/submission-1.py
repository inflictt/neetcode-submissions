class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        ans = [0] * n
        stack = []
        for i in range(n):
            curr = temp[i]
            if not stack:  # add to stack
                stack.append([curr, i])  # added 30 to stack with index
            # if top stack less thn upcoming val pop it and store the ans for it
            else:
                while stack and stack[-1][0] < curr:  # 30 <40 true store and rest
                    prev_temp, prev_index = stack.pop()  # = 30,  1
                    ans[prev_index] = i - prev_index
                # anyways ye append to dono he hongey he so direclty appending
                stack.append([curr, i])
        return ans
