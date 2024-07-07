'''
Problem: Merge Intervals

Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
    - 1 <= intervals.length <= 10^4
    - intervals[i].length == 2
    - 0 <= starti <= endi <= 10^4
'''

def merge(intervals):
    # Sort intervals based on start times
    intervals.sort(key=lambda x: x[0])
    
    result = []
    
    for interval in intervals:
        # If result is empty or if there's no overlap,
        # simply append the current interval
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            # There is an overlap, so merge the current and previous intervals
            result[-1][1] = max(result[-1][1], interval[1])
    
    return result

# Test cases
if __name__ == "__main__":
    print(merge([[1,3],[2,6],[8,10],[15,18]]))  # Expected output: [[1,6],[8,10],[15,18]]
    print(merge([[1,4],[4,5]]))  # Expected output: [[1,5]]