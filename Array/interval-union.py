def find_missing_intervals(intervals, n):
    intervals.sort()
    result = []
    curr = intervals[0]

    for i in intervals:

        if i[0] <= interval[1]:
            curr[1] = _interval[1]

        if i[0] > interval[1]:
            gap = [curr[1]+1, i[0]-1]
            result.append(gap)
            curr = i

    gap = [curr[1]+1, n]
    result.append(gap)

    return result

garden = [[1,2], [5,6]]
n = 8

missing_intervals = find_missing_intervals(garden, n)
print(missing_intervals)