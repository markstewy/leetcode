class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {} # n: count

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        sortedArray = [[] for i in range(len(nums) + 1)]

        for n, c in count.items():
            sortedArray[c].append(n)
        
        answer = []
        for i in range(len(sortedArray) - 1, -1, -1):
            for n in sortedArray[i]:
                answer.append(n)
                if len(answer) == k:
                    return answer
    
        return []
