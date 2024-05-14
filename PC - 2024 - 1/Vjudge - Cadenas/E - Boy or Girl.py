#E - Boy or Girl
def main():
    S = input()
    print(girl_or_not(S))
def girl_or_not(S):
    if len(set(S))%2 == 0:
        return 'CHAT WITH HER!'
    else: return 'IGNORE HIM!'
main()