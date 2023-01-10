### **Week 2**
|                                  #                                   |             TITLE              |        TAGS         |              DIFFICULTY               |
|:--------------------------------------------------------------------:|:------------------------------:|:-------------------:|:-------------------------------------:|
| [417](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Pacific Atlantic Water Flow |        Graph        | <span style="color:orange">Medium</span> |
| [73](https://leetcode.com/problems/set-matrix-zeroes/)                | Set Matrix Zeroes                | Matrix              | <span style="color:orange">Medium</span> |

73. Set Matrix Zeroes
첫 접근:
row와 col에 해당하는 list를 각각 만들어주자! -> O(m+n) space

두번째 접근:
0인 position에 대해서만 row와 col index를 기록해주자.
궁금한 점은 if문을 실행시켜줘서 그 index가 list에 없을 때만 넣어주는 게 좋을까 아니면 일단 넣고 보는 게 좋을까?
