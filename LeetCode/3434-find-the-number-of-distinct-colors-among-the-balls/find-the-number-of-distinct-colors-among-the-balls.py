class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_freq = {}
        ball_color = {}
        result = []

        for ball, color in queries:
            if ball in ball_color:
                prev = ball_color[ball]

                color_freq[prev] -= 1
                if color_freq[prev] == 0:
                    del color_freq[prev]
            
                ball_color[ball] = color

                if color in color_freq:
                    color_freq[color] += 1
                else:
                    color_freq[color] = 1
            else:
                ball_color[ball] = color
                if color in color_freq:
                    color_freq[color] += 1
                else:
                    color_freq[color] = 1

            result.append(len(color_freq))

        return result

            



























        """
        create two hashmap to track
            - ball_color
            - color_freq
        create an array to store the result

        loop through the queries:
            - does the ball exist in ball_color:
                YES
                - update the color freq in color_freq
                        if freq == 0:
                            remove form the dictionary
                            
                - update the ball color ib ball_color
                - update color freq in color_freq
                        - if color exist increment by one
                        - else add new color with freq = 1
                N0:
                - update the ball in ball_color 
                - update color freq in color_freq
                        - if color exist increment by one
                        - else add new color with freq = 1
        
        """


        # ball_to_color = {}
        # color_to_freq = {}
        # result = []

        # for qry in queries:
        #     ball, color = qry

        #     if ball in ball_to_color and ball_to_color[ball] != color:
        #         color_to_freq[ball_to_color[ball]] -= 1

        #         if color_to_freq[ball_to_color[ball]] == 0:
        #             del color_to_freq[ball_to_color[ball]]
                    
        #     elif ball in ball_to_color and ball_to_color[ball] == color:
        #         result.append(len(color_to_freq))
        #         continue

        #     if color in color_to_freq:
        #         color_to_freq[color] += 1
        #     else:
        #         color_to_freq[color] = 1

        #     ball_to_color[ball] = color
        #     result.append(len(color_to_freq))

        # return result