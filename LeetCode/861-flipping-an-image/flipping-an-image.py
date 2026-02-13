class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(image)
        cols = len(image[0])

        res = [[0] * rows for _ in range(cols)]

        for i in range(rows):
            res[i] = image[i][::-1]

        for row in range(rows):
            for col in range(cols):
                if res[row][col] == 0:
                    res[row][col] = 1
                else:
                    res[row][col] = 0

        return res