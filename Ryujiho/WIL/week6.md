## Problem 1 (String)
- `s[::-1]` : 문자열 순서 뒤집기
- `s[::-1]`를 사용하는 것보다 panlindromic substring의 case가 2개인 점을 고려하여 직접 구현하는 방법이 훨씬 빠른 속도로 실행된다. 

---
## Problem 2 (Heap, dictionary)
#### My solution
- dictionary를 사용하여 (key=number, value=count)로 계산한 후, value값을 `sorted()`를 사용하여 정렬한 후 top K개의 값만 사용한다. 
- sorted()의 return 값이 tuple list이라서 first value만 k개 가져와야하므로 list comprehension으로 값을 얻는다. 

#### Other solution
- `from collections import defaultdict`
  - dict클래스의 서브클래스
  - `defaultdict(int)` 생성 시 인자로 주어진 객의 기본값을 딕셔너리 value의 초기값으로 세팅 가능하다.
    int -> 0 으로 초기화
  - dictionary 에 key가 있는지 체크하여 0으로 초기화해주는 것보다 `defaultdict`를 사용하면 바로 초기화가 되어 활용하기 좋을 것 같다.
