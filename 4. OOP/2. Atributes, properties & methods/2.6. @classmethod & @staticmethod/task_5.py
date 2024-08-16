# StrExtension

import string

class StrExtension:
    @staticmethod
    def remove_vowels(stringg):
        return "".join([i for i in stringg if i.lower() not in 'eyuioa'])

    @staticmethod
    def leave_alpha(stringg):
        return "".join([i for i in stringg if i.lower() in string.ascii_lowercase])
    
    @staticmethod
    def replace_all(stringg, chars, char):
        result = ''
        for i in stringg:
            for j in chars:
                if i == j:
                    i = char
            result += i
        return result