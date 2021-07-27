def longestCommonPrefix(liste):

    subString=""
    longest=""

    similarSub=[]

    if len(liste)>=1 and len(liste)<=200:



        if len(liste[0])>=0 and len(liste[0])<=200:

            for j in range(len(liste[0])):

                subString = liste[0][0:j+1]

                confirmCount=0



                for k in range(len(liste)):

                    if len(liste[k])>=0 and len(liste[k])<=200:

                        if len(liste[k])>= len(subString):

                            if liste[k].find(subString) ==0 :

                                confirmCount+=1



                                if confirmCount==len(liste):

                                    similarSub.append(subString)

    if len(similarSub)==0:
        return ""
    else:
        for idx in range(len(similarSub)):

            if len(similarSub[idx])> len(longest):

                longest=similarSub[idx]
        return longest

isimler=["eardal"]

print(longestCommonPrefix(isimler))
