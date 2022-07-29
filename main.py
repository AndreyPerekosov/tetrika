import requests
from bs4 import BeautifulSoup

URL = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'


# Task 1
def binary_search(A):
    left = -1
    right = len(A)
    while left <= right - 1:
        middle = (left + right) // 2
        if A[middle - 1] + A[middle] == '10':
            return middle
        elif A[middle] == '1':
            left = middle + 1
        else:
            right = middle - 1
    return False


# Task 2
def get_letters(url):
    word_dict = {}
    href = url
    count = 1
    while href:
        request = requests.get(href)
        href = BeautifulSoup(request.text, 'html.parser').find('a', string='Следующая страница')
        content = BeautifulSoup(request.text, 'html.parser').find(class_='mw-category-columns').findAll('a')
        for h in content:
            char = h.getText()[0].upper()
            if word_dict.get(char):
                word_dict[char] += 1
            else:
                word_dict[char] = 1
        if href:
            href = 'https://ru.wikipedia.org/' + href.get('href')
            count += 1
    print(word_dict)


# Task 3
def helper(data):
    for value in data.values():
        if not (len(value)):
            return False
    return True


def appearance(intervals):
    prepared_data = []
    markers_dict = dict()
    for key in intervals.keys():
        markers_dict[key] = []
        for i in range(len(intervals[key])):
            tmp = intervals[key][i]
            if i % 2:
                prepared_data.append((tmp, '-' + key))
            else:
                prepared_data.append((tmp, '+' + key))
    prepared_data.sort(key=lambda x: x[0])
    timer = 0
    marker = False
    test_seq = []
    for item in prepared_data:
        if item[1][0] == '+':
            markers_dict[item[1][1:]].append(1)
        else:
            markers_dict[item[1][1:]].pop()
        if helper(markers_dict):
            if not marker:
                marker = True
                timer -= item[0]
                test_seq.append(item[0] * -1)
        else:
            if marker:
                timer += item[0]
                marker = False
                test_seq.append(item[0])
    return timer


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    test = '111111111110000000000'
    print(binary_search(test))
    # get_letters(URL)
    # for i, test in enumerate(tests):
    #     test_answer = appearance(test['data'])
    #     assert test_answer == test[
    #         'answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
