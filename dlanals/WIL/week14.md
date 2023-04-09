# 파이썬 알고리즘 인터뷰
## 3. 파이썬
### 파이썬 문법
#### Generator
- 루프의 반복(Iteration) 동작을 제어할 수 있는 루틴 형태
- 만약 임의의 조건으로 숫자 1억 개를 만들어내 계산하는 프로그램을 작성한다고 할 때
  - 제너레이터가 없으면 메모리 어딘가에 만들어낸 숫자 1억개 보관하고 있어야 함
  - 제너레이터를 이용하면 단순히 제너레이터만 생성해두고 필요할 때 언제든 숫자 만들어낼 수 있음
- yield -> 제너레이터 리턴
  - 사전적 의미로 '양보하다'
  - 제너레이터가 여기까지 실행 중이던 값을 내보낸다는 의미
  - 중간값을 리턴한 다음 함수는 종료되지 않고 계속해서 맨 끝에 도달할 때까지 실행됨
  - 다음 값을 생성하려면 next()로 추출

#### range
- a = [n for n in range(1000000)], b = [range(1000000)]일 때
- len(a) = len(b) = 1000000로 동일
- 하지만 메모리 점유율에서 차이가 남
  - range 클래스에는 생성해야 한다는 조건만 존재하게 때문
  - a에는 미리 생성된 값이, b에는 생성해야 한다는 조건만 존재

#### enumerate
- 사전적 의미 : 열거하다
- 여러가지 자료형을 인덱스를 포함한 enumerate 객체로 리턴함

#### print
- .format 방식
  - print('{0}:{1}'.format(idx + 1, fruit))
  - 인덱스 생략 가능 -> print('{}:{}'.format(idx + 1, fruit))
- f-string(formated string literal)
  - print(f'{idx + 1} : {fruit}')

#### pass
- 일단 코드의 전체 골격을 잡아 놓고 내부에서 처리할 내용은 차근차근 생각하며 만들 때 유용
- Null Operation으로 아무것도 하지 않는 기능
- 불필요한 오류 방지
- 먼저 mockup 인터페이스로부터 구현한 다음에 추후 구현 진행할 수 있게 해줌
- 온라인 코테시에도 유용

#### locals
- 로컬 심볼 테이블 딕셔너리 가져오는 메소드
- 클래스 메소드 내부 모든 로컬 변수 출력 -> 디버깅에 많은 도움

## 9. Stack, Queue
- Stack : LIFO (Last-In-First-Out)
- Queue : FIFO (First-In-First-Out)
- 파이썬에서 스택과 큐 자료형을 별도로 제공하진 않지만, 사실상 리스트가 모든 연산을 지원함
- 다만 리스트는 동적 배열로 구현되어 있어 큐의 연산을 수행하기에는 효율적이지 않기 때문에, 큐를 위해서는 Deque란느 별도의 자료형을 사용해야 좋은 성능을 낼 수 있음
- 굳이 성능을 고려하지 않는다면 사실상 리스트를 잘 사용하기만 해도 충분

### Linked List를 이용한 스택 ADT(Abstract Data Type) 구현
```python
# 연결리스트 노드 정의
class Node:
  def __init__(self, item, next):
    self.item = item
    self.next = next
    
class Stack:
  def __init__(self):
    self.last = None
  
  def push(self, item):
    self.last = Node(item, self.last)
   
  def pop(self):
    item = self.last.item
    self.last = self.last.next
    return item
```

### 20) Valid Parentheses
- Easy

#### 의식의 흐름
- stack (list)
- open bracket 입력 -> push
- close bracket 입력 -> pop 후 같은 종류 open bracket인지 확인
- dictionary 이용해서 같은 종류끼리 묶어주기

#### Solution
처음 작성한 코드
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_dic = {')':'(', ']':'[', '}':'{'}
        for bracket in s:
            if bracket in bracket_dic.values():
                stack.append(bracket)
            else:
                if stack.pop() == bracket_dic[bracket]: continue
                else: return False
```
- '[', ']' 케이스 통과X

예외처리 추가해준 코드
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_dic = {')':'(', ']':'[', '}':'{'}
        for bracket in s:
            if bracket in bracket_dic.values():
                stack.append(bracket)
            else:
                if len(stack) == 0 : return False
                else:
                    if stack.pop() == bracket_dic[bracket]: continue
                    else: return False

        if len(stack) == 0 : return True
        else: return False
```

참고 솔루션
```python
class Solution(object):
    def isValid(self, s):
        opcl = dict(('()', '[]', '{}'))
        stack = []
        
        for idx in s:
            if idx in '([{':
                stack.append(idx)
            elif len(stack) == 0 or idx != opcl[stack.pop()]:
                return False
        # At last, we check if the stack is empty or not...
        # If the stack is empty it means every opened parenthesis is being closed and we can return true, otherwise we return false...
        return len(stack) == 0
```
- 같은 알고리즘이지만 예외처리를 한줄로 좀 더 깔끔하게 해줬다.


## 10. 데크, 우선순위 큐
- 데크 (Deque)
  - 스택과 큐의 연산을 모두 갖고 있는 복합 자료형
  - Double-Ended Queue의 줄임말
  - 양쪽 끝을 모두 추출할 수 있는, 큐를 일반화한 형태의 추상 자료형(ADT).
  - 구현은 배열이나 연결 리스트 모두 가능하지만, 특별히 이중 연결 리스트로 구현하는 편이 가장 잘 어울림
    - 이중 연결리스트로 구현하게 되면, head와 tail이라는 이름의 투 포인트를 가지게 됨
    - 새로운 아이템이 추가될 때마다 앞쪽 또는 뒤쪽으로 연결시켜주기
    - 연결 후에는 포인터 이동
  - collections 모듈에서 deque라는 이름으로 지원
    - collections.deque는 이중 연결 리스트로 구현되어 있음.

#### What I learned

# 느낀점
- 그동안 여러가지 핑계로 너무 쉬어버렸다..! 나약한 자신
