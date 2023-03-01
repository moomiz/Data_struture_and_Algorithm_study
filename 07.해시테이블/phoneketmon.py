# nums는 폰켓몬의 종류 번호가 담긴 1차원 배열입니다.
# nums의 길이(N)는 1 이상 10,000 이하의 자연수이며, 항상 짝수로 주어집니다.
# 폰켓몬의 종류 번호는 1 이상 200,000 이하의 자연수로 나타냅니다.
# 가장 많은 종류의 폰켓몬을 선택하는 방법이 여러 가지인 경우에도, 
# 선택할 수 있는 폰켓몬 종류 개수의 최댓값 하나만 return 하면 됩니다.

# def solution(nums):
#     answer = 0
#     type = set(nums)
    
#     return answer

# answer =0
# nums = [2,2,4,3,3,3]
# take = len(nums)//2 # 가져갈 수 있는 포켓몬 수  2
# typemon = len(set(nums)) # 중복 제거하고 남은 포켓몬 수 
# if take <= typemon:
#     answer = take
# else:
#     answer = typemon

# print(answer)

# def solution(nums):
#     answer = 0
#     takemon = len(nums)//2 # 가져갈 수 있는 포켓몬 수 
#     typemon = len(set(nums)) # 중복 제거하고 남은 포켓몬 수 
#     if takemon <= typemon:   # 가져갈 수 있는 포켓몬 수 보다 중복제거한 포켓몬 수가 더 많으면 
#         answer = takemon
#     else:
#         answer = typemon

#     return answer

clothes=[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

print(len(clothes))