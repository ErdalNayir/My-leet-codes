class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:]=[s[i] for i in range(len(s)-1,-1,-1)]
