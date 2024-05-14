#Taller 8 - Parejas de XOR = 0
def main():
    N = int(input())
    nums = input().split()
    print(xor(nums))
def xor(nums):
    count = 0
    dic = {}
    for i in range(len(nums)):
        if nums[i] not in dic:
            dic[nums[i]] = [i]
        else: dic[nums[i]].append(i)
    for val in dic:
        count = count+((len(dic[val])-1)*(len(dic[val]))//2)
    return count
main()