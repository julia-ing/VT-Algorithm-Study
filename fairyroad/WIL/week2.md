✔1번문제

    #First solution
    BFS문제인 것 같음!
    1. 현재 cells보다 neighboring cells가 작거나 같으면 표시하기
    2. path찾아서 return하기
    생각했어야 하는건 pacific, atlantic이 모두 true였어야 함! 그러니까 bfs를 2번썼어야 했음
    pacific에 닿아있는 곳부터 bfs를 시작해서 true로 marking하고, atlantic에 닿아있는 곳부터 bfs를 시작해서 true로 marking하면 됨!
    3. 둘다 true인걸 구현하기 위해서 pacific, atlantic이라는 graph를 만들었음
  
 ![image](https://user-images.githubusercontent.com/74306759/212039726-bfaf132b-3fab-4922-9e9c-4618fda01639.png)
  
    
    [BFS 복습]
    time complexity : O(N)
    queue는 insert할때 visited 처리 함!
    - 탐색 시작 노드 정보를 queue에 insert하고 visited 처리를 함
    - queue에서 노드를 꺼내서 visited되지 않은 인접한 노드의 정보를 모두 queue에 삽입하고 visited 처리를 함
    - 2번 과정을 더 이상 수행할 수 없을 때 까지 반복
    
    def bfs(graph, node, visited):
        queue = deque([node])
        visited[node] = True
        
        while queue:
            v = queue.popleft()
            for i in graph[v]:
                if not (visited[i]):
                    queue.append(i)
                    visited[i] = True
📝WIL

    - dx,dy 선언하는 것
    - dx = [1,-1.0,0], dy = [0,0,1,-1] 로 인접노드 이동을 표현할 수 있음
    - NxN graph만들때 [[for _ in range(sth[0])] for _ in range(sth)]으로 표현할 수 있음
    - x,y있는 건 append할 때 X.appemd([x,y]) 이렇게 하고 pop할 때 x,y = X.popleft()로 할 수 있음
    - 처음에 dequeue 선언을 X = dequeue()로 하는 것!

✔2번문제

    #First solution
    1. list_x, list_y를 선언해서 하나씩 보고 0인걸 append 시킴
    2. 0이 나왔던 자리의 entire row 와 column을 0으로 초기화 시킴
![image](https://user-images.githubusercontent.com/74306759/212015506-fdb27da2-c369-4962-bc08-7e3fa1e0e552.png)
