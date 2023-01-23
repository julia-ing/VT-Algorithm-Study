/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
    ArrayList<ListNode> allList = new ArrayList<>();
    for (int i = 0; i < lists.length; i++) {
        while (lists[i] != null) {
            allList.add(lists[i]);
            lists[i] = lists[i].next;
        }
    }

    allList.sort(Comparator.comparingInt(o -> o.val));

    for (int i = 0; i < allList.size() - 1; i++) {
        allList.get(i).next = allList.get(i + 1);
    }

    if (allList.size() == 0){
        return null;
    }

    allList.get(allList.size() - 1).next = null;
        return allList.get(0);
    }
}
