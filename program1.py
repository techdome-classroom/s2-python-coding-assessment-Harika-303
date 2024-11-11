class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
      
        bracket_map = {')': '(', '}': '{', ']': '['}
        
    
        stack = []
        
        print("Starting validation of string:", s)  
        
        for i, char in enumerate(s):
            print(f"Step {i+1}: Processing character '{char}'")

            if char in bracket_map:
                
                top_element = stack.pop() if stack else '#'
                print(f"Found closing bracket '{char}', top of stack was '{top_element}'")
                
               
                if bracket_map[char] != top_element:
                    print("Mismatch found! Returning False.")
                    return False
                else:
                    print("Match found. Continuing...")
            else:
              
                stack.append(char)
                print(f"Found opening bracket '{char}'. Pushed to stack: {stack}")
        
       
        print("Final stack state:", stack)
        return not stack
