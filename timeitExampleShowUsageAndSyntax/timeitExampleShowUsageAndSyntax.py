import timeit
import time

# define the sum , and multiplication function


def sum(x, y):
    return x + y


def mul(x, y):
    return x * y


# test the sum function

sumTimingResult = timeit.timeit(
    globals=globals(),
    setup='xData= range(0,100);  yData = range(220 , 320)',
    stmt='[  sum(x,yData[index]) for index,x in enumerate(xData)]',
    number=10000,
    timer=time.perf_counter
)

# test the mul function
mulTimingResult = timeit.timeit(
    globals=globals(),
    setup='xData = range(0,100); yData =range(220 , 320)',
    stmt='[  mul(x,yData[index]) for index,x in enumerate(xData)]',
    number=10000,
    timer=time.perf_counter
)

# compare the result
if sumTimingResult < mulTimingResult:
    print(
        f'The sum function {sumTimingResult} is faster than the mul function {mulTimingResult}')
else:
    print(
        f'The sum function {sumTimingResult} is slower than the mul function {mulTimingResult}')
