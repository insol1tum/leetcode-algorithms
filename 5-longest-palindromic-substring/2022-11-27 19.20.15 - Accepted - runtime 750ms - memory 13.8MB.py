class Solution:
    def longestPalindrome(self, s: str) -> str:
        ll = len(s)
        w, wl = '', 0

        for i in range(ll):
            for j in (0, 1):
                l, r = i, i + j
                while l >= 0 and r < ll and s[l] == s[r]:
                    a = r - l + 1
                    if a > wl:
                        wl = a
                        w = s[l: r + 1]
                    
                    l -= 1
                    r += 1
        
        return w