class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        
       
        total = 0
        
      
        for i in range(len(s)):
          
            current_value = roman_map[s[i]]
            
           
            if i + 1 < len(s) and roman_map[s[i + 1]] > current_value:
                total -= current_value
            else:
                total += current_value
        
        return total


