class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Template for the linked list
class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None

    # insert_node_at_head method will insert a LinkedListNode at head
    # of a linked list.
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    # create_linked_list method will create the linked list using the
    # given integer array with the help of InsertAthead method.
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)
    
    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result


# Template for reversing a linked list
def reverse_linked_list(head):
	prev, curr = None, head
	while curr:
		nxt = curr.next
		curr.next = prev
		prev = curr
		curr = nxt
	return prev


def traverse_linked_list(head):
    current, nxt = head, None
    while current:
      nxt = current.next
      current = nxt


# Template for printing the linked list with forward arrows
def print_list_with_forward_arrow(linked_list_node):
    temp = linked_list_node
    while temp:
        print(temp.data, end=" ") #print node value
        
        temp = temp.next
        if temp:
            print("→", end=" ")
        else:
            print("→ null", end=" ") # if this is the last node, print null at the end



####################################################################



# Helper Function
def merge_2_lists(head1, head2):
    
    # Assign previous pointer to a dummy node
    dummy = LinkedListNode(-1)
    prev = dummy

    # Traverse over the list until both or one becomes null
    while head1 and head2:
        if head1.data <= head2.data:

            # if list1 value <= list2 value, add list1 value to list
            prev.next = head1
            head1 = head1.next

        else:

            # if list1 value > list2 value, add list2 value to list
            prev.next = head2
            head2 = head2.next
        
        prev = prev.next

    if head1 is not None:
        prev.next = head1
    else:
        prev.next = head2

    return dummy.next



def merge_k_lists(lists):

    if len(lists) > 0:
        step = 1
        
        while step < len(lists):

            for i in range(0, len(lists) - step, step * 2):
                lists[i].head = merge_2_lists(lists[i].head, lists[i + step].head)

            step *= 2
        
        return lists[0].head
    
    return



# Time Complexity = O(nlogk)
# Space Complexity = O(1)



####################################################################



# Driver code
def main():
    inputlists = [[[21, 23, 42], [1, 2, 4]],
        [[11, 41, 51], [21, 23, 42]],
        [[2], [1, 2, 4], [25, 56, 66, 72]],
        [[11, 41, 51], [2], [2], [2], [1, 2, 4]],
        [[10, 30], [15, 25], [1, 7], [3, 9], [100, 300], [115, 125], [10, 70], [30, 90]]
    ]
    inp_num = 1
    for i in inputlists:
        print(inp_num, ".\tInput lists:", sep = "")
        ll_lists = []
        for x in i:
            a = LinkedList()
            a.create_linked_list(x)
            ll_lists.append(a)
            print("\t", end = "")
            print_list_with_forward_arrow(a.head)
            print()
        inp_num += 1
        print("\tMerged list: \n\t", end = "")
        print_list_with_forward_arrow(merge_k_lists(ll_lists))
        print("\n", "-"*100, sep = "")


if __name__ == "__main__":
    main()
