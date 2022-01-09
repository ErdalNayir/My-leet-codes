class Solution:
    def reverseWords(self, s: str) -> str:
        
        word=""
        newS=""
        i=len(s)-1
        while(i>=0):
            if s[i]==" ":
                newS=word+" "+newS
                word=""
            else:
                word=word+s[i]
            i=i-1

        newS=word+" "+newS
        newS=newS[0:len(newS)-1]
        
        return newS
