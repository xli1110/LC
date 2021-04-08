class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        area = (p2 - p1) * min(arr[p1], arr[p2])

        Assume that arr[p1] < arr[p2].
        area = (p2 - p1) * arr[p1]

        If we move p2 to p2' = p2 - 1.
        If arr[p1] <= arr[p2'], then area' = (p2' - p1) * arr[p1] < area, length decreases and height remains.
        If arr[p1] > arr[p2'], then area' = (p2' - p1) * arr[p2'] < area, length decreases and height decreases.
        We suck as we always get a smaller area.

        If we move p1 to p1' = p1 + 1.
        If arr[p1'] <= arr[p2], then area' = (p2 - p1') * arr[p1'] < area, length decreases and height remains.
        If arr[p1'] > arr[p2], then area' = (p2 - p1') * arr[p2] < area, length decreases and height increases.
        We MAY get a larger area. It depends.

        As a result, we move the pointer whose height is lesser then the other.
        """
        if len(height) < 2:
            raise Exception("Invalid Array: {0}".format(height))

        low = 0
        high = len(height) - 1
        area = (high - low) * min(height[low], height[high])

        while high - low >= 1:
            t = (high - low) * min(height[low], height[high])
            if t > area:
                area = t

            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
                
        return area
