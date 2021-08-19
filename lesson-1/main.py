from time import time
from functools import wraps

# constants
NUM_TYPE_EVEN = 'even'
NUM_TYPE_ODD = 'odd'
NUM_TYPE_SIMPLE = 'simple'

# varible types

# String
hello = "Hello"
# show string
print(hello)
print(hello[0])
print(hello[-1])
print(hello[0:-2])

# Int
intt = 1

# Float
floatt = 12.54234234

# List
lissts = ['foo', 'bar', 3, True, [1, 2, 3]]
print(lissts)
print(lissts[0])

# Tuples
tupless = (1, 2, 'foo', 'bar', ('spamm', 'eggs', 3))
print(tupless)
print(tupless[-1])

# Sets
setss = {1, 2, 3, 4, 'foo', 'bar', False}
print(setss)

# Dictionaries
dicts = {1: 'foo', 2: 'bar', 'spamm': 'eggs', 3: {'baz': 1}}
print(dicts)
print(dicts['spamm'])


# Decoratot function
def run_time_decor(func):
    print('In decorator')

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('In decorated function')
        stat = time()
        result = func(*args, **kwargs)
        end = time()
        time_diff = end - stat
        print(f"time diff: {time_diff:.15f}")
        return result

    print('In outer decorated function')
    return wrapper


# Function of exponentiation
@run_time_decor
def degree_up(nums, factor=4):
    num_dict = {}
    for n in nums:
        num_dict[n] = n ** factor
    return num_dict


print(degree_up((1, 2, 3, 4, 5, 6, 7, 8)))
print('Not decorated degree_up: ' ,degree_up.__wrapped__((1,2,3)))

# Nums auto-filter functions in range
@run_time_decor
def numsFilter(nums):
    num_dict = {}
    for i, n in enumerate(range(nums)):
        if n == 0:
            continue
        if n % 2 == 0:
            key = 'ev-' + str(i)
            num_dict[key] = n
        if n % 2 > 0:
            key = 'od-' + str(i)
            num_dict[key] = n
        if n == 2:
            key = 'si-' + str(i)
            num_dict[key] = n
        if n != 2:
            d = 2
            flag = True
            while d < n:
                if n % d == 0:
                    flag = False
                    break
                d += 1
            if flag:
                key = 'si-' + str(i)
                num_dict[key] = n
    return num_dict


print(numsFilter((30)))


# Nums arg-filter functions
@run_time_decor
def numsFilterArgs(nums, type=NUM_TYPE_EVEN):
    num_list = []
    for n in nums:
        if (type == 'odd') and (n % 2 > 0):
            num_list.append(n)
        if (type == 'even') and (n % 2 == 0):
            num_list.append(n)
        if (type == 'simple'):
            if n == 2:
                num_list.append(n)
            if n != 2:
                d = 2
                flag = True
                while d < n:
                    if n % d == 0:
                        flag = False
                        break
                    d += 1
                if flag:
                    num_list.append(n)

    return num_list


print(numsFilterArgs((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), NUM_TYPE_SIMPLE))


# Fibonacci functions
def fib(position):
    if position <= 1:
        return 1
    return fib(position - 1) + fib(position - 2)


# Fibonacci runner functions
@run_time_decor
def run_rib(position, renge=False):
    if range:
        fib_lists = []
        for i in range(position):
            fib_lists.append(fib(i))
        return fib_lists
    else:
        return fib(position)


print(run_rib(10, True))


# Fibonacci runner functions generator
@run_time_decor
def fib_run_gen(position):
    print('before generator')
    for i in range(position):
        print('in generate: ', i)
        yield fib(i)


print(list(fib_run_gen(20)))

for fi in fib_run_gen(20):
    if fi > 40:
        print(fi)
        print('fi great then 40')
        break
