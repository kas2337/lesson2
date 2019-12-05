from datetime import datetime, timedelta
import calendar
# Напечатайте в консоль даты: вчера, сегодня, месяц назад

date_today = datetime.now()
date_yesterday = date_today - timedelta(1)
day_in_month = calendar.mdays[date_today.month]
date_30_last_day = date_today - timedelta(day_in_month)
print(date_yesterday)
print(date_today)
print(date_30_last_day)


print()

# Превратите строку "01/01/17 12:10:03.234567" в объект datetime

date_string = "01/01/17 12:10:03.234567"
str_date = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
print(f'{str_date} type is {type(str_date)}')
