from re import match


def get_longest_sorted_asc(lst):
    # :param lst: list of numbers
    # :return: longest sequence of sorted numbers
    current_min_index = 0
    min_index = max_index = 0
    for current_max_index, i in enumerate(lst[1:]):
        if lst[current_max_index] > i or current_max_index + 2 == len(lst):
            if lst[current_max_index] < i:
                current_max_index += 1
            if max_index - min_index < current_max_index - current_min_index:
                min_index, max_index = current_min_index, current_max_index
            current_min_index = (current_max_index := current_max_index + 1)
    return lst[min_index: max_index + 1]


def test_get_longest_sorted_asc():
    # test function for get longest sorted asc
    assert get_longest_sorted_asc([4, 3, 4, 5, 6]) == [3, 4, 5, 6]
    assert get_longest_sorted_asc([9, 10, 1, 2, 3, 2]) == [1, 2, 3]
    assert get_longest_sorted_asc([1, 2, 3, 4]) == [1, 2, 3, 4]


def get_longest_average_below(lst, average):
    # :param lst: list of integers
    # :param average: a float value
    # :return: a list of integers representing
    # the maximum sequence of numbers that have
    # the average lower than the average variable
    current_min_index = 0
    min_index = max_index = 0
    current_average = lst[0]
    count = 1
    for current_max_index, i in enumerate(lst[1:]):
        if (current_average := current_average + i) / (count := count + 1) > average or \
                current_max_index + 2 >= len(lst):
            if current_average / count <= average:
                current_max_index += 1
            if max_index - min_index < current_max_index - current_min_index:
                min_index, max_index = current_min_index, current_max_index
            current_average = i
            count = 1
            current_min_index = (current_max_index := current_max_index + 1)
    return lst[min_index: max_index + 1]


def test_get_longest_average_below():
    # test function for get longest average below
    assert get_longest_average_below([1, 2, 3], 2) == [1, 2, 3]
    assert get_longest_average_below([5, 10, 6, 4, 4, 4, 4], 4) == [4, 4, 4, 4]


def is_prime(n):
    # :param n: integer
    # :return: true if n is prime, false otherwise
    return not match(r'^1?$|^(11+?)\1+$', '1' * n)


def test_is_prime():
    assert is_prime(11)
    assert not is_prime(4)
    assert is_prime(13)


def get_longest_concat_is_prime(lst):
    max_seq = []
    for left in range(len(lst)):
        for right in range(left, len(lst)):
            if is_prime(int(''.join(map(str, lst[left: right + 1])))):
                if len(max_seq) < right - left + 1:
                    max_seq = lst[left: right + 1]
    return max_seq


def test_get_longest_concat_is_prime():
    assert get_longest_concat_is_prime([1, 2, 3, 1]) == [1, 2, 3, 1]
    assert get_longest_concat_is_prime([1, 1, 2]) == [1, 1]


def menu():
    print('1. read list')
    print('2. get first prop')
    print('3. get second prop')
    print('4. quit')


def main():
    menu()
    lst = []
    while (option := input('your option: ')) != '4':
        if option == '1':
            lst = [int(x) for x in input().split(' ')]
        elif option == '2':
            print(get_longest_sorted_asc(lst))
        elif option == '3':
            average = float(input('enter average: '))
            print(get_longest_average_below(lst, average))
        else:
            print('invalid option')


if __name__ == '__main__':
    test_get_longest_sorted_asc()
    test_get_longest_average_below()
    test_get_longest_concat_is_prime()
    main()
