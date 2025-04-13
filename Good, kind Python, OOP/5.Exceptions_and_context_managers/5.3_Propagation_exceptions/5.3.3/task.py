def input_int_numbers():
    return tuple(map(int, input().split()))


end = False

while not end:
    try:
        print(*input_int_numbers())
    except ValueError:
        continue
    else:
        end = True