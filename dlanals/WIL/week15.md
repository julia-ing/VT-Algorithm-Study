# 파이썬 알고리즘 인터뷰

## 10. 데크, 우선순위 큐
- 데크 (Deque)
  - 스택과 큐의 연산을 모두 갖고 있는 복합 자료형
  - Double-Ended Queue의 줄임말
  - 양쪽 끝을 모두 추출할 수 있는, 큐를 일반화한 형태의 추상 자료형(ADT).
  - 구현은 배열이나 연결 리스트 모두 가능하지만, 특별히 이중 연결 리스트로 구현하는 편이 가장 잘 어울림
    - ![image](https://user-images.githubusercontent.com/97150219/232277549-666418f1-2002-4163-954f-4c7fe1fa9f64.png)
    - 이중 연결리스트로 구현하게 되면, head와 tail이라는 이름의 투 포인트를 가지게 됨
    - 새로운 아이템이 추가될 때마다 앞쪽 또는 뒤쪽으로 연결시켜주기
    - 연결 후에는 포인터 이동
  - collections 모듈에서 deque라는 이름으로 지원
    - collections.deque는 이중 연결 리스트로 구현되어 있음.

### 641) Design Circular Deque
- Medium

#### 의식의 흐름
- deque를 직접 구현하려면 이중 연결리스트 클래스부터 정의?
- 어디서부터 정의해줘야할지 모르겠다..! 솔루션 앞부분 참고
  - ListNode 사용해준거면 ListNode도 따로 정의해줘야하는 것 아닌가?
  - insertFront 메소드에서 _add -> 템플릿에 없는 새로운 메소드 추가?
- inserfFront -> head에 _add 해준 후 head 바꿔줘야하는것 아닌가
- 의문점이 너무 많아서 솔루션 전체를 읽어봐야겠다!

#### Solution
```python

```
- _add
  - 이중 연결리스트에 신규 노드 삽입
  - _add에서 '_' : 내부에서만 사용한다는 의미
  - 오른쪽에 새로운 노드 삽입

- 의문점 -> 해결 후 코드 추가 예정
  - ListNode 정의
  - head, tail 변경
  - _del에서 node삭제가 아니라 node.right을 삭제하고 있는게 아닌가

- 사실상 원형 데크를 이중 연결리스트로 구현하게 되면 원형의 이점을 살릴 수 없게 됨.
  - 원형으로 구현하는 이유는 뒤쪽으로 요소를 채우다가 공간이 다 차게되면 tail과 head를 연결해 앞쪽의 빈 공간을 활용하려는 의도인데,  
    연결리스트는 애초에 빈 공간이라는 개념이 존재하기 않기 때문에 원형은 아무런 의미가 없게 됨.
  - 데크의 연산은 맨 처음과 맨 끝의 값을 추출할 뿐, 맨 끝의 다음 값을 추출하는지 등의 연산은 존재 X  
    -> 서로 연결되어 있을 필요 또한 없음
   
## 11. Hash Table
- Hash table
  - 대부분의 연산이 분할 상환 분석에 따른 시간 복잡도가 O(1)

### Hash
- 해시 함수 : 임의 크기 데이터를 고정 크기 값으로 매핑하는 데 사용할 수 있는 함수
- ex)  
  ABC     -> A1  
  1324BC  -> CB  
  AF32B   -> D5  
  각각 글자 수는 다르지만 화살표로 표시한 특정 함수를 통과하면 2바이트의 고정 크기 값으로 매핑됨.  
  이때 화살표 역할을 하는 함수가 해시 함수
- 해시 테이블을 인덱싱하기 위해 이처럼 해시 함수를 사용하는 것이 Hashing
- 정보를 가능한 한 빠르게 저장하고 검색하기 위해 사용하는 중요한 기법
- 최적의 검색이 필요한 분야에 사용됨
- 성능 좋은 해시 함수들의 특징
  - 해시 함수 값 충돌의 최소화
  - 쉽고 빠른 연산
  - 해시 테이블 전체에 해시 값이 균일하게 분포
  - 사용할 키의 모든 정보를 이용하여 해싱
  - 해시 테이블 사용 효율이 높을 것

#### Birthday Problem
- 생각보다 충돌이 쉽게 일어나는 흔한 예
- 생일의 가짓수는 365개이므로, 비둘기집 원리(Pigeonhole Principle)에 따라 366명 이상이 모여야 생일이 같은 2명이 존재할 것 같지만  
  실제로는 23명만 모여도 50%를 넘고, 57명이 모이면 99%를 넘어섬
- 실험
  ```python
  import random
  
  TRIALS = 100000
  same_birthdays = 0  # 생일이 같은 사람이 있는 실험의 수
  
  # 10만번 실험 진행
  for _ in range(TRIALS):
    birthdays = []
    
    # 23명이 모였을 때, 생일이 같은 경우 same_birthdays += 1 후 break
    for i in range(23):
      birthday = random.randint(1, 365)
      if birthday in birthdays:
        same_birthdays += 1
        break
      birthdays.append(birthday)
      
  # 전체 10만 번 실험 중 생일이 같은 사람이 있는 실험의 확률
  print(f'{same_birthdays / TRIALS * 100}%')
  ```
  -> 50.708%
  
#### Load Factor
- 해시 테이블에 저장된 데이터 개수 n을 버킷의 개수 k로 나눈 것  
  load factor = n / k
- 

### 문제번호) 제목
- 난이도

#### 의식의 흐름


#### Solution

```python

```

#### What I learned
