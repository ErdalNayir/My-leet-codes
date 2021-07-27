def isPalindrome(x):

    if x>= -(2**31) and x<=(2**31)-1:

        if x<0:
            return False

        elif x>=0:

            sayi = 0
            reversed=0
            target = x

            while(x>0):

                sayi= x%10

                reversed = (reversed*10) + sayi

                x= int(x/10)


            if target == reversed:
                return True
            else:
                return False

print(isPalindrome(0))
