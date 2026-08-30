class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        have = 0
        need = {}
        best_length = float('inf')
        best_start = 0

        for char in t:
            need[char] = need.get(char, 0) + 1

        need_count = len(need)
        
        left = 0
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1

            while have == need_count:
                window_length = right - left + 1

                if window_length < best_length:
                    best_length = window_length
                    best_start = left

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        if best_length == float('inf'):
            return ""

        return s[best_start:best_start + best_length]

                
                    


        