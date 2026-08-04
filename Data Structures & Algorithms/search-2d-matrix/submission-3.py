class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if target < matrix[0][0]:
            return False
    
        row = -1

        for i in range(len(matrix)):
            cur_row = set(matrix[i])
    
            if target in cur_row:
                row = i
                break
        
        if row == -1:
            return False
        
        l, r = 0, len(matrix[row]) - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False 
        