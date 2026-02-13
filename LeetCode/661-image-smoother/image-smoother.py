class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(img)
        cols = len(img[0])

        result = [[0] * cols for _ in range(rows)]
        
        for row in range(rows):
            for col in range(cols):
                
                total = 0
                count = 0

                for i in (row - 1, row, row + 1):
                    for j in (col - 1, col, col + 1):
                        if i >= 0 and i < rows and j >= 0 and j < cols:
                            total += img[i][j]
                            count += 1

                result[row][col] = total // count

        return result