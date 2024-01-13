from DAY5 import SockPairs

def test1():
    assert SockPairs("AA") == 1

def test2():
    assert SockPairs("ABABC") == 2

def test3():
    assert SockPairs("CABBACCC") == 4

if __name__ == "__main__":
    test1()
    test2()
    test3()
    print('all tests passed')