public class Solution3 {

	public ListNode removeElements(ListNode head, int val) {
		if (head == null)
			return null;
		head.next = removeElements(head.next, val);
		return head.val == val ? head.next : head;

	}

	public static void main(String[] args) {
		int[] nums = {1, 23, 4, 56, 6};
		ListNode head = new ListNode(nums);
		System.out.println(head);

		ListNode res = (new Solution2()).removeElements(head, 6);
		System.out.println(res);
	}
}
