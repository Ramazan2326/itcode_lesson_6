from datetime import datetime
from django.http import HttpResponse


def normalize_number(number):
    if number // 10 == 0:
        number = '0' + str(number)
    return number


def get_current_date_time(request):
    current_date = datetime.now()
    current_day = current_date.day
    current_month = current_date.month
    current_year = current_date.year

    current_hour = current_date.hour
    current_minutes = current_date.minute

    current_day = normalize_number(current_day)
    current_month = normalize_number(current_month)
    current_hour = normalize_number(current_hour)
    current_minutes = normalize_number(current_minutes)

    return HttpResponse(f"<h1>Текущая дата и время </h1><br>"
                        f"Дата: {current_day}.{current_month}.{current_year}"
                        f"<br> Время: {current_hour}:{current_minutes}")
