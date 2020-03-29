import csv
from time import strptime

def timeFromStr(string):
    time = int(string.split(":")[0]) + (12 if string[-2] == 'P' else 0)
    print(time)
    return time


def monthFromStr(string):
    month = strptime(string, '%B').tm_mon
    print(month)
    return month


def addTimeRange(times, s, e):
    if s >= e:
        e += 24
    for i in range(s, e):
        times += pow(2, i % 24)
    return times


def addMonthRange(months, s, e):
    if s >= e:
        e += 12
    for i in range(s - 1, e):
        months += pow(2, i % 12)
    return months


def importData():
    with open("Fishing - Data.csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if (len(row["Fish"]) > 1):
                fish_name = row["Fish"]
                location = None
                for l in Fish.LOCATIONS:
                    if (row["Location"] == l[1]):
                        location = l[0]
                        break
                size = None
                for s in Fish.SIZES:
                    if (row["Size"] == s[1]):
                        size = s[0]
                        break
                times = 0
                times = addTimeRange(times, timeFromStr(row["Start Time"]), timeFromStr(row["End Time"]))
                if (len(row["Start Time 2"]) > 0):
                    times = addTimeRange(times, timeFromStr(row["Start Time 2"]), timeFromStr(row["End Time 2"]))

                months = 0
                months = addMonthRange(months, monthFromStr(row["Start Month"]), monthFromStr(row["End Month"]))
                if (len(row["Start Month 2"]) > 0):
                    months = addMonthRange(months, monthFromStr(row["Start Month 2"]), monthFromStr(row["End Month 2"]))
                if (len(row["Start Month 3"]) > 0):
                    months = addMonthRange(months, monthFromStr(row["Start Month 3"]), monthFromStr(row["End Month 3"]))
                price = int(row["Price"].replace(',', ''))
                # print(fish_name, location, size, "{0:024b}".format(times), "{0:012b}".format(months), price)
                fish = Fish(name=fish_name, location=location, size=size, months=months, times=times, price=price)
                fish.save()
    return JsonResponse([Fish.objects.all().count()], safe=False)