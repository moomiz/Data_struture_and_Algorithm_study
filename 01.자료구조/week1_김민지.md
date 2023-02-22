# 자료구조(DATa structure) , 알고리즘 (Algorithm)

## 자료 : data 
### data ->[ 저장공간(memory) + 읽기, 쓰기, 삽입, 삭제, 탐색 ] => 구조 

### 알고리즘 :  data 입력(유한한 횟수의 연산들) -> 정답 출력 

## 자료구조 예:
1) 변수 (variable)
2) 배열 (arrary), 리스트(list)

* 인류최초의 알고리즘: 최대공약수(GCD)계산 알고리즘
* gcd(8,12) = max{1,2,4} = 4
```
gdc(a,b):
    while a! = 0 and b! = 0:
        if a>b: a = a-b
        else: b = b-a
    return a+b
```