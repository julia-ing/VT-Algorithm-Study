#417	Pacific Atlantic Water Flow	Graph	Medium
- 그래프로 탐색하는 DFS로 왼쪽과 위에서부터 체크하는 p와 오른쪽과 아래부터 체크하는 a를 시작점을 다르게 하여 dfs로 탐색한 후 교집합을 구한다.
- TC : O(2nm)

#73	Set Matrix Zeroes	Matrix	Medium
https://leetcode.com/problems/set-matrix-zeroes/
- 배열을 새로 만들지 않고 기존 배열을 사용해 SC O(N+M)으로 만들 수 있다.
- 첫 번째 row와 column의 값을 사용하여  O(1)으로 해결하는 솔루션도 있다.
* 참고링크 : https://leetcode.com/problems/set-matrix-zeroes/solutions/657430/python-solution-w-approach-explanation-readable-with-space-progression-from-o-m-n-o-1/