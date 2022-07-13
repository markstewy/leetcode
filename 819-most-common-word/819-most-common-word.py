import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned.append(" ")
        banned.append("")
        words: List[str] = re.sub("[,.!?;'\"]", " ", paragraph).lower().split(" ")
        count: Dict[int] = {}
        
        for word in words:
            if word not in banned:
                if word not in count:
                    count[word] = 1
                else:
                    count[word] = count[word] + 1
        # print(count)         
        max: tuple[str, int] = ("", 0)
        for i, (k, v) in enumerate(count.items()):
            if v > max[1]:
                max = (k, v)
        return max[0]
        
                