class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution: List[int] = []
        # create a map of all indexes by their value
        dict:Dict[int, List[int]] = {};
        
        for i, val in enumerate(nums):
            if val not in dict:
                dict[val] = [i]
            else:  
                dict[val].append(i);      
        # loop over each num and see if value exists in map
        for i, val in enumerate(nums):
            diff: int = target - val;
            if diff in dict:
                for idx in dict[diff]:
                    # if exists make sure it's not the same as the current index
                    if idx != i:
                        solution.append(i)
                        solution.append(idx)
                        return solution
        return solution              
        