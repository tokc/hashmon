def scale_to_range(original_number, original_range_width, new_range_width, new_range_offset):
    ''' Scale input number to a different range.
        To go from 0 - 999 to 600 - 900,
        first scale to the width of the range, 0 - 300,
        then add offset, 600. '''
    intermediate_number = original_number/original_range_width
    intermediate_number = intermediate_number*new_range_width
    final_number = intermediate_number + new_range_offset
    return int(final_number)

def make_hash(string):
    MOD_NUMBER = 22953686867719691230002707821868552601124472329079
    # With 20 digits as the multiplier, output is guaranteed to be at least
    # 20 digits. But we can reasonably assume the output to be upwards of
    # 50 - 70 digits?
    MULTIPLIER = 48112959837082048697
    string_number = '0'
    for character in string:
        string_number += str(ord(character))
    string_number = int(string_number)

    intermediate_number = string_number * MULTIPLIER % MOD_NUMBER
    intermediate_number = intermediate_number * MULTIPLIER % MOD_NUMBER
    intermediate_number = intermediate_number * MULTIPLIER % MOD_NUMBER
    intermediate_number = intermediate_number * MULTIPLIER % MOD_NUMBER
    intermediate_number = intermediate_number * MULTIPLIER % MOD_NUMBER
    intermediate_number = intermediate_number * MULTIPLIER % MOD_NUMBER
    intermediate_number = intermediate_number * MULTIPLIER % MOD_NUMBER

    final_number = intermediate_number * MULTIPLIER
    return final_number

if __name__ == '__main__':
    while True:
        a = input()
        b = make_hash(a)
        print(b)
        print(str(b)[:3])
        print(scale_to_range(int(str(b)[:3]), 1000, 301, 600))
        list_of_digits = list(str(b)[:3])
        list_of_digits = [int(d) for d in list_of_digits]
        print(list_of_digits)
        print(sum(list_of_digits))
