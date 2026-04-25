# Given an array of intervals whereendi]overlapping intervals that cover all the intervals in the input. intervals[i] = [starti,
# merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

def mergeIntervals(intervals):

    intervals.sort()
    n = len(intervals)

    result = [intervals[0]]

    for i in range(1,n):
        if intervals[i][0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1],intervals[i][1])
        else:
            result.append(intervals[i])
    return result

n = int(input())
intervals = [list(map(int,input().split())) for _ in range(n)]

result = mergeIntervals(intervals)
for interval in result:
    print(interval[0],interval[1])
