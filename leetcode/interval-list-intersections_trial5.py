class Solution:
    def intervalIntersection(self, firstList, secondList):
        if not firstList or not secondList:
            return []

        p1 = 0
        p2 = 0
        output = []

        while p1 < len(firstList) and p2 < len(secondList):

            val1 = max(firstList[p1][0], secondList[p2][0])
            val2 = min(firstList[p1][1], secondList[p2][1])

            if val1 <= val2:
                output.append([val1, val2])

            if firstList[p1][1] < secondList[p2][1]:
                p1 += 1
                
            else:
                p2 += 1

        return output