class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key = lambda x : x[0]) # sort by position

        arrivalTimes = []

        for c in cars:
            dist = target - c[0]
            speed = c[1]
            arrivalTimes.append(dist / speed)
        

        k = 1
        time = arrivalTimes[-1]
        for i in range(len(arrivalTimes) - 1, -1, -1):
            if arrivalTimes[i] > time:
                k += 1
                time = arrivalTimes[i]
        
        return k




