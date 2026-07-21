class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left: int = 0
        frequencies: dict[str, int] = dict()
        max_frequency: int = 0
        longest: int = 0
        for right in range(len(s)):
            char: str = s[right]
            frequencies[char] = frequencies.get(char, 0) + 1
            max_frequency: int = max(max_frequency, frequencies[char])
            window_length: int = right - left + 1
            while window_length - max_frequency > k:
                left_char: str = s[left]
                frequencies[left_char] -= 1
                left += 1
                window_length: int = right - left + 1
            longest: int = max(longest, window_length)
        return longest