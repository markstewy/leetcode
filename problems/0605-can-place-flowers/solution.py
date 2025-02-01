class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0

        for i in range(len(flowerbed)):

            openLeft = i == 0 or flowerbed[i - 1] == 0
            openRight = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
            
            if openLeft and openRight and flowerbed[i] == 0:
                count += 1
                flowerbed[i] = 1

        return count >= n


