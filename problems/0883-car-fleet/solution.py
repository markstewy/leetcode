class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()
        
        arrivalTimes = [] # dist / speed

        for c in cars:
            distance = target - c[0]
            speed = c[1]
            arrivalTimes.append(distance / speed)


        fleetCount = 0
        fleetTime = 0
        print(arrivalTimes)

        for i in range(len(arrivalTimes) - 1, -1, -1):
            carTime = arrivalTimes[i]
            
            if carTime > fleetTime: # if carTime is greater than fleetTime, it arrives after separately
                fleetCount += 1
                fleetTime = carTime
        
        return fleetCount
