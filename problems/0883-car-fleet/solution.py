class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()

        arrivalTimes = []
        for c in cars:
            position = c[0]
            speed = c[1]
            distance = target - position
            arrivalTime = distance / speed
            arrivalTimes.append(arrivalTime)

        
        fleetTime = arrivalTimes[-1]
        fleetCount = 1
        for i in range(len(arrivalTimes) - 1, -1, -1):
            if arrivalTimes[i] > fleetTime:
                fleetTime = arrivalTimes[i]
                fleetCount += 1
            
        return fleetCount
