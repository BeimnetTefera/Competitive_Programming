class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * (n + 1)
              
        """
        first last seaat
        first seat add
        last + 1 seat
        dif[1] = seat
        dif[2+1]
        
        dif [0,10,45,-10,-20,-25]
        [10,0 ,0]
        
        
        dif=[0,10,55,45,25,0]
        
        
        [[1,2,10],[2,3,20],[2,5,25]], n = 5
        
        
        
        """
        
        
        for first , last, seat in bookings:
            ans[first - 1] += seat
            ans[last] -= seat

        res = [ans[0]]
        cur = ans[0]
        for i in range(1, len(ans)):
            cur += ans[i]
            res.append(cur)
        
        res.pop()
        return res  