class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort() # sort by position

        times = []
        for c in cars:
            speed = c[1]
            pos = c[0]
            arrivalTime = (target - pos) / speed
            times.append(arrivalTime)
        

        fleetCount = 1
        fleetTime = times[-1]
        for i in range(len(times) - 1, -1, -1):
            if times[i] > fleetTime:
                fleetTime = times[i]
                fleetCount += 1
        
        return fleetCount

