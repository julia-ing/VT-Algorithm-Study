# 파이썬 알고리즘 인터뷰
## 1. 코딩 인터뷰
- 코딩 인터뷰를 위한 온라인 테스트 플랫폼
- 국내 기업의 코딩 테스트 플랫폼 활용 현황
- 온라인 코딩 테스트의 사전 준비사항
- 화이트보드 코딩 인터뷰

## 2. 프로그래밍 언어 선택
### 경진대회 통계로 알아본 언어 선호도
- c++ > python > java
- c++는 매우 효율적이며, 표준 라이브러리에 이미 많은 양의 자료구조와 알고리즘이 포함되어있음
- python 사용 -> 코드 라인 수가 압도적으로 짧음

### 프로그래밍 언어별 특징
#### 루프
- c++, java 문법 동일
- python -> one-liner 처리 가능 -> but 지나친 사용은 가독성을 떨어트릴 수 있음
#### generic programming
- generic : 파라미터의 타입이 나중에 지정 (to-be-specified-later)되게 해서 재활용성을 높일 수 있는 프로그래밍 스타일
- c++ : template 기능 통해 구현
- java
  - 1.5버전부터 추가
  - c++ 템플릿과 함께 객체 지향 프로그래밍(OOP, Object-Oriented Programming)을 추구하는 두 언어의 중요한 특징 중 하나로서 다양한 타입의 객체 재사용할 수 있음
- python
  - Dynamic Typing 언어이기 때문에 generic 필요 x
  - 동적 타이핑은 얼핏 사용하기엔 매우 편하지만 코드의 복잡도가 높아질수록 혼란 가중시킬 수 있음
  - 타입을 아예 명시하지 않으면 가독성을 낮추고 버그 발생 확률 높아질수도
  - 따라서 PEP(Python Enhancement Proposals)에 추가된 Type Hints 통해 generic 사용 가능
#### 배열 반복
- c++
  - 버전 11 이후 -> 모던 c++
  - 가장 큰 변화 중 하나는 : 연산자의 지원
  - c++도 사실상 파이썬과 큰 차이 없는 문법으로 배열 반복(Iterate through Array) 가능해짐
- java
  - 모던 c++과 유사
- python
  - 다른 언어와 다르게 문자열 자료형이라는 선언조차 필요x
  - 매우 간결
  - 코딩테스트 시 빠르게 문제 해결하는데 도움
  - but 지나친 간결함은 나중에 코드 복잡도가 높아졌을 때 가독성을 떨어뜨릴수도
#### 구조체
- C에서는 구조체(struct)는 특별한 의미가 있음
- 순차적으로 메모리를 할당하는 배열과 달리 구조체는 메모리의 어느 영역에나 어떤 크기로든 할당할 수 있는 사실상 유일한 복합 자료형이기 때문
- 연결리스틀 포함해 배열을 제외한 모든 추상 자료형의 구현은 사실상 구조체를 한 번 이상 이용한다고 할 수 있음
- 이 때 추상 자료형 : ADT, Abstract Data Type, 자료형의 연산을 정의한 것으로 실제 구현 방법은 명시하지 않음
- C++ 에서 클래스의 등장으로 이후 등장한 언어들에는 사용 빈도가 줄었음
- C++ 
  - 여전히 구조체 문법 지원, 클래스와 구조체가 공존
- Java
  - 더이상 지원 X
- Python
  - 구조체가 없음
  - 클래스 또한 데이터 타입을 지정할 수 없어, 구조체와 같은 형태를 정의하려면 Named Tuple 사용해야 함
  - 3.7부터는 dataclass 지원
#### 클래스
- C++
  - 클래스는 C++의 가장 큰 특징 중 하나
  - 구조는 요즘 언어들에 비해 복잡해 보이지만 크게 선언부와 구현부로 구분할 수 있음
  - 이를 통해 헤더 파일과 소스 파일로 각각 분리 가능
  - 선언과 구현을 분리하는 방식은 컴파일 속도를 높일 수 있음
- Java
  - 모든 것이 클래스
#### 코딩테스트에 최적인 언어
- 유연성
  - C++, Java는 대표적인 정적 타이핑 언어로 유연함과는 거리가 멀고, 매번 자료형을 엄격하게 선언해야 함
  - 대규모 프로젝트 시 유지 보수와 가독성을 높이지만, 알고리즘을 빠르게 구현해야 하는 코딩 테스트에서는 생산성을 상당히 저해


