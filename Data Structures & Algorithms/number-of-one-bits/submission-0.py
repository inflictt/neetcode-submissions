class Solution:
    def hammingWeight(self, n: int) -> int:
        # tip1. answer is one if that comes in the power of 2
        # tip 2 if the number is perfectSqaure - 1 would be all ones
        # ithink it would be solve using theat take the xor or n with n - 1 and either take hte & and
        # 1-0
        # 2-10
        # 3-11
        # 4-10
        # 5-101
        # # so let num be 5
        # n= 5
        # n -1 =4
        # 5 is 101
        # 4 is 100
        # ---------> took and would give me
        #  100 se it remove the right most 1 101 the right most 1 is gone qas its 100 now instead of 101
        # now n=4 and n-1 =3
        # ->100
        # ->011 woulde doing and opr give me 0 but cnt +=1 = ans as 2
        answer = 0
        while n != 0:  # as n is the one getting decreased
            answer += 1
            n = n & (n - 1)
        return answer
