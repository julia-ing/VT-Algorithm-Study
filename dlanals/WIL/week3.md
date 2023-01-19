# 23. Merge k Sorted Lists
- hard

## 의식의 흐름
- 각 연결리스트에서 current (작은것부터)
- min끼리 비교해서 작은 것부터 result 삽입
- 근데 일단 다 집어놓고 list.sort() 하면 안되나?
  - 일단 시도해보자
  - 연결리스트 속성이 헷갈려서 순회하는것 부터 문제가 생김
- solution 참고

## 관련 개념
- 분할정복(Divide and Conquer)
  - 여러 알고리즘의 기본이 되는 해결방법
  - 엄청나게 크고 방대한 문제를 조금씩 조금씩 나눠가면서 용이하게 풀 수 있는 문제 단위로 나눈 다음 그것들을 다시 합쳐서 해결하자는 개념.
  - 대표적으로는 퀵소트나 병합정렬. 
  - 과정
    - 분할: 문제를 더이상 분할할 수 없을 때까지 동일한 유형의 여러 하위 문제로 나눈다.
    - 정복: 가장 작은 단위의 하위 문제를 해결하여 정복한다.
    - 조합: 하위 문제에 대한 결과를 원래 문제에 대한 결과로 조합한다.

- 우선순위 큐
  - 우선순위의 개념을 큐에 도입한 자료 구조
  - 임의의 기준을 중심으로 가장 높은 우선순위를 가지는 항목의 삭제 및 반환과 임의의 우선순위를 가지는 항목 삽입을 지원하는 자료구조
  - 스택, 큐도 일종의 우선순위 큐
  - 이용사례
    - 시뮬레이션 시스템
    - 네트워크 트래픽 제어
    - 운영 체제에서의 작업 스케쥴링
    - 수치 해석적인 계산
  - 우선순위 큐는 배열, 연결리스트, 힙 으로 구현이 가능한데, 이 중에서 힙(heap)으로 구현하는 것이 가장 효율적.
  - 우선순위 큐의 구현과 enque, dequeue 연산의 시간복잡도 비교
    - ![IMG_3573](https://user-images.githubusercontent.com/97150219/213466649-e6f57bc2-8e2d-416e-a941-cd4cfeb2c34a.jpg)
  - 힙을 이용한 우선순위 큐 구현의 movitation
    - 우선순위 큐는 현재 우선순위가 가장 높은 항목을 하나씩 삭제 및 반환하는 목적으로 사용
    - 현재 우선순위가 갖아 높은 항목을 하나씩 삭제 및 반환할 경우 모든 항목을 정렬시킬 필요가 없음
    
 - 힙
   - 완전 이진 트리로서 부모 노드 키 값의 우선순위가 자식 노드 키 값의 우선순위보다 높은 자료구조
   - 종류 : Max, Min heap

   - 트리 구현 종류
     - 배열(python list)
       - 메모리 낭비 많을 수 있음
       - 부모 노드와 자식 노드 index 알 수 있음
       - but 완전이진트리일 때는 낭비 x
     - 노드 연결

## Solution
### divide and conquer solution
```python
class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)
    
    def merge(self, l, r):
        dummy = p = ListNode()
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return dummy.next
    
    def merge1(self, l, r):
        if not l or not r:
            return l or r
        if l.val< r.val:
            l.next = self.merge(l.next, r)
            return l
        r.next = self.merge(l, r.next)
        return r
```
