def decor1(sayhello):
    print("outise decor1")
    def wrapper():
        print("Before function - decor1")
        sayhello()
        print("Before function - decor1")
    return wrapper


def decor2(sayhello):
    def wrapper():
        print("Before function - decor2")
        sayhello()
        print("Before function - decor2")
    return wrapper


@decor2
@decor1
def sayhello():
    print("Hello Disha")

sayhello()