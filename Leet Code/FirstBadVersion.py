# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
 
        firstVersion,lastVersion=0,n
        while(firstVersion<lastVersion):
            middleVersion = (firstVersion+lastVersion)//2

            if not isBadVersion(middleVersion):    
                firstVersion=middleVersion+1
              
            elif isBadVersion(middleVersion):
                lastVersion=middleVersion
           
                        
        return lastVersion
