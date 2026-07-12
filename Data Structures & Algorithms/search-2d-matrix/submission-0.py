class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols  = len(matrix), len(matrix[0])
        low, high = 0, rows*cols - 1

        while low <= high:
            mid = low + (high-low)//2
            midVal = matrix[mid//cols][mid%cols]

            if midVal == target:
                return True
            elif midVal > target:
                high = mid-1
            else:
                low = mid+1
            
        return False