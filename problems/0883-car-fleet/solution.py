class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()

        times = []
        for c in cars:
            position = c[0]
            speed = c[1]
            time = (target - position) / speed
            times.append(time)

        fleetCount = 0
        fleetTime = -1

        for i in range(len(times) - 1, -1, -1):
            if times[i] > fleetTime:
                fleetCount += 1
                fleetTime = times[i]
        
        return fleetCount
