# 자료구조와 알고리즘 성능1: 가상 컴퓨터 + 가상언어 + 가상 코드 

HW/SW 환경 상이(!) 
* 가상 컴퓨터 (virtual machine) + 가상언어 (Pseudo Language) + 가상코드(Pseudo code)
* 가상 컴퓨터 : Turing Machine -> von Neumann : RAM (Random Access Machine)
RAM = CPU + Memory + 기본연산(단위시간에 수행되는 연산)
기본연산: 1시간 단위 
 -배정, 대입, 복사연산: A(쓰기) = B(읽기)
 -산술 연산: +, -, *, / : 1시간 (*, %, [], x)
 -비교연산: >, >= , <, ,<=, ==, != A < B <=> A-B < 0
 -논리연산: AND , OR, NOT
 -비트연산: bit-AND, OR, NOT 

가상언어(Pseudo/virtual Languages) 
 - 배정, 산술, 비교, 논리, bit-논리: 기본연산 표현
 - 비교: if, if else, if elseif(elif) ... else
 - 반복: for, while
 - 함수: 정의, 호출, return

 가상코드(pseudo Code) 
    algorithmn ArrayMax(A, n):
        A =[3,-1,9,2,12] n:5 
        무한히 많은 입력 
        무한히 많은 n 
        input:n개의 정수를 갖는 배열 A
        output:A의 수 중에서 최대값 리턴
        currentMax = A[0]
        for i = 1 to n-1 do
            if currentMax < A[i]:
                currentMax A[i]
        return currentMax


A = [_,_,_,_,_,_] n: input size
1) 모든 입력에 대해 기본 연산 횟수를 더한 후 평균 (현실적으로 불가능)
2) 가장 안 좋은 입력(worstcase input)에 대한 기본 연산 횟수를 측정 : worstcase time complexity
=> 어떤 입력에 대해서도 w.t.c보다 수행시간이 크지 않다! 

# 알고리즘 수행시간 = 최악의 입력에 대한 기본 연산 횟수 

Big-o 표기법: 알고리즘의 수행시간 = 최악의 경우의 입력에 대한 기본 연산 횟수
Algorithm1(arrayMax): T1(n) = 2n-1
1)Algorithm2가 Algorithm1 보다 2배 느리다.
Algorithm2(sum1): T2(n) = 4n+1 
2) Algorithm3 n < 5/3면 Algorithm 2보다 빠르다 
모든 n에 대해서 Algorithm 1보다 느리다
Algorith3(sum2): T3(n) = 3/2*n^2 - 3/2*n + 1
3)Algorithm3는 n > 5/3면 항상 Algorithm2 보다 느리다! 
T1(n), T2(n), T3(n)
T1(n),T2(n) :n에 대해 선형적으로 증가 
T3(n) :제곱으로 증가

수행시간 T(n) = 함수값을 결정하는 최고차항만으로 간단하게 표기: Big-o 표기법

1) 최고차항만 남긴다.
2) 최고차항 계수(상수)는 생략
3) Big-o (최고차항)
