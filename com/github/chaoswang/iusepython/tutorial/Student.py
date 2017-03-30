from functools import reduce

def str2int(s):

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(lambda x,y:x * 10 + y, map(char2num, s))

print(str2int("12345"))

def normalize(name):
    return name[0].upper() + name[1::].lower()

print(list(map(normalize, ['adam', 'LISA', 'barT'])))

print(reduce(lambda x,y:x*y, [1,2,3,4]))