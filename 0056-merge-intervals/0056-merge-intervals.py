class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        sorted_intervals = sorted(intervals, key=lambda interval: interval[0])

        start, end = 0, 1
        
        while start <= len(sorted_intervals)-2 and end <= len(sorted_intervals)-1:
            if sorted_intervals[start][1] >= sorted_intervals[end][0] and sorted_intervals[start][1] < sorted_intervals[end][1]:
                sorted_intervals[start][1] = sorted_intervals[end][1]
                sorted_intervals.pop(end)
            elif sorted_intervals[start][1] >= sorted_intervals[end][0] and sorted_intervals[start][1] >= sorted_intervals[end][1]:
                sorted_intervals.pop(end)
            else: 
                start += 1
                end += 1

        return sorted_intervals
        