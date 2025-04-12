lst_in = input().split()

def is_integer(number):
    try:
        return int(number)
    except ValueError:
        return False


new_lst = sum(list(map(int, filter(lambda x: is_integer(x), lst_in))))
print(new_lst)