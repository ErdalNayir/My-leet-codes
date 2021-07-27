class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1=ListNode(1)
second_1=ListNode(2)
third_1=ListNode(3)

l1.next=second_1
second_1.next=third_1



l2=ListNode(2)
second_2=ListNode(5)
third_2=ListNode(3)

l2.next=second_2
second_2.next=third_2



new_node = ListNode(0)
result_node = new_node

while True:

    if not l2:  #eğer l2 none ise resulnode l1 i işaret etsin
        result_node.next = l1
        break
    if not l1:
        result_node.next = l2  #tam tersi
        break

    if l1.val > l2.val: # l1 şuanki değer büyük l2 ş.d.
        result_node.next = ListNode(l2.val)  #result pointer l2 oldu
        l2 = l2.next  #l2 nin eski değeri silindi
    else:
        result_node.next = ListNode(l1.val) #tam tersi
        l1 = l1.next  # şuanki değer none oldu

    result_node = result_node.next










head = ListNode()
        curr = head

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            elif l2.val <= l1.val:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return head.next
