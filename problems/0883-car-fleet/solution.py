class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()

        arrivalTimes = []
        for pos, speed in cars:
            dist = target - pos
            time = dist / speed
            arrivalTimes.append(time)

        mostRecentArrival = arrivalTimes[-1]
        fleetCount = 1

        for i in range(len(arrivalTimes) - 1, -1, -1):
            if arrivalTimes[i] <= mostRecentArrival:
                continue
            else:
                fleetCount += 1
                mostRecentArrival = arrivalTimes[i]
        
        return fleetCount
            

