class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=int(a) # Convert string to int
        b=int(b)  # Convert string to int
        valueFirst=0 # decimal value of first bin number
        valueSecond=0 # decimal value of second bin number
		
        n=0
        while(a>0): # transfering to decimal
            digit= a%10
            valueFirst=valueFirst+(digit*(2**n))
            n+=1
            a= a//10
			
        n=0
        while(b>0): # transfering to decimal
            digit= b%10
            valueSecond=valueSecond+(digit*(2**n))
            n+=1
            b= b//10

        decimalResult=valueFirst+valueSecond # sum of two decimal numbers

        if decimalResult==0:
            return "0"

        binaryNum=[]
        while (decimalResult > 0):  # decimal to binary
            binaryNum.append(str(decimalResult % 2))
            decimalResult = decimalResult // 2

        binaryNum.reverse()
        result="".join(binaryNum)

        return result
