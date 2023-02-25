from datetime import datetime

# 2002-12-30


class DetermineDate:
    def __init__(self, day_input):
        self.day_input = day_input

    def add_date_input(self):
        res = True
        if day_input != " ":
            date = self.format_date(day_input)
            self.determine_date(date)
            val_timestamp = self.convert_timestamp(date)
            res = bool(val_timestamp)
            print("Integer timestamp in seconds: ", val_timestamp)
            if res:
                print("Convert timestamp to datetime", self.convert_datetime(val_timestamp))
        else:
            print("Not variable!!")

    def format_date(self, date_text):
        format_date = "%Y-%m-%d"
        try:
            date = datetime.strptime(date_text, format_date)
            return date
        except ValueError:
            raise ValueError(f"Incorrect data format, should be {format_date}")

    def determine_date(self, date):
        year, week_num, day_of_week = date.isocalendar()
        print("Year %d, Week Number %d, Day of the Week %d" % (
            year, week_num, day_of_week) + ", " + "Date: " + date.strftime("%d-%m-%Y") + " " + date.strftime("%A"))

    def convert_timestamp(self, date):
        dtimestamp = date.timestamp()
        return int(round(dtimestamp))

    def convert_datetime(self, dtimestamp):
        # Convert timestamp to datetime
        cvr_datetime = datetime.fromtimestamp(dtimestamp).strftime('%d-%m-%Y')
        return cvr_datetime


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    day_input = input("Enter a day in YY-MM-DD format")
    deter_date = DetermineDate(day_input)
    deter_date.add_date_input()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
