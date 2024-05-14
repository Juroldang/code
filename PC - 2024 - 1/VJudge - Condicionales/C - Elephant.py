#C - Elephant
x =int(input())
steps = 0
if x%5 == 0:
    print(x//5)
else:
    steps = x//5
    x = x%5
    if x%4 == 0:
        print(steps + x//4)
    else:
        steps += x//4
        x = x%4
        if x%3 == 0:
            print(steps + x//3)
        else:
            steps += x//3
            x = x%3
            if x%2 == 0:
                print(steps + x//2)
            else:
                steps += x//2
                x = x%2
                print(steps + x)