# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # sort intervals according to the starting point
        intervals = sorted(intervals, key=lambda i: i.start)
        
        if len(intervals)<=1: return intervals;
        
        start = intervals[0].start;
        end = intervals[0].end;
        result = [];
        
        for n in xrange(1,len(intervals)):
            i = intervals[n]
            if end < i.start:
                result.append(Interval(start,end));
                start = i.start;
                end = i.end;
            elif end >= i.start:
                end = max(end,i.end);
            if n == len(intervals)-1:
                result.append(Interval(start,end))
        return result
