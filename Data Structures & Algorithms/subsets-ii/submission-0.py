class Solution:
    def subsetsWithDup(self, arr: List[int]) -> List[List[int]]:
        # code here
        # so i dry ran the print all possibnle subset in my cope and obeserved that if the array ahs 
        # so ill try having a set that would be keeping track what we have added if we have added a value and it came again then the  value came again wont be added
        arr = sorted(arr)
        seen = set() #so i need to pass tuple as set wont allow list in it
        def solve(index, arr , temp , final):
            if index>=len(arr):#we found an possible subset as an answer
                if tuple(temp) not in seen:#add in this case only 
                    seen.add(tuple(temp))
                    final.append(temp[:])
                return 
            # so in subsert we have a way call pick / not pick
            # so lets pick
            temp.append(arr[index])
            # picked now explore and build it furhter
            solve(index + 1, arr , temp , final)
            # not pick this and then search further
            temp.pop()
            solve(index + 1, arr , temp , final)
            
        temp , final =[], []
        solve(0, arr , temp , final)            
        return final