class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days: List[int] = list()
        for i, temp in enumerate(temperatures):
            count: int = 0
            for j, nextTemp in enumerate(temperatures):
                print(temp, i, nextTemp, j)
                if not j <= i and nextTemp > temp:
                    count = j - i
                    break
            days.append(count)
            print(days)
        return days