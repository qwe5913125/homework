import re, os, sys

__author__ = 'ivn'

if __name__ == '__main__':
    name_pattern = r'My name is .*\.'
    is_name = re.match(name_pattern, 'Myname is Nikita')
    print('is_name:', bool(is_name))

    is_name = re.match(name_pattern, 'I am just string!')
    print('is name:', bool(is_name))

    name_pattern_group = r'My name is (.*)\.'

    name = re.findall(name_pattern_group, 'My name is Nikita.')
    print(name)




with open('../regular/ParseData.txt', 'r') as r:
    data = r.read()

    pattern_data = r'\d\d/\D\D\D/\d\d\d\d'
    x = re.findall(pattern_data , data)
    pattern_for_pach = r'django.*[:]'
    z =re.findall(pattern_for_pach, data)

    pattern_text =r'([][.*:.*:.*].*[:].*[]] )(.*)'
    y = re.match(pattern_text, data)
    y2 = re.match(pattern_text, data)



ee = list(m.group(2) for m in re.finditer(pattern_text, data))

for i in ee:
    print(i)

