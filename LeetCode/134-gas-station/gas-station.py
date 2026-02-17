class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        size = len(gas)

        gas_available = sum(gas)
        gas_needed = sum(cost)

        if gas_needed > gas_available:
            return - 1

        amount = 0
        idx = 0
        for i in range(size):
            
            amount += gas[i]
            amount -= cost[i]

            if amount < 0:
                amount = 0
                idx = i + 1

        return idx    