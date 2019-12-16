#
# d = {
#     key: value
# }

d = {
    1: 'first',
    2: 'second',
    'etc': 'etc'
}

list1 = [['a,', 1], ['b', 2], ['c', 3]]
dic = dict(list1)
print(dic, type(dic))

dic1 = {}

d4 = dict.fromkeys(['a', 'b', 'c'], 100)
print(d4, type(d4))


