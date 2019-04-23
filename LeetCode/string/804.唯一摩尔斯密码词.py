# 804. 唯一摩尔斯密码词
class Solution:
    def uniqueMorseRepresentations(self,words):
            # words: List[str]) -> int:
            morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
            morse_code = dict(zip([chr(i) for i in range(97,132)],morse))
            for i in range(len(words)):
                words[i] = "".join(morse_code[k] for k in words[i])
            return len(set(words))