class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        timePoints = sorted(timePoints)
        min_diff = 720

        for i, t in enumerate(timePoints):
            hours, minutes = t.split(':')
            hours = int(hours)
            minutes = int(minutes)
            totalmin = hours * 60 + minutes
            timePoints[i] = totalmin
        
        for i in range(len(timePoints)-1):
            cur_diff = abs(timePoints[i+1] - timePoints[i])
            if cur_diff < min_diff:
                min_diff = cur_diff
        
        return min(min_diff, timePoints[0] + 1440 - timePoints[-1])