# 문제(Leetcode)
## 6. 문자열 조작
### 125) Valid Palindrome
- Easy

#### 의식의 흐름
- 먼저 문자열 처리 -> 공백, 기호 제거하고 소문자로 바꾸기
- 앞에서부터 시작하면서 비교해주기
- non-alphanumeric -> 숫자까지 포함한다는 건가?

#### What I leanred
- 문자열에서 문자, 숫자 제외하는 방법 -> s = ''.join(c for c in s if c.isalnum())

#### Solution
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())

        for idx in range(len(s)//2):
            if s[idx] != s[len(s)-1-idx]: return False
        
        return True
```

#### Solution - Deque
- Deque의 popleft -> O(1)
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
      # 자료형 Deque로 선언
      strs: Deque = collections.deque()
        
      for char in s:
        if char.isalnum():
          strs.append(char.lower())
          
      while len(strs) > 1:
        if strs.popleft() != strs.pop():
          return False
        
      return True
```

#### Solution - Slicing & Regular Expression
- [::-1] -> 문자열 뒤집기 -> 속도 개선
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
      s = s.lower()
      
      # 정규식으로 불필요한 문자 필터링
      s = re.sub('[^a-z0-9]', '', s)
      
      # 슬라이싱
      return s == s[::-1]
```


## 7. 배열
### 1) Two Sum
- Easy
- 쉬운 난이도에다 예전에 푼 문제지만 책에서 새로 알게된 풀이가 있어 정리해보았음

#### What I learned
- Two Pointer
  - 왼쪽 포인터와 오른쪽 포인터의 합이 타겟보다 크다면 오른쪽 포인터를 왼쪽으로, 작다면 왼쪽 포인터를 오른쪽으로 옮기면서 값을 조정하는 방식

#### Solution - Two Pointer
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while not left == right:
            # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
            if nums[left] + nums[right] < target:
                left += 1
            # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [left, right]
```
- Time Complexity : O(n)
- 하지만 이 방법은 잘못됐음 -> two pointer 방식을 사용하려면 정렬해줘야하는데, 기존 인덱스를 반환해야 하는 이 문제에서는 적용할 수 없음 

## 8. 연결 리스트
### 234) Palindrome Linked List
- Easy

#### 의식의 흐름
- 먼저 linked list -> list 해준 다음 확인해주기?

#### Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []

        while head != None:
            l.append(head.val)
            tmp = head
            head = head.next

        for idx in range(len(l)//2):
            if l[idx] != l[len(l) - 1 - idx]: return False
        
        return True
```
- linked list -> list 변환시 tmp변수는 필요없을 듯하다.
- 비교해줄 때 위 125) Valid Palindrome의 Deque 방식을 사용하면 속도를 개선할 수 있다.

#### Solution - Runner
- Runner
  - 연결리스트를 순회할 때 2개의 포인터를 동시에 사용한느 기법
  - 한 포인터가 다른 포인터보다 앞서게 하여 병합 지점이나 중간 위치, 길이 등을 판별할 때 유용하게 사용할 수 있음
  - 2개의 포인터는 각각 Fast Runner, Slow Runner라고 부르는데, 보통 Fast Runner(Pointer)는 두 칸씩 건너뛰고 Slow Runner(Pointer)는 한 칸씩 이동하게 함
  - 이 때 Fast Runner가 연결리스트의 끝에 도달하면, Slow Runner는 정확히 연결리스트의 중간 지점을 가리키게 됨
  - 이 같은 방식으로 중간 위치를 찾아내면, 여기서부터 값을 비교하거나 뒤집기를 시도하는 등 여러모로 활용 가능
  - 연결리스트에서 반드시 쓰이는 기법
- 투포인터 방식.. 아직 헷갈린다
```python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
      rev = None
      slow = fast = head
      
      # runner를 이용해 역순 연결 리스트 구성
      while fast and fast.next:
        fast = fast.next.next # 두 칸 이동
        rev, rev.next, slow = slow, rev, slow.next
      if fast: # 원소 개수가 홀수개일 때
        slow = slow.next
        
      # palindrome 여부 확인
      while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
      return not rev
```
