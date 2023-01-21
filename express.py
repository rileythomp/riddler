month_days = {
    1: 31,
    2: 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

ans = 0

for month in month_days:
    for day in range(1, month_days[month]+1):
        if month + day <= 12 and month*day <= month_days[month+day]:
            ans += 1
        if month*day <= 12 and month + day <= month_days[month*day]:
            ans += 1

# double counted 02/02
print(ans - 1)