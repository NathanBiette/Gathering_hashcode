f = open('../data/example.in')
data = f.readlines()
print(data)
numbers = data[0].split(' ')
print(numbers)
R = int(numbers[0])
C = int(numbers[1])
L = int(numbers[2])
H = int(numbers[3])
print(R, C, L, H)

def parse_pizza(data):
    pizza = []
    for index, line in enumerate(data[1:]):
        row = []
        for char in line:
            if char == 'T':
                row += [0]
            if char == 'M':
                row += [1]
        pizza += [row]
    return pizza


print(parse_pizza(data))