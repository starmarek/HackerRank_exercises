def is_leap(yearr):

    if yearr % 4 == 0:
        if yearr % 100 == 0:
            if yearr % 400 == 0:
                return True
            return False
        return True
    return False


year = int(input())
print(is_leap(year))
