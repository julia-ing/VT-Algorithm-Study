# 파이썬 | 그리디 알고리즘

Week: 0
URL: https://school.programmers.co.kr/learn/courses/30/lessons/42891
문제 이름: 무지의 먹방 라이브
유형: 그리디

## 파이썬

### 파이썬3의 range는 어떤 것일까?

[[python] Lazy Evaluation | 코딩장이 (itholic.github.io)](https://itholic.github.io/python-lazy-evaluation/)

python2에서는 range와 xrange를 구분했는데, python3부터는 range가 되었다. 

range는 generator로 list와 다르게 lazy evalutaion을 통해 메모리 효율성을 높였다. 

- Lazy evaluation란?
    
    generator()를 사용하며, 실제 값이 쓰이기 전까지 연산을 미루는 동작이다. generator에서 yield 값을 리턴한다.
    
    값을 사용할지 여부가 불확실할 때 사용하면 리스트보다 좋다. 
    

### 파이썬 dict에서 get()을 쓰는 이유

[210924 개발기록: 파이썬 dictionary, get()을 사용해야하는 이유 (tistory.com)](https://junior-datalist.tistory.com/203)

null로 인해 프로그램이 종료되는 에러를 막기 위해서 return할 default값을 설정하여 get()을 사용하는 것이 안전하다. 

```python
dict1 = { 'a':3, 'b':1 }
dict1.get('a', 0) # dict.get({키 이름}, {default 값})
```

## Greedy 알고리즘

### 그리디 문제를 풀 때 점검해야할 것

- 정당성 (그리디하게 연산하는 것이 논리적으로 올바른지)

### 그리디 구현할 때 쓰는 요소들

- 정렬 (min, max값, 우선순위 큐)
- 반복문 (재귀, for문, while문)

### 문제) 무지의 먹방 라이브

```
import heapq

def solution(food_times, k):

    if sum(food_times) <= k:
        return -1

    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    time=0
    sub=0
    length=len(food_times)

    while time + ((q[0][0]-sub)*length) <=k:
        now = heapq.heappop(q)[0]
        time += (now-sub)*length
        length-=1
        sub=now

    result = sorted(q, key=lambda x:x[1])

    return result[(k-time)%length][1]
```

키워드: `heap`, `greedy`