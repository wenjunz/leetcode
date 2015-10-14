class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        d = {}
        return self.check(s,wordDict,d)
        
    def check(self,s,wordDict,d,start=0):
        if start in d:
            return d[start]
        if s[start:] in wordDict:
            d[start] = True
            return d[start]
        ans = False
        for end in range(start,len(s)):
            if s[start:end] in wordDict:
                ans = ans or self.check(s,wordDict,d,end)
        d[start] = ans
        return d[start]
