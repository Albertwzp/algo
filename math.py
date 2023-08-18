
class Solution:
    def lastRemaining(self, n: int, m: int)-> int:
        x=0
        for i in range(2, n+1):
            x = (x+m)%i
        return x

if __name__ == '__main__':
    so=Solution()
    x=so.lastRemaining(249,37)
    print(x)