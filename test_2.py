# find abundant, deficient perfect number, Ref >>> https://stackoverflow.com/questions/40064750/python-abundant-deficient-or-perfect-number/40064812

def get_divs(n):
    return [i for i in range(1, n) if n % i == 0]

def classify(num):
    divs_sum = sum(get_divs(num))
    if divs_sum > num:
        print('{} is abundant number'.format(num))
    elif divs_sum < num:
        print('{} is deficient number'.format(num))
    elif divs_sum == num:
        print('{} is perfect number'.format(num))

for x in range(100):
    classify(x)
