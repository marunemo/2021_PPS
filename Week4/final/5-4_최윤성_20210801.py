class Solution(object):
    def dayOfYear(self, date):
        dayMonth = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31,
                    8:31, 9:30, 10:31, 11:30, 12:31}
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])
        doy = 0
        for m in range(1,month):
            doy += dayMonth[m]
        if year % 4 == 0 and month > 2:
            doy += 1
        doy += day
        return doy