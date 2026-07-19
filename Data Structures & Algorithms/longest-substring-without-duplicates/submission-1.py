class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        streaks: dict[int, List[int]] = dict()
        currentKey: int = 0
        if s:
            for char in s:
                if currentKey not in streaks:
                    streaks[currentKey] = [char]
                elif char not in streaks[currentKey]:
                    streaks[currentKey].append(char)
                else:
                    currentKey += 1
                    streaks[currentKey] = [char]
            return len(max(streaks.values(), key=lambda x: len(x)))
        return 0