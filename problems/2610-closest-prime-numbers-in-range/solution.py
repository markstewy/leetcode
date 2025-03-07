class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
                
        def isPrime(n):
            if n <= 1:
                return False
            if n == 2 or n == 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            
            # Check from 5 to the square root of n, with a step of 6
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        primes = []
        while left <= right:
            if isPrime(left):
                primes.append(left)
            left += 1
        
        if len(primes) < 2:
            return [-1, -1]

        prev = primes[0]
        minDiff = float("infinity")
        minl, minr = None, None

        for n in primes[1:]:
            if n - prev < minDiff:
                minDiff = n - prev
                minl = prev
                minr = n
            prev = n
        
        return [minl, minr]
