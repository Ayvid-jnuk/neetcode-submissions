class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        left = 0
        characters = set()

        for right in range(len(s)):
            while s[right] in characters:
                characters.remove(s[left])
                left += 1
            characters.add(s[right])
            length = right - left + 1
            output = max(output, length)
        return output
        