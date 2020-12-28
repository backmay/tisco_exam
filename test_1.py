input_a = '9876543'
input_b = [
    '3467985',
    '7865439',
    '8743956',
    '3456789',
]

def is_same_ditgit_in_same_index(input_a, input_b):
    for index in range(len(input_a)):
        if input_a[index] == input_b[index]:
            print('{} : is Invalid'.format(input_b))
            return
    print('{} : is Valid'.format(input_b))

for index in range(len(input_b)):
    is_same_ditgit_in_same_index(input_a, input_b[index])
