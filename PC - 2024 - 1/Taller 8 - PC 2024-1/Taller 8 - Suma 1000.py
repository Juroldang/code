#Taller 8 - Suma 1000
def main():
    nums = list(map(int, input().split()))
    print(sum1000(nums))
def sum1000(nums):
    comp = {}
    count500 = 0
    nums = sorted(nums)
    for i in range(len(nums)):
        if nums[i] == 500:
            count500 += 1
            if count500 > 1: return 'SI'
        elif 1000-nums[i] not in comp: comp[1000-nums[i]] = nums[i]
    for i in range(len(nums)):
        if nums[i] in comp: return 'SI'
    return 'NO'
main()