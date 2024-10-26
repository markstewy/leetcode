class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()

        times = []
        for c in cars:
            # append travel time (arrival time)
            times.append((target - c[0]) / c[1])
        
        fleetArrivalTime = 0
        fleetCount = 0
        for i in range(len(times) - 1, -1, -1):
            if times[i] > fleetArrivalTime:
                fleetCount += 1
                fleetArrivalTime = times[i]
        
        return fleetCount
