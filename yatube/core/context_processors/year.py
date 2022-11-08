import datetime


def year(request):
    """Добавляет переменную с текущим годом."""

    years = datetime.datetime.now()

    return {
        'year': years.year
    }


years = year(year)
print(years)
