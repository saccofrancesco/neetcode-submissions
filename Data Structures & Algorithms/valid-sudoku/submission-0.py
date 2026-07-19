class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        groups: dict[str, dict[int, list[int]]] = {
            "rows": {
                0: [],
                1: [],
                2: [],
                3: [],
                4: [],
                5: [],
                6: [],
                7: [],
                8: [],
            },
            "cols": {
                0: [],
                1: [],
                2: [],
                3: [],
                4: [],
                5: [],
                6: [],
                7: [],
                8: [],
            },
            "blocks": {
                0: [],
                1: [],
                2: [],
                3: [],
                4: [],
                5: [],
                6: [],
                7: [],
                8: [],
            }
        }
        for row in range(len(board)):
            for col in range(len(board[0])):
                number: str = board[row][col]
                if number != ".":
                    number: int = int(number)
                    if number in groups["rows"][row] or number in groups["cols"][col]:
                        return False
                    groups["rows"][row].append(number)
                    groups["cols"][col].append(number)
                    if row <= 2 and col <= 2:
                        if number in groups["blocks"][0]:
                            return False
                        groups["blocks"][0].append(number)
                    elif row <= 5 and col <= 2:
                        if number in groups["blocks"][1]:
                            return False
                        groups["blocks"][1].append(number)
                    elif row <= 8 and col <= 2:
                        if number in groups["blocks"][2]:
                            return False
                        groups["blocks"][2].append(number)
                    elif row <= 2 and col <= 5:
                        if number in groups["blocks"][3]:
                            return False
                        groups["blocks"][3].append(number)
                    elif row <= 5 and col <= 5:
                        if number in groups["blocks"][4]:
                            return False
                        groups["blocks"][4].append(number)
                    elif row <= 8 and col <= 5:
                        if number in groups["blocks"][5]:
                            return False
                        groups["blocks"][5].append(number)
                    elif row <= 2 and col <= 8:
                        if number in groups["blocks"][6]:
                            return False
                        groups["blocks"][6].append(number)
                    elif row <= 5 and col <= 8:
                        if number in groups["blocks"][7]:
                            return False
                        groups["blocks"][7].append(number)
                    elif row <= 8 and col <= 8:
                        if number in groups["blocks"][8]:
                            return False
                        groups["blocks"][8].append(number)
        return True