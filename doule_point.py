class Solution:
    def reverseWordsA(self, s: str) ->str:
        s=s.strip()
        i=j=len(s)-1
        res=[]
        while i >= 0:
            while s[i]!=' ': i-=1
            res.append(s[i+1:j+1])
            while s[i]== ' ': i-=1
            j=i
        print(res)
        return ' '.join(res)
    def reverseWordsB(self, s: str) ->str:
        return ' '.join(s.strip().split()[::-1])

if __name__ == '__main__':
    s=' Who am I. google it'
    rs=Solution()
    print(rs.reverseWordsB(s))