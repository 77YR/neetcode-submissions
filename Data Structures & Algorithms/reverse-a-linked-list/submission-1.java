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
    public ListNode reverseList(ListNode head) {

        if (head == null)
            return head;
        Deque<Integer> stack = new ArrayDeque<>();

        ListNode curr = head;

        while (curr.next != null){
            stack.push(curr.val);
            curr = curr.next;
        }
        stack.push(curr.val);

        ListNode res = new ListNode(0);
        ListNode cur = res;
        while (!stack.isEmpty()){
            ListNode node = new ListNode(stack.pop());
            cur.next = node;
            cur = cur.next;
        }
        cur.next = null;

        return res.next;
        
    }
}
