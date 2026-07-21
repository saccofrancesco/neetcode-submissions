from itertools import permutations

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for perm in self.getPermutationsList(s1):
            if perm in s2:
                return True
        return False

    def getPermutationsList(self, s: str) -> List[str]:
        return ["".join(c) for c in permutations(s)]