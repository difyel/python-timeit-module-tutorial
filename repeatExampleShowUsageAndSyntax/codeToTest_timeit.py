# import the modules
import timeit
import time

testData = [
    'this is a test data',
    'the aim is to verify',
    'which of the splitting function',
    'is going to perform better',
    'the number of iteration here is 235712',
    'and this is why the repeat can be usefull',
    'since sometimes just running a test once',
    'we can get a result which is not true'
]


# def splitUsingRegex(messageToSplit: str, separator: str = '\s'):
# def splitUsingLoop(messageToSplit: str, separator: str = [' ', '\t', '\n', '\r', '\x0b', '\x0c']):


splitUsingRegexTimingResult = timeit.repeat(
    setup='from codeToTest import splitUsingRegex , splitUsingLoop',
    stmt='[splitUsingRegex(data) for data in testData]',
    number=235712,
    repeat=5,
    globals=globals(),
    timer=time.perf_counter

)

splitUsingLoopTimingResult = timeit.repeat(
    setup='from codeToTest import splitUsingRegex , splitUsingLoop',
    stmt='[splitUsingLoop(data) for data in testData]',
    number=235712,
    repeat=5,
    globals=globals(),
    timer=time.perf_counter

)

for _splitUsingLoopTimingResult, _splitUsingRegexTimingResult in zip(splitUsingLoopTimingResult, splitUsingRegexTimingResult):
    if _splitUsingLoopTimingResult < _splitUsingRegexTimingResult:
        print(
            f'splitUsingLoop : {_splitUsingLoopTimingResult} is faster than splitUsingRegex {_splitUsingRegexTimingResult} ')
    else:
        print(
            f'splitUsingLoop : {_splitUsingLoopTimingResult} is slower than splitUsingRegex {_splitUsingRegexTimingResult} ')
