#B - Queue at the School
def main():
    inp = input().split()
    n, t = int(inp[0]), int(inp[1])
    Q = list(input())
    print(queue_school(n, t, Q))
def queue_school(n, t, Q):
    tempQ = Q.copy()
    for i in range(t):
        for j in range(n-1):
            if Q[j] == 'B' and Q[j+1] == 'G':
                tempQ[j], tempQ[j+1] = 'G', 'B'
        Q = tempQ.copy()
    return "".join(Q)
main()