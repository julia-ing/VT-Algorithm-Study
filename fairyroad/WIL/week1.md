⚡<b>1번_Array</b>

    [Bruteforce]
    나는 Bruteforce 방법으로 풀었는데 O(n^2)으로 복잡도는 매우 안좋음
![1_array](https://user-images.githubusercontent.com/74306759/210808120-a35b667a-f3df-4536-aa9a-a2b7d20a71be.PNG)


⚡<b>300번_LIS</b>

    LIS = Longest Incrasing Subsequence
    Strictly 라는 표현이 있으면 같은 건 안된다고 함!
    DP중에서 특별한 케이스
    10, 20, 40, 25, 20, 50, 30, 70, 85가 있으면 10, 20, 40, 50, 70, 85 이렇게 숫자를 고르면서 subsequence의 길이가 최대가 되도록 선택!
    아래 공식을 이용해서 최종 DP 테이블에서 가장 원소가 큰 값이 가장 긴 증가하는 부분 수열의 길이가 되는 것
    그렇게 나온 dp list중에서 max값이 longest increasing subsequence가 됨
    python에서는 bisect라는 binary search library를 이용해서 자리를 끼워맞추는 방식도 있음

![image](https://user-images.githubusercontent.com/74306759/210807957-2bba2505-0b2e-4397-9623-e53d34120398.png)
![image](https://user-images.githubusercontent.com/74306759/210809972-c7ba21c1-fbec-478a-90a5-d52138a900d2.png)
