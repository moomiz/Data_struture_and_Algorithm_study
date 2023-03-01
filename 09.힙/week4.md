# 힙(heap)
## :  힙 성질(heap property) 만족하는 이진 트리

H = [a, b, c , 공 , d, e, f]
0 : a
1 : b, c 
2 : 공, d, e, f

H[0]의 
왼쪽 자식노드: H[1]
오른쪽 자식노드: H[2]

H[2]의 왼쪽 자식노드: H[2*2+1] = H[5] = e
H[2]의 오른쪽 자식노드: H[2*2+2] = H[6] = f

H[k]의 왼쪽 자식노드 : H[2*k+1]
H[k]의 오른쪽 자식노드 : H[2*k+2]

H[k]의 부모노드 : H[(k-1)//2]

## heap 성질 :
 모든 부모노드의 키값은 자식 노드의 키값보다 작지 않다.

## heap:
1. 모양
2. heap 성질

## 루트노드 :
 가장 큰 값 make heap 제공 연산

## 제공연산:
1. Insert
2. find_max : return A[0]
3. delete_max

## make-heap 
:heapify-down