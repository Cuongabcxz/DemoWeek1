import datetime
from datetime import timedelta, datetime

# begin: 30-10-2001-16:40:20
# end: 10-12-2002-17:46:23


class CalculateDifferenceDate:

    def __init__(self, begin_str, end_str):
        self.begin_str = begin_str
        self.end_str = end_str

    def create_date_input(self):
        if begin_str != "" and end_str != "":
            begin_date = self.format_date(begin_str)
            end_date = self.format_date(end_str)
            self.cal_difference_date(begin_date, end_date)
        else:
            print("Not variable!!")

    def format_date(self, date_text):
        format_date = "%d-%m-%Y-%H:%M:%S"
        try:
            date = datetime.strptime(date_text, format_date)
            return date
        except ValueError:
            raise ValueError(f"Incorrect data format, should be {format_date}")

    def cal_difference_date(self, begin_date, end_date):
        difference = end_date - begin_date
        difference_day = difference.days
        difference_year = end_date.year - begin_date.year
        difference_month = (end_date.year - begin_date.year) * 12 + (end_date.month - begin_date.month)
        difference_second = difference.seconds + difference_day * 24 * 60 * 60
        difference_munite = difference_second // 60
        difference_hour = difference_munite // 60
        print(f"difference between dates in {difference_year} year, {difference_month} months, "
              f"{difference_day} days, {difference_hour} hour, {difference_munite} munites, "
              f"{difference_second} seconds")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    begin_str = str(input('Enter a day begin in DD-MM-YY-H:M:S format'))
    end_str = str(input('Enter a day end in DD-MM-YY-H:M:S format'))
    cal_diff_date = CalculateDifferenceDate(begin_str, end_str)
    cal_diff_date.create_date_input()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
