# Selection Sort

    가장 작은 데이터를 선택해서 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해서 앞에서 두번째 데이터와 바꿈
    time complexity : O(n^2)

# Insertion Sort

    특정한 데이터를 적절한 위치에 insert한다는 의미
    맨 앞에 (7이라고 할때, pivot을 가정) 는 그 자체로 정렬이 되어있다고 가정하고 5가 작으니까 왼쪽에 삽입이 되고
    그 다음 0이라고 할때 0은 5,7보다 훨씬 작으니까 맨 앞으로 insertion이 됨
    3은 0과 5의 사이에 들어가야 하니까 그 사이에 insertion이 됨
    time complexity : O(n^2)이지만 best일때가 O(n)이 된다는 장점이 있음
    일단 selection sort보다는 조금 더 똑똑한 방법인걸로...ㅎ

# Quick Sort

    merge sort는 quick sort와 비교할 정도로 빠른 알고리즘
    pivot이 사용이 되며, 큰 숫자와 작은 숫자를 교환할 때 교환하기 위한 기준을 pivot이라고 함
    part가 총 3개로 구성이 됨
    1. 첫번째 데이터를 pivot으로 정함
    2. 순서대로 5보다 큰 데이터를 선택하게 되는데 7이 선택되고 오른쪽부터 5보다 작은 데이터를 찾게되는데 찾으면 두 데이터의 위치를 바꾸게 됨
    3. 다시 pivot
