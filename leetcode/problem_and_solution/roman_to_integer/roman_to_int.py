class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        l_dict={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum=0
        i=0
        while(i<len(s)-1):
            if l_dict[s[i]]>=l_dict[s[i+1]]:
                sum+=l_dict[s[i]]
            if l_dict[s[i]]<l_dict[s[i+1]]:
                sum-=l_dict[s[i]]
            i+=1
        
        return sum+l_dict[s[i]]

            
            

