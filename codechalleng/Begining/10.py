expected = '''10
9
8
7
6
5
4
3
2
1
time is up
'''

def countdown_for(start=10):
    countdown_recursive(start)


def countdown_recursive(start=10):
    for i in reversed(range(1, start + 1)):
        print(i)
    print('time is up')



countdown_for(13)