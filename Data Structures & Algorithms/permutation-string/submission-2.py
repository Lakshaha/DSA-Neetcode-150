class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        s1 = "".join(sorted(s1))
        for i in range(n-m+1):
            s3 = s2[i:i+m]
            if "".join(sorted(s3)) == s1:
                return True
        
        return False