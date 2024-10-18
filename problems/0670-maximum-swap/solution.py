class Solution:
    def maximumSwap(self, num: int) -> int:
        digit = []
        for i, c in enumerate(str(num)):
            digit.append({"val": int(c), "idx": i})

        digitSorted = sorted(digit, key = lambda x : (x["val"], x["idx"]), reverse = True)

        for d in digit:
            for ds in digitSorted:
                if d["val"] < ds["val"] and ds["idx"] > d["idx"]:
                    tempVal = d["val"]
                    digit[d["idx"]]["val"] = ds["val"]
                    digit[ds["idx"]]["val"] = tempVal
                    
                    ans = ""
                    for n in digit:
                        ans += str(n["val"])
                    return int(ans)
        return num

