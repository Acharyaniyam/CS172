from pair import Pair

if __name__ == '__main__':
    p1 = Pair(10,3)
    p2 = Pair(20)
    p3 = Pair()
    
    print(p1)
    print()
    print(p2)
    print()
    print(p3)
    
    
    print('p1 + p2 = ', p1 + p2)
    print('p1 - p2 = ', p1 - p2)
    
    print()
    first = p1[0]
    second = p1[1]
    print(p1)
    print(first, second)
    
    print()
    print(p2)
    p2[0] = 1000
    p2[1] = 2000
    print('after')
    print(p2)
    
    if p1 == p2:
        print('the two pairs hold the same values')
        