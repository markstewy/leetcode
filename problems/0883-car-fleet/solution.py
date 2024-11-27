class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()

        times = []
        for c in cars:
            distance = target - c[0]
            speed = c[1]
            arrivalTime = distance / speed
            times.append(arrivalTime)

        
        fleetTime = times[-1]
        fleetCount = 1

        for i in range(len(times) - 1, -1, -1):
            if times[i] > fleetTime:
                fleetCount += 1
                fleetTime = times[i]

        return fleetCount
