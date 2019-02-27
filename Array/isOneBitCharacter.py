class Solution:
    def isOneBitCharacter(self, bits) -> bool:
        if bits[-1]==1: return False
        i = 0
        while i< len(bits)-1:
            i += bits[i]+1
        return i==len(bits)-1

         