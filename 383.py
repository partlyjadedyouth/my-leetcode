class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alphs = [0 for _ in range(26)]
        for alph in magazine:
            alphs[ord(alph) - 97] += 1

        for alph in ransomNote:
            if alphs[ord(alph) - 97] == 0:
                return False
            else:
                alphs[ord(alph) - 97] -= 1

        return True
