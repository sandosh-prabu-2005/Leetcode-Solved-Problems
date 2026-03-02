class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        
        def backtrack(current_s, open_count, closed_count):
            # Base Case: string is complete
            if len(current_s) == 2 * n:
                result.append(current_s)
                return
            
            # Rule 1: Add opening bracket if we have 'n' pairs to make
            if open_count < n:
                backtrack(current_s + "(", open_count + 1, closed_count)
            
            # Rule 2: Add closing bracket only if it matches an open one
            if closed_count < open_count:
                backtrack(current_s + ")", open_count, closed_count + 1)
        
        # Start the recursion with an empty string and 0 counts
        backtrack("", 0, 0)
        return result