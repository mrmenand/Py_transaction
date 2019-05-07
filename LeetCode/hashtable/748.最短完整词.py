# 748 最短的完整词
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
          newPlate = [ i.lower() for i in licensePlate if i.isalpha()]
          # newPlate = filter(str.isalpha,str(licensePlate.lower()))
          words = sorted(words, key=lambda x: len(x))
          for word in words:
              tmp = [i for i in newPlate]
              for i in word:
                  if i in tmp:
                      tmp.remove(i)

              if len(tmp) == 0 :
                  return word



