class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""
        for i in range(len(strs)):
            length = len(strs[i])
            encoded += str(length) + ":" + strs[i]
        return encoded

    def decode(self, s: str) -> List[str]:

        decoded = []
        start = 0 
        while start < len(s):
            position = s.index(":", start)
            length = int(s[start:position])

            word_start = position + 1
            word_end = word_start + length 

            word = s[word_start:word_end]
            decoded.append(word)

            start = word_end
        return decoded