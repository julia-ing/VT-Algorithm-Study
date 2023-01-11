### **Week 2**
|                                  #                                   |             TITLE              |        TAGS         |              DIFFICULTY               |
|:--------------------------------------------------------------------:|:------------------------------:|:-------------------:|:-------------------------------------:|
| [417](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Pacific Atlantic Water Flow |        Graph        | <span style="color:orange">Medium</span> |
| [73](https://leetcode.com/problems/set-matrix-zeroes/)                | Set Matrix Zeroes                | Matrix              | <span style="color:orange">Medium</span> |

### 417. Pacific Atlantic Water Flow
#### 문제풀이
- graph search를 쓰기 위해 아래같이 root는 각 ocean에 인접한 node들로 설정을 해준다.
```
#nodes adjacent to ocean
pacific  = [[0, i] for i in range(n)]   + [[i, 0] for i in range(1,m)]
atlantic = [[m-1, i] for i in range(n)] + [[i, n-1] for i in range(m-1)]
```
- 그리고 bfs를 써주는데 일반 bfs와 같이 visited list를 따로 저장해주지 않았다. 그 이유는 예를 들어 [2,2]로 인해 오른쪽에 있는 [2,3]으로는 물이 흘러가지 않을 수도 있지만 [2,4]에서 반대 방향으로 [2,3]을 갈 수도 있기 때문에 visited을 써서 안되겠다는 생각이 들었다.
- 또한 기본적으로 오른쪽 위, 왼쪽 아래 모서리는 입력과 상관 없이 두 바다 모두로 흘러갈 수 있기 때문에 처음에 기본적으로 초기화를 해줬다. 

```
def bfs(ocean_nodes): 
            queue=ocean_nodes
            reached_ocean=list(ocean_nodes)
            reached_ocean.extend([item] for item in [[0,n-1],[m-1,0]] if item not in reached_ocean)

            while queue:          
                node = queue.pop(0) 
                x, y = node[0], node[1]

                for dx, dy in [(x, y+1), (x, y-1), (x-1, y), (x+1, y)]:
                    if 0<=dx and dx<m and 0<=dy and dy<n and heights[dx][dy]>=heights[x][y]:
                        if [dx,dy] not in reached_ocean:
                            reached_ocean.append([dx,dy])
                            queue.append([dx,dy])
            return reached_ocean
```
- 마지막으로 두 리스트 간의 intersection을 반환한다!
```
return [inner for inner in reached_atlantic if inner in reached_pacific]
```
#### 💡 What I learned!
![image](https://user-images.githubusercontent.com/63735383/211860967-1a8e711e-7fca-42a3-8a27-441388f2dd23.png)

문제를 풀어나가는 데 있어서 runtime error가 난 적이 있다. root들을 shallow copy해주는데 로컬에서는 잘 돌아갔지만 leetcode에서는 runtime error를 뱉어냈는데 일부 버전에서는 지원이 안된다고 한다. 이때 list(my_list)로 감싸주거나 my_list[:] 이런 식으로 불러와주면 어디든 적용할 수 있다.

-------------------------------------------------------------------
### 73. Set Matrix Zeroes
#### 문제풀이
첫 접근:
처음에는 모든 array 자리에 0이 들어가야하는지 말아야하는지 brute force방법을 생각했다. 이 경우 간편하게 구현할 수는 있겠지만 O(mn)의 space를 차지하게 될 것이다.

두번째 접근:
row와 col 각각의 index에 0이 있는지를 체크하는 list를 각각 만들어주자! -> O(m+n) space

마지막 접근:
이렇게 되면 array 속에서 0인 position에 대해서만 row와 col index를 기록해주자. 이렇게 되면 m이나 n의 space를 모두 차지하지 않고서 O(#0의 개수)의 space를 차지하게 된다.

이때 궁금했던 점은 if문을 실행시켜줘서 그 0의 index가 list에 이미 넣어져있는지 판단 후 append 해주는 게 좋을까 아니면 if문 판단 없이 일단 넣고 보는 게 좋을까?

#### 💡 What I learned!
```
# trial 1 runtime beats 62%     
        for i in range(m):
            for j in range(n):
                if i in row_list or j in col_list:
                    matrix[i][j]=0
                    
# trial 2 runtime beats 96%
        for idx in row_list:
            for j in range(n):
                matrix[idx][j]=0
        
        for idx in col_list:
            for i in range(m):
                matrix[i][idx]=0
```
1. 0으로 값을 바꿔줘야하는 row, column index를 갖고 있을 때, 모든 자리를 돌면서 그 position의 index들이 조건에 맞을 때 값을 써주는 방법
2. row list에 있는 애들을 쭉 바꿔준 다음에 col list에 있는 애들을 바꿔주는 방법 -> 이 경우 row랑 col의 intersection에 해당하는 값을 두번이나 반복하여 덮어씌워준다.

를 시도해봤는데 두번째가 time이 훨씬 잘 나왔다!
