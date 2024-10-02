class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key=lambda x : x[0])

        arrivalTimes = []

        for c in cars:
            distance = target - c[0]
            speed = c[1]
            arrivalTime = distance / speed
            arrivalTimes.append(arrivalTime)

        fleetCount = 1
        time = arrivalTimes[-1] # arrival time of first fleet (or the fleet in front of the current car)
        for i in range(len(arrivalTimes) - 1, -1, -1):
            if arrivalTimes[i] > time: # if you will arrive after the fleet in front of you then you will be a new fleet
                fleetCount += 1
                time = arrivalTimes[i]
        
        return fleetCount
    
    # 2, 4, 6, 8 # one fleet
    # 8, 6, 4, 2 # 4 fleets
        

