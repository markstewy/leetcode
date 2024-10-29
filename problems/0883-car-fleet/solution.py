class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))

        cars.sort()
        time = []

        for c in cars:
            time.append((target - c[0]) / c[1])
        
        fleetTime = 0
        fleetCount = 0

        for i in range(len(time) - 1, -1, -1):
            if time[i] > fleetTime:
                fleetCount += 1
                fleetTime = time[i]
        
        return fleetCount
