# VT-Algorithm-Study

## ๐ Directory / FileName Rule

๊ธฐ๋ณธ ๊ตฌ์กฐ๋ ๋ค์๊ณผ ๊ฐ์, **๋ณธ์ธ ๋๋ ํ ๋ฆฌ๋ง ๊ฑด๋๋ฆด ๊ฒ**

```cpp
|โ julia-ing
|    |โ WIL
|          |โ week1.md
|          |โ week2.md
|    |โ LeetCode
|          |โ ๋ฌธ์ ๋ฒํธ_๋ฌธ์ ์ด๋ฆ_์๊ณ ๋ฆฌ์ฆ.py  
|              ์์: 123_๋ฌธ์ _DFS.py
|    |โ Programmers 
|    |โ โฆ
|โgithub id
โฆ
|โ README.md (์ปจ๋ฒค์ ์ ๋ฆฌ)
```
*์คํฐ๋ ์ปค๋ฆฌํ๋ผ ์ธ์ ๋ณธ์ธ์ด ํ๊ณ  ์ถ์ ๋ฌธ์ ๋ฅผ ์์ ๋กญ๊ฒ ํ์ด์ ์ฌ๋ ค๋ ๋ฉ๋๋ค*


## ๐ฆ Commit Rule

- repository forkํ์ฌ ์์ ์ ๊น์์ clone (๋ณธ์ธ์ ๊น์์ ์์ํ๊ณ  ์ปค๋ฐํฉ๋๋ค.)
- root ์ ๊ฐ์ ๊น์์ด๋ ๋ช์ผ๋ก ํด๋ ๋ง๋ค๊ธฐ, ๋ณธ์ธ ํด๋ ์์๋ ์์ ๊ทธ๋ฆฐ ๊ตฌ์กฐ์ฒ๋ผ ์งํ
- ์ปค๋ฐ ๋ฉ์ธ์ง๋ ์์ ๋กญ๊ฒ ์์ฑํด์ฃผ์๋ฉด ๋ฉ๋๋ค. ๋์ค์ ๋ณธ์ธ์ด ์ฐพ์๋ณด๊ธฐ ํธํ ๋ฉ์์ง๋ก ํด์ฃผ์ธ์.
    - ์) `week2: ํฌํฌ์ธํฐ, BFS` , `์นด์นด์ค 2021 ๊ธฐ์ถ` , `ํ๋ก๊ทธ๋๋จธ์ค 123๋ฒ` ..

## ๐ PR Rule

- **julia-ing:main โ ๋ณธ์ธ๊นํid:main** ๋ก PR 
- PR ๋ฉ์์ง
    - [์ด๋ฆ] week1 `[์ต์์] week5`

## ๐ฅ Study Rule

- ์์(0) โ ๋ฏผ์ฃผ(1) โ ์๋ฏผ(2) โ ์ ๋ฆฌ(3) โ ์งํธ(4) โ ํจ์(5) โ ์คํ(6) โ ์ ์  (7) โ ํํ(8)
    - ๋์๊ฐ๋ฉด์ ์ด๋ฌด๋ฅผ ๋งก์ต๋๋ค.
- ๋ฏธํ ์๊ฐ: ๊ธ์์ผ ์ค์  11์
1. ๋ฏธํ ํ๋ฃจ ์  ์์ ๊น์ง
    - ์ปค๋ฆฌํ๋ผ ๋ฌธ์  ํ๊ณ  PR ๋ ๋ฆฌ๊ธฐ
    - ๋ง์ฝ ๋ค ๋ชปํ์๋๋ผ๋ ์ผ๋ถ๋ผ๋ ์๊ฐ ์ง์ผ์ pr ์ฌ๋ ค์ฃผ์ธ์ (๋จ ์ ๋ถ ๋ชปํ์์ผ๋ฉด pr x)
2. ๋ฏธํ ์ ๊น์ง
    - ์ฌ์ดํด์ ๋ง์ถ์ด ํด๋น ์ฌ๋ ์ฝ๋ ๋ฆฌ๋ทฐ
        - ์ฝ๋๋ฆฌ๋ทฐ๋ฅผ ๋ฐ์ ํ ๋ถ์กฑํ ๋ถ๋ถ ์ฑ์๋ฃ๋ ๊ฑด ๋ง๊ฐ์๊ฐ์ ์๊ณ  ์์ ๋กญ๊ฒ ํ๋ฉด ๋ฉ๋๋ค
    - ์ฃผ์ฐจ๋ณ ์ฝ๋๋ฆฌ๋ทฐ ๋์
        - 1๋ฒ ๋ฌธ์ : **(์์ ์ ๋ฒํธ + ํด๋น ์ฃผ์ฐจ) % ์ธ์์**
        - 2๋ฒ ๋ฌธ์ : **(์์ ์ ๋ฒํธ + ํด๋น ์ฃผ์ฐจ + 1) % ์ธ์์**
        - ์) `1์ฃผ์ฐจ-์์-1๋ฒ๋ฌธ์  : (์์(0) + 1) % 9 = 1 : 1๋ฒ ์ฌ๋ ์ฝ๋ PR`
            
            `1์ฃผ์ฐจ-์์-2๋ฒ๋ฌธ์  : (์์(0) + 1 + 1) % 9 = 2 : 2๋ฒ ์ฌ๋ ์ฝ๋ PR`
    - pr merge
    - ์ด๋ฌด๊ฐ ๋ฒ๊ธ ์ ์ฐ
4. ๋ฏธํ
    - ๊ฐ์ ๊ณต๋ถ๋ ๋์ด์๋ค๋ ๊ฐ์ ํ์ ๋์๊ฐ๋ฉด์ โ์ค๋ชํ๊ธฐโ ๋ฅผ ์ฐ์ต
    - ๋๋๋ก ์ฐธ์ฌ๋ฅผ ๊ถ์ฅ, ์ค๋ชํ  ์ฐจ๋ก์ธ ์ฌ๋์ ํ์, ๋ฏธํ ์ฐธ์ฌ์ ๋ํ ๋ฒ๊ธ์ ์์
    
### ๐ธ ๋ฒ๊ธ ๊ท์น

```
1. PR ์ ๋ฏธํ ํ๋ฃจ ์ ๊น์ง ์ ์ถํ๋์ง?
   - ํ์ง ๋ชปํ ๋ฌธ์  ๋น 500์
   - ex) 1๋ฌธ์ ๋ง ํ๊ณ  PR ์ฌ๋ฆผ : (๊ทธ ์ฃผ์ ํ๊ธฐ๋ก ํ ๋ฌธ์  ๊ฐ์ - 1)*500
2. ์ฝ๋๋ฆฌ๋ทฐ๋ฅผ ์  ์๊ฐ์ ๋ชปํ๋์ง?
   - 500์
3. ์ํ๊ธฐ๊ฐ / ์ค์ํ ํ์ฌ -> ํฉ์..
```

## ๐งธ ์ปค๋ฆฌํ๋ผ

- 1์ฐจ ์คํฐ๋: https://leetcode.com/problemset/all/

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
