from typing import List

class Solution:
    def is_straight(self, nums: List[int])->bool:
        repeat=set()
        mi, ma=14,0
        for num in nums:
            if num==0: continue
            ma = max(ma,num)
            mi = min(mi,num)
            if num in repeat: return False
            repeat.add(num)
        return ma-mi<5

if __name__ == '__main__':
    ss=Solution()
    print(ss.is_straight([5,8,6,4,7]))