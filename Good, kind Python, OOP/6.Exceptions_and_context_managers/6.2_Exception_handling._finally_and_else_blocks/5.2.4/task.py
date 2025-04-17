try:
    a,b = input().split()
    try:
        n_sum = int(a) + int(b)
    except:
        n_sum = float(a)+float(b)
except:
    n_sum = str(a)+str(b)
finally:
    print(n_sum)
