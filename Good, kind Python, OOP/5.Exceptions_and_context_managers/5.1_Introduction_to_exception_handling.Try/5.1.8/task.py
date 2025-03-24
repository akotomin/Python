lst_in = input().split()

def is_number(number):
    try:
        return int(number)
    except ValueError:
        try:
            return float(number)
        except ValueError:
            return number

lst_out = list(map(lambda x: is_number(x), lst_in))
