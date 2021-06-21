class Solution:
    def __init__(self):
        self.res = []
        self.cur_hour = 0
        self.cur_min = 0

    def time_format_conversion(self):
        hour_str = str(self.cur_hour)

        min_str = str(self.cur_min) if self.cur_min >= 10 else "0" + str(self.cur_min)

        return hour_str + ":" + min_str

    def DFS(self, arr, cur_LEDs, tar_LEDs):
        if self.cur_hour > 11 or self.cur_min > 59:
            # early break, invalid time format
            return
        if cur_LEDs == tar_LEDs:
            # target found
            # add path to res
            self.res.append(self.time_format_conversion())
            return
        if not arr:
            return

        for i, x in enumerate(arr):
            # append
            if x % 60 == 0:
                # x is a hour
                self.cur_hour += x // 60
            else:
                # x is a minute
                self.cur_min += x
            # recurse
            self.DFS(arr[i + 1:], cur_LEDs + 1, tar_LEDs)
            # pop
            if x % 60 == 0:
                # x is a hour
                self.cur_hour -= x // 60
            else:
                # x is a minute
                self.cur_min -= x

    def readBinaryWatch(self, turnedOn: int) -> [str]:
        if turnedOn < 0 or turnedOn > 10:
            raise Exception("Invalid Nubmer of LEDs: {0}".format(turnedOn))

        # merge two arrays
        # use x % 60 to determine element types(hour or minute)
        arr_hour = [x * 60 for x in [8, 4, 2, 1]]
        arr_minute = [32, 16, 8, 4, 2, 1]
        arr = arr_hour + arr_minute

        self.DFS(arr, 0, turnedOn)

        return self.res


if __name__ == "__main__":
    sol = Solution()
    print(sol.readBinaryWatch(2))
    res_2 = ["0:03", "0:05", "0:06", "0:09", "0:10", "0:12", "0:17", "0:18", "0:20", "0:24", "0:33", "0:34", "0:36",
             "0:40", "0:48", "1:01", "1:02", "1:04", "1:08", "1:16", "1:32", "2:01", "2:02", "2:04", "2:08", "2:16",
             "2:32", "3:00", "4:01", "4:02", "4:04", "4:08", "4:16", "4:32", "5:00", "6:00", "8:01", "8:02", "8:04",
             "8:08", "8:16", "8:32", "9:00", "10:00"]
