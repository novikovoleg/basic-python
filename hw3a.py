print('3-easy1') # n не видит
def my_round(number, ndigits):
    m = 10 ** ndigits
    return int((number * m) + 0.5) / m
d = 0
n = float(n.strip())
if d < 0:
    raise ValueError()

print('3-easy2')  # ticket не видит
def luck(ticket):
    s = str(ticket)
    return sum(map(int, s[0:3])) == sum(map(int, s[3:]))

try:
    if 6 != len(ticket) or not ticket.isdigit():
        raise ValueError
except ValueError:
    print('')
    exit(1)
    print('{} is {}'.format)

print('3-easy3') #  не работает
def fibonacci(n, m):
    if not (0 <= n <= m):
        raise ValueError()
    result = [0, 1]
    for i in range(2, m + 1):
        result.append(result[i-2] + result[i-1])
        return result[n:"m + 1"]
print(fibonacci(0, 20))
print(fibonacci(1, 20))
print(fibonacci(1, 1))

print('3-norm1') # в конце тоже проблемы
def bubble(origin_list):
    n = 1
    while n < len(origin_list):
        for i in range(len(origin_list) - n):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i += 1]
print()

print('3-norm2')
def filter(f, seq):
    if f is None:
        f = bool
    return [x for x in seq if f(x)]
print('filter:', filter(lambda x: x > 5, [1,2,5,6,7,1,10,20]))
print('filter:', filter(None, [0,1,'',None,[],[1,2]]))

# как решать задачу 3 урока - 4 альтернативная, надо считать сумму квадратов a,b,c in ax^2+bx+c?