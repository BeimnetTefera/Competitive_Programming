class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_to_color = {}
        color_to_freq = {}
        result = []

        for qry in queries:
            ball, color = qry

            if ball in ball_to_color and ball_to_color[ball] != color:
                color_to_freq[ball_to_color[ball]] -= 1

                if color_to_freq[ball_to_color[ball]] == 0:
                    del color_to_freq[ball_to_color[ball]]
            elif ball in ball_to_color and ball_to_color[ball] == color:
                result.append(len(color_to_freq))
                continue
                
            if color in color_to_freq:
                color_to_freq[color] += 1
            else:
                color_to_freq[color] = 1

            ball_to_color[ball] = color
            result.append(len(color_to_freq))

        return result