class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_binary = int("0b"+a, 2)
        b_binary = int("0b"+b, 2)
        result = str("{0:b}".format(a_binary+b_binary))
        return result