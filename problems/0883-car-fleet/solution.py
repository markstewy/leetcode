class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = list(zip(position, speed))
        combined.sort()

        time = []

        for c in combined:
            arrival = (target - c[0]) / c[1]
            time.append(arrival)
        

        fleetArrivalTime = 0
        fleetCount = 0
        for i in range(len(time) - 1, -1, -1):
            if time[i] > fleetArrivalTime:
                fleetCount += 1
                fleetArrivalTime = time[i]
        
        return fleetCount
