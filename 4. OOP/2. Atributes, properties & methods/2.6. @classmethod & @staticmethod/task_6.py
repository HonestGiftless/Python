# CaseHelper 🌶️🌶️

import re

class CaseHelper:
    @staticmethod
    def is_snake(stringg):
        return bool(re.fullmatch(r'([a-z]+_?)+', stringg))

    @staticmethod
    def is_upper_camel(stringg):
        return bool(re.fullmatch(r'^[A-Z][a-z]+([A-Z][a-z]+)*$', stringg, flags=re.MULTILINE))

    @staticmethod
    def to_snake(stringg):
        def to_small(match_obj):
            s = match_obj.group(0)
            if s.islower():
                return s
            else:
                if match_obj.start() != 0:
                    return "_" + s.lower()
                else:
                    return s.lower()

        result = re.sub(r'[A-Z]', to_small, stringg)

        return result

    @staticmethod
    def to_upper_camel(stringg):
        item = re.split(r'_', stringg)
        result = item[0].capitalize()

        if len(item) > 1:
            for i in range(1, len(item)):
                result += item[i].capitalize()

        return result