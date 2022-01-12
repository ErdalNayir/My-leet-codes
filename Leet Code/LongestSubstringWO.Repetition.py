class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSubString=""
        currMaxSubString=""

        for i in range(len(s)):
            if s[i] not in currMaxSubString:
                currMaxSubString=currMaxSubString+s[i]
            else:
                if len(maxSubString)<len(currMaxSubString):
                    maxSubString=currMaxSubString
                    while len(currMaxSubString)>0:
                        if s[i]!=currMaxSubString[0]:
                            currMaxSubString=currMaxSubString[1::]
                        else:
                            currMaxSubString=currMaxSubString[1::]
                            currMaxSubString=currMaxSubString+s[i]
                            break
                else:
                    while len(currMaxSubString)>0:
                        if s[i]!=currMaxSubString[0]:
                            currMaxSubString=currMaxSubString[1::]
                        else:
                            currMaxSubString=currMaxSubString[1::]
                            currMaxSubString=currMaxSubString+s[i]
                            break


        if len(maxSubString)<len(currMaxSubString):
            maxSubString=currMaxSubString

        return len(maxSubString)
