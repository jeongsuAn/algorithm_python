def validate_utf_8_str(data: List[int]) -> bool:
        if len(data) == 1:
            first_data = '{:08b}'.format(data[0])
            if first_data.startswith("0"):
                return True
        elif len(data) == 2:
            first_data = '{:08b}'.format(data[0])
            second_data = '{:08b}'.format(data[1])
            if first_data.startswith("110") and second_data.startswith("10"):
                return True
        elif len(data) == 3:
            first_data = '{:08b}'.format(data[0])
            second_data = '{:08b}'.format(data[1])
            third_data = '{:08b}'.format(data[2])
            if first_data.startswith("1110") and second_data.startswith("10") and third_data.startswith("10"):
                return True
        elif len(data) == 4:
            first_data = '{:08b}'.format(data[0])
            second_data = '{:08b}'.format(data[1])
            third_data = '{:08b}'.format(data[2])
            fourth_data = '{:08b}'.format(data[3])
            if first_data.startswith("11110") and second_data.startswith("10") and third_data.startswith("10") and fourth_data.startswith("10"):
                return True
        return False
    
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        result = True
        while data:
            if '{:08b}'.format(data[0]).startswith("0"):
                result = validate_utf_8_str([data[0]])
                data = data[1:]
            elif '{:08b}'.format(data[0]).startswith("110"):
                if len(data) < 2:
                    return False
                result = validate_utf_8_str([data[0], data[1]])
                if not result:
                    return False
                data = data[2:]
            elif '{:08b}'.format(data[0]).startswith("1110"):
                if len(data) < 3:
                    return False
                result = validate_utf_8_str([data[0], data[1], data[2]])
                if not result:
                    return False
                data = data[3:]
            elif '{:08b}'.format(data[0]).startswith("11110"):
                if len(data) < 4:
                    return False
                result = validate_utf_8_str([data[0], data[1], data[2], data[3]])
                if not result:
                    return False    
                data = data[4:]
            else:
                return False
        return result