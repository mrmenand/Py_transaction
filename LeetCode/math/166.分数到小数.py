# 166.分数到小数
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = "-" if numerator * denominator < 0 else ""
        numerator, denominator = abs(numerator), abs(denominator)
        # Return the tuple (x//y, x%y)
        m, n = divmod(numerator, denominator)
        int_part = str(m)
        if not n:
            return sign + str(m)

        decimal_part = []
        dic = {}
        i = 0
        while n and n not in dic:
            dic[n] = i
            i += 1
            m, n = divmod(n * 10, denominator)
            decimal_part.append(str(m))

        if not n:
            ret = sign + int_part + "." + "".join(decimal_part)
        else:
            decimal_part.insert(dic[n], "(")
            decimal_part.append(")")
            ret = sign + int_part + "." + "".join(decimal_part)

        return ret
