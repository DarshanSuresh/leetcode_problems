class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        revisions1 = version1.split('.')
        revisions2 = version2.split('.')
        
        n1, n2 = len(revisions1), len(revisions2)
        max_revisions = max(n1, n2)
        
        for i in range(max_revisions):
            v1 = int(revisions1[i]) if i < n1 else 0
            v2 = int(revisions2[i]) if i < n2 else 0
            
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        
        return 0
