# VT-Algorithm-Study

## 📚 Directory / FileName Rule

기본 구조는 다음과 같음, **본인 디렉토리만 건드릴 것**

```cpp
|— julia-ing
|    |— WIL
|          |— week1.md
|          |— week2.md
|    |— LeetCode
|          |— 문제번호_문제이름_알고리즘.py  
|              예시: 123_문제_DFS.py
|    |— Programmers 
|    |— …
|—github id
…
|— README.md (컨벤션 정리)
```
*스터디 커리큘럼 외에 본인이 풀고 싶은 문제를 자유롭게 풀어서 올려도 됩니다*


## 🦄 Commit Rule

- repository fork하여 자신의 깃에서 clone (본인의 깃에서 작업하고 커밋합니다.)
- root 에 각자 깃아이디 명으로 폴더 만들기, 본인 폴더 안에는 위에 그린 구조처럼 진행
- 커밋 메세지는 자유롭게 작성해주시면 됩니다. 나중에 본인이 찾아보기 편한 메시지로 해주세요.
    - 예) `week2: 투포인터, BFS` , `카카오 2021 기출` , `프로그래머스 123번` ..

## 🍋 PR Rule

- **julia-ing:master ← 본인깃헙id:master** 로 PR 
- PR 메시지
    - [이름] week1 `[최예원] week5`

## 🔥 Study Rule

- 예원(0) → 민주(1) → 수민(2) → 유리(3) → 지호(4) → 효서(5) → 준형(6) → 유정 (7) → 태현(8)
    - 돌아가면서 총무를 맡습니다.
- 미팅 시간: 금요일 오전 11시
1. 미팅 하루 전 자정까지
    - 커리큘럼 문제 풀고 PR 날리기
    - 만약 다 못풀었더라도 일부라도 시간 지켜서 pr 올려주세요 (단 전부 못풀었으면 pr x)
2. 미팅 전까지
    - 사이클에 맞추어 해당 사람 코드 리뷰
        - 코드리뷰를 받은 후 부족한 부분 채워넣는 건 마감시간은 없고 자유롭게 하면 됩니다
    - 주차별 코드리뷰 대상
        - 1번 문제: **(자신의 번호 + 해당 주차) % 인원수**
        - 2번 문제: **(자신의 번호 + 해당 주차 + 1) % 인원수**
        - 예) `1주차-예원-1번문제 : (예원(0) + 1) % 9 = 1 : 1번 사람 코드 PR`
            
            `1주차-예원-2번문제 : (예원(0) + 1 + 1) % 9 = 2 : 2번 사람 코드 PR`
    - pr merge
    - 총무가 벌금 정산
4. 미팅
    - 각자 공부는 되어있다는 가정하에 돌아가면서 “설명하기” 를 연습
    - 되도록 참여를 권장, 설명할 차례인 사람은 필수, 미팅 참여에 대한 벌금은 없음
    
### 💸 벌금 규칙

```
1. PR 을 미팅 하루 전까지 제출했는지?
   - 풀지 못한 문제 당 500원
   - ex) 1문제만 풀고 PR 올림 : (그 주에 풀기로 한 문제 개수 - 1)*500
2. 코드리뷰를 제 시간에 못했는지?
   - 500원
3. 시험기간 / 중요한 행사 -> 합의..
```

## 🧸 커리큘럼

- 1차 스터디: https://leetcode.com/problemset/all/

