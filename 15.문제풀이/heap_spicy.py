# 스코빌 가장 낮은 음식 + (스코빌 두번째로 낮은 음식 * 2) = 새로운 스코빌 
# 모든 음식의 스코빌 지수가 K이상 일때 최소 섞은 횟수가 답
# 모든 음식의 스코빌 지수를 k 이상으로 만들 수 없는 경우 -1 return 

import heapq 

scoville = [1, 2, 3, 9, 10, 12]
K = 7
def solution(scoville, K):
  answer = 0
  heapq.heapify(scoville)

  # 내림차순이기 때문에 가장 앞에 오는 작은 숫자가 K 보다 크면 섞을 필요 없음! 

  while scoville[0] <= K:
      first = heapq.heappop(scoville)
      second = heapq.heappop(scoville)
      mix = first + (second * 2)
      heapq.heappush(scoville, mix)
      answer += 1
      if len(scoville) == 1 and scoville[0] < K:
        return -1
      return answer
# print(answer)

# heapq 쓰니까 런타임 에러남..! 

# scoville.sort()
# while scoville[0] <= K:
#     first = scoville[0]
#     second = scoville[1]
#     del scoville[0]
#     del scoville[1]
#     mix = first + (second * 2)
#     scoville.append(mix)
#     answer += 1
# print(answer)

#  얘가 더 안됨