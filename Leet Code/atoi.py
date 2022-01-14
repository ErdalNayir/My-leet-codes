class Solution:
    def myAtoi(self, s: str) -> int:
        
        seenDigit=0
        seenWhitspace=0
        seenSign=0
        
        result=0
        signOfResult=1
        s=s.strip()
        
        if "+-" in s or "-+" in s:
            return result
            
        for i in range(len(s)):
            if s[i]=="-":
                if seenDigit==1 or seenSign==1:
                    break
                else:        
                    signOfResult=-1 
                    seenSign=1
            elif s[i]=="+":
                if seenDigit==1 or seenSign==1:
                    break
                else:                 
                    signOfResult=+1  
                    seenSign=1
                    
            elif s[i] in "1234567890":
                if seenWhitspace==0:
                    temp=int(s[i])             
                    result=result*10+temp   
                    if seenDigit==0:
                        seenDigit=1
                else:
                    break
            elif s[i]==" ":
                if seenWhitspace==0:
                    seenWhitspace=1
                result=result
            else:
                break
                
        result=signOfResult*result
                
        if result<-(2**31):
            return -(2**31)
        if result>(2**31)-1:
            return (2**31)-1
                
        return result
        