### **Week 1**
|                                  #                                   |             TITLE              |        TAGS         |                DIFFICULTY                |
|:--------------------------------------------------------------------:|:------------------------------:|:-------------------:|:----------------------------------------:|
|             [1](https://leetcode.com/problems/two-sum/)              |            Two Sum             |        Array        |  <span style="color:green">Easy</span>   |
| [300](https://leetcode.com/problems/longest-increasing-subsequence/) | Longest Increasing Subsequence | Dynamic Programming | <span style="color:orange">Medium</span> |

### **Week 2**
|                                  #                                   |             TITLE              |        TAGS         |              DIFFICULTY               |
|:--------------------------------------------------------------------:|:------------------------------:|:-------------------:|:-------------------------------------:|
| [417](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Pacific Atlantic Water Flow |        Graph        | <span style="color:orange">Medium</span> |
| [73](https://leetcode.com/problems/set-matrix-zeroes/)                | Set Matrix Zeroes                | Matrix              | <span style="color:orange">Medium</span> |

### **Week 3**
|                                  #                                   |        TITLE         |        TAGS         |              DIFFICULTY               |
|:--------------------------------------------------------------------:|:--------------------:|:-------------------:|:-------------------------------------:|
| [23](https://leetcode.com/problems/merge-k-sorted-lists/) | Merge k Sorted Lists | Heap                |  <span style="color:red">Hard</span>  |
|      [226](https://leetcode.com/problems/invert-binary-tree/)      |  Invert Binary Tree  |   Tree   | <span style="color:green">Easy</span> |

### **Week 4**
|                                  #                                   |        TITLE         |        TAGS         |              DIFFICULTY               |
|:--------------------------------------------------------------------:|:--------------------:|:-------------------:|:-------------------------------------:|
| [3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Longest Substring Without Repeating Characters |       String        | <span style="color:orange">Medium</span> |
|         [139](https://leetcode.com/problems/word-break/)          |         Word Break          | Dynamic Programming | <span style="color:orange">Medium</span> |

### **Week 5**
|                                  #                                   |            TITLE             |        TAGS         |              DIFFICULTY               |
|:--------------------------------------------------------------------:|:----------------------------:|:-------------------:|:-------------------------------------:|
|      [200](https://leetcode.com/problems/number-of-islands/)      |      Number of Islands       |        Graph        | <span style="color:orange">Medium</span> |
| [124](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Binary Tree Maximum Path Sum |   Tree   |  <span style="color:red">Hard</span>  |

### **Week 6**
|                                  #                                   |            TITLE             |        TAGS         |                DIFFICULTY                |
|:--------------------------------------------------------------------:|:----------------------------:|:-------------------:|:----------------------------------------:|
| [5](https://leetcode.com/problems/longest-palindromic-substring/)                               | Longest Palindromic Substring                             | String   | <span style="color:orange">Medium</span> |
| [347](https://leetcode.com/problems/top-k-frequent-elements/)                    | Top K Frequent Elements                    | Heap     |   <span style="color:red">Hard</span>    |

### **Week 7**
|                                  #                                   |            TITLE             |        TAGS         |             DIFFICULTY              |
|:--------------------------------------------------------------------:|:----------------------------:|:-------------------:|:-----------------------------------:|
| [230](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Kth Smallest Element in a BST | Tree     |                  <span style="color:orange">Medium</span>                  |
| [198](https://leetcode.com/problems/house-robber/)                    | House Robber                     | Dynamic Programming | <span style="color:orange">Medium</span> |

### **Week 8**
|                                  #                                   |            TITLE             |        TAGS         |                DIFFICULTY                |
|:--------------------------------------------------------------------:|:----------------------------:|:-------------------:|:----------------------------------------:|
| [128](https://leetcode.com/problems/longest-consecutive-sequence/)    | Longest Consecutive Sequence     | Graph               | <span style="color:orange">Medium</span> |
| [295](https://leetcode.com/problems/find-median-from-data-stream/)               | Find Median from Data Stream               | Heap     | <span style="color:red">Hard</span>   |

### **Week 9**
|                                  #                                   |            TITLE             |        TAGS         |                DIFFICULTY                |
|:--------------------------------------------------------------------:|:----------------------------:|:-------------------:|:----------------------------------------:|
| [212](https://leetcode.com/problems/word-search-ii/)      | Word Search II       | Tree                | <span style="color:red">Hard</span>   |
|       [46](https://leetcode.com/problems/group-anagrams/)       |      Group Anagrams       |   String    | <span style="color:orange">Medium</span> |
