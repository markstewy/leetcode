class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()

        time = []
        for c in cars:
            position = c[0]
            speed = c[1]
            time.append((target - position) / speed)

        
        fleetTime = 0
        fleetCount = 0

        for i in range(len(time) - 1, -1, -1):
            t = time[i]
            if t > fleetTime:
                fleetCount += 1
                fleetTime = t
        
        return fleetCount


