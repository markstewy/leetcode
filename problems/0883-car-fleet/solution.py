class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key=lambda x : x[0])

        arrivalTimes = []

        for c in cars:
            time = (target - c[0]) / c[1]
            arrivalTimes.append(time)
        
        fleetCount = 1
        fleetTime = arrivalTimes[-1]
        print(arrivalTimes)
        for i in range(len(arrivalTimes) - 1, -1, -1):
            if arrivalTimes[i] > fleetTime:
                fleetCount += 1
                fleetTime = arrivalTimes[i]
        
        return fleetCount
