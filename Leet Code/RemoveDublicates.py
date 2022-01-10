class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode temp=head;
        while(temp!=null && temp.next!=null){
            while(temp.val==temp.next.val){
                temp.next=temp.next.next;
                
                 if (temp.next == null){
                break;
                }
                
            }
           
					
            temp=temp.next;
        }
        return head;
    }
}
