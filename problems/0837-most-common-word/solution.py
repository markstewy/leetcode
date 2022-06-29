class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()

        words: List[str] = re.split('[ .,;!?\']', paragraph)

        banned.append("")
        banned.append(" ")
        
        maxStr: str = ""
        maxCount: int = 0
        count: Dict[str, int] = {}
        for word in words:
            if word not in banned:
                if word not in count:
                    count[word] = 1
                else:
                    count[word] = count[word] + 1
                if count[word] > maxCount:
                        maxCount = count[word]
                        maxStr = word
        print(count)
        return maxStr
