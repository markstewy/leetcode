class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] # arrival time
        # default sort on first element in tuple (also, .sort is in place while sort() returns a new array
        combinedArr = list(zip(position, speed))
        combinedArr.sort(reverse=True)

        for i in range(len(combinedArr)):
            pos = combinedArr[i][0]
            speed = combinedArr[i][1]
            arrivalTime = (target - pos) / speed

            if i == 0:
                stack.append(arrivalTime)
# if doesnt arrive before the car in front of it and become one fleet then add a secont fleet arrivalTime to the stack
            elif arrivalTime > stack[-1]: 
                stack.append(arrivalTime)
        
        return len(stack)
