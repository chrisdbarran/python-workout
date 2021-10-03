from typing import List, Dict

def mysum(*args):
    output = args[0]
    for arg in args[1:]:
        output += arg
    return output


def mysum_bigger_than(threshold, *args):
    filtered = [arg for arg in args if arg > threshold]
    return mysum(*filtered)


def sum_numeric(*args):
    total = 0

    for arg in args:
        try:
            total += int(arg)
        except ValueError:
            pass
    return total


def combine_dicts(dicts:List[Dict]) -> Dict:
    result = {}
    for d in dicts:
        for key, value in d.items():
            if key in result:
                try:
                    result[key].append(value)
                except AttributeError:
                    result[key] = [result[key], value]
            else:
                result[key] = value
    return result
