✔number2

     recursive하게 구현하려고 함 (left, self, right) -> inorder
     cnt를 어떻게 올릴지 고민하다가 복잡할 것 같아서 그냥 list에 append하는 방식을 생각함
     근데 어떻게 구현해야할 지 감이 안와서 그냥 정답을 봤음
     완전 신박함.. 어차피 BST이므로 크기는 left, self, right순으로 크게 되니까 왼쪽부터 k-1 index에 있는 값이 내가 찾는 k번째의 값이 됨!
     class Solution:
        def inorders(r):
            return inorders(r.left) + [r.val] + inorders(r.right) if r else []
        def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
            return inorders(root)[k-1]

✔number2

    House Rober는 dp문제였는데, 기존 문제와는 다르게 바로 왼쪽에 있는것이 아니라 i-2, i-3을 가져와야 한다는 특징이었다.
    그냥 dp기본문제 풀듯이 풀면 쉽게 풀렸다.
    딱히 설명할 말은 없음..
    2개이하와 index가 3, 그리고 index가 3보다 클때 조금 달라질 수 있어서 그 부분만 나눠서 풀었다.
    - 2개 이하는 바로 max를 return하면 되고
    - index == 3이면 그냥 0번을 가져오면 됨
    - 나머지는 현재와 i-2, i-3중에 max를 가져오면 됨!
   
 ![image](https://user-images.githubusercontent.com/74306759/219309550-e86ba013-3a42-422a-9b2b-9a4e9a84a99b.png)
