class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []

        for i in range(len(position)):
            combined.append({
                "position": position[i], 
                "speed": speed[i], 
                "arrivalTime": (target - position[i]) / speed[i]})

        combined.sort(key=lambda x: x["position"])


        fleetCount = 1
        fleetTime = combined[-1]["arrivalTime"]
        for i in range(len(combined) - 1, -1, -1):
            if combined[i]["arrivalTime"] > fleetTime:
                fleetCount += 1
                fleetTime = combined[i]["arrivalTime"]

        return fleetCount



