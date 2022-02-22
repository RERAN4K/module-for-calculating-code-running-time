def language(lan):
    global language
    language = lan


def worktimebeg():
    import time as t
    global start
    start = t.time()


def worktimeend():
    global firstwords, name_s, name_m
    import time as t
    end = t.time()
    total_ts = end - start
    total_s = total_ts % 60
    total_m = int(total_ts // 60)
    if language == 'ru':
        firstwords = 'Программа выполнилась за'
        if total_s % 10 > 4 or total_s % 10 == 0 and total_s > 4 or total_s < 19:
            name_s = 'секунд'
        if 1 < total_s % 10 < 5 and total_s < 5 or total_s > 19:
            name_s = 'секунды'
        if total_s % 10 == 1 and total_s < 2 or total_s > 19:
            name_s = 'секунду'
        if total_m % 10 > 4 or total_m % 10 == 0 and total_m > 4 or total_m < 19:
            name_m = 'минут'
        if 1 < total_m % 10 < 5 and total_m < 5 or total_m > 19:
            name_m = 'минуты'
        if total_m % 10 == 1 and total_m < 5 or total_m > 19:
            name_m = 'минуту'
    elif language == 'en':
        firstwords = 'The program was completed in'
        if total_s == 0 or total_s != 1:
            name_s = 'seconds'
        else:
            name_s = 'second'
        if total_m != 1:
            name_m = 'minutes'
        else:
            name_m = 'minute'
    if total_m == 0:
        print(firstwords, '%.0f' % total_s, name_s)
    else:
        print(firstwords, total_m, name_m, '%.0f' % total_s, name_s)
