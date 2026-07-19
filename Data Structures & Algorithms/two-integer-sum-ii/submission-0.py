class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbersIndexes: dict[int, int] = dict()
        for i, n in enumerate(numbers):
            needed: int = target - numbers[i]
            if needed in numbersIndexes:
                index: int = numbersIndexes[needed]
                if i < index:
                    return [i + 1, index + 1]
                else:
                    return [index + 1, i + 1]
            numbersIndexes[n] = i