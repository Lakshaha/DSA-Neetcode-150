class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.grid = matrix[:][:]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rows = len(self.grid)
        cols = len(self.grid[0])
        totalSum = 0
        for i in range(row1, row2+1):
            array = self.grid[i][col1:col2+1]
            totalSum += sum(array)
        
        return totalSum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)