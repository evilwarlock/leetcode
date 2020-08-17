class Solution:
    def getRow(self, rowIndex):
        
        #Initialise tri grid:
        rowIndex += 1 #Adjust for 1 indexing.
        tri = [[1]*x for x in range(1, rowIndex+1)] #Triangle grid of all 1's.
        
        #Edge cases:
        if rowIndex <= 2: #Just return row as initialised.
            return tri[rowIndex-1] #Beware we must undo our indexing adjustment.
        
        #Fill tri grid:
        for row in range(2, len(tri)): #First 2 rows are already correct. Skip.
            for i in range(1, len(tri[row])-1): #Indices skip edge cells.
                tri[row][i] = tri[row-1][i] + tri[row-1][i-1] #Apply formula.
            
        return tri[row] #Return requested row.