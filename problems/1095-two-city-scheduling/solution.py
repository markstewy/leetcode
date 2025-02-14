class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x : abs(x[0] - x[1]), reverse=True)
        aCount = 0
        bCount = 0
        total = 0

        for a, b in costs:
            if bCount == len(costs) // 2:
                aCount += 1
                total += a
            elif aCount == len(costs) // 2:
                bCount += 1
                total += b
            elif a <= b: 
                aCount += 1
                total += a
            else:
                bCount += 1
                total += b
        
        return total



