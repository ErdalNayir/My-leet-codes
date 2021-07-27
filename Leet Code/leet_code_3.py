def romanToInt(roman):

     symbols ={"I":1, "V":5, "X":10,"L":50,"C":100,"D":500,"M":1000}

     roman =str(roman)

     roman=roman.upper()
     sums=0

     if len(roman)>=1 and len(roman)<=15:
         if len(roman)!=2:
             if len(roman)%2==0:

                 firstLetter=roman[0]
                 lastLetter=roman[-1]

                 interLetters= roman[1:-1]

                 sums=sums + (symbols[firstLetter]+symbols[lastLetter])

                 for index in range(0,len(interLetters),2):

                     sums= sums + (symbols[interLetters[index:index+2][1]]-symbols[interLetters[index:index+2][0]])

                 return sums

             if len(roman)%2!=0:

                firstLetter=roman[0]

                interLetters=roman[1:]

                for index in range(0,len(interLetters),2):

                    sums= sums + (symbols[interLetters[index:index+2][1]]-symbols[interLetters[index:index+2][0]])


                sums=sums + (symbols[firstLetter])

                return sums
         else:
             if roman[1]=="I" and roman[0]=="I":
                return 2
             else:
                 return (symbols[roman[1]]-symbols[roman[0]])


print(romanToInt("ıx"))
