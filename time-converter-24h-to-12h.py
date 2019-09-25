def time_converter(time):
    if '00:00' <= time <= '23:59':
        if time<'10:00':
            result = time[1:] + ' a.m.'
        elif time<'12:00':
            result = time + ' a.m.'
        elif time < '13:00':
            result = time + ' p.m.'
        else:
            time_split = time.split(':')
            result = str(int(time_split[0])-12) + ':' + time_split[1] + ' p.m.'
    return result


if __name__ == '__main__':
    print("Example:")
    print(time_converter('23:30'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
