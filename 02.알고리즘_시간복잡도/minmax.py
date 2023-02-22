T = int(input())
for tc in range(1,T+1):
    N = int(input())
    nums = list(map(int,input().split()))
    maxnum = 0  #최댓값   
    minnum = 1000001 # 최솟값
    for num in nums:
        if num >= maxnum:
            maxnum = num
        if num <= minnum:
            minnum = num

    result = maxnum-minnum
    print(f'{tc} {result}')
