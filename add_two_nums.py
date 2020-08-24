class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_total = ""
        l2_total = ""
        ll = ListNode()
        
        while l1 is not None:
            l1_total += str(l1.val)
            
            l1 = l1.next
             
        l1_total = int(''.join(reversed(str(l1_total))))
        
        
        while l2 is not None:
            l2_total += str(l2.val)

            l2 = l2.next
        
        l2_total = int(''.join(reversed(str(l2_total))))
        

        ll_total = l1_total + l2_total
        
        ll_total = ''.join(reversed(str(ll_total)))
        
        counter = 0
        for i in ll_total:
            
            i = int(i)
            
            if counter == 0:
                if ll.val == 0:
                    ll.val = i
            else:
                start_node = ll
                while start_node.next is not None:
                    start_node = start_node.next
                
                start_node.next = ListNode(i)
            counter += 1
            
        return ll
        
