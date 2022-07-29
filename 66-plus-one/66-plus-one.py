class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_len = len(digits)
        index = -1
        while True:
            if digits_len >= abs(index) and digits[index]==9:
                digits[index] = 0
                index -= 1
            elif digits_len < abs(index):
                digits.insert(0,1)
                break
            else:
                digits[index] +=1
                break
        return digits