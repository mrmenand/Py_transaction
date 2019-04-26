# 917. 仅仅反转字母
class Solution:
    def reverseOnlyLetters(self, S):
            # S: str) -> str:
            i, j = 0, len(S)-1
            list_S = [k for k in S]
            while i < j:
                if not list_S[i].isalpha():
                    i += 1
                if not list_S[j].isalpha():
                    j -= 1
                if list_S[i].isalpha() and S[j].isalpha():
                    list_S[i], list_S[j] = list_S[j], list_S[i]
                    i += 1
                    j -= 1

            return "".join(list_S)

