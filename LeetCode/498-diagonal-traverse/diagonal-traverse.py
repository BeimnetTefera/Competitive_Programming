class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        rows = len(mat)
        cols = len(mat[0])

        # count the number of diagonal and create a list accordingly
        diagonal = rows + cols - 1

        # create a list with equal number od diagonal
        lists = [[] for _ in range(diagonal)]

        # traverse all over an original matrix
        for row in range(rows):
            for col in range(cols):
                # sum up the row and column
                add = row + col
                # append the result in that summed place of the list
                lists[add].append(mat[row][col])

        # traveres all over the created list and if it is even backwards append to final result if it is odd as it is
        final_res = []
        for i in range(len(lists)):
            if i % 2 == 0:
                final_res.extend(lists[i][::-1])
            else:
                final_res.extend(lists[i])

        return final_res