class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
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
                - add the ball in ball_color 
                - update color freq in color_freq
                        - if color exist increment by one
                        - else add new color with freq = 1
        
        """
        color_freq = {}
        ball_color = {}
        result = []

        for ball, color in queries:
            # check if ball in ball_color dictionary
            if ball in ball_color:
                # for readability store the ball color in prev variable
                prev = ball_color[ball]

                # decrement the color freq from ball_freq becuase if it that ball has different color previously know we have to decrement the previous count
                color_freq[prev] -= 1
                # if the color freq is 0, no ball is assigned to it so we should remove it 
                if color_freq[prev] == 0:
                    del color_freq[prev]
            
            # then if all the sanity check on the upper block is passed we update the color of the ball and its color
            ball_color[ball] = color

            # update the freq of the new color 
            if color in color_freq:
                color_freq[color] += 1
            else:
                color_freq[color] = 1

            # we store the length of the color_freq in result 
            result.append(len(color_freq))

        return result