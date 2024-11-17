class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None
    
    # insert_node_at_head method will insert a LinkedListNode at 
    # head of a linked list.
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
    

def print_list_with_forward_arrow(linked_list_node):
    temp = linked_list_node
    while temp:
        print(temp.data, end=" ")  # print node value
        
        temp = temp.next
        if temp:
            print("→", end=" ")
        else:
            # if this is the last node, print null at the end
            print("→ null", end=" ")



############################################################



def reorder_list(head):
    
    # Check that head exists
    if not head:
        return head
    
    # First find the middle node via fast/slow pointer method
    # Initialize fast and slow pointers
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Slow pointer will be located at the middle of the linked list (i.e head of reverse section)
    # Initialize pointers for reversing LinkedList
    current = slow
    prev, next = None, None

    # Reverse until we reach end of LinkedList
    while current is not None:
        current.next, prev, current = prev, current, current.next  

    # Merge the two halves of the list together (i.e folding them)
    # Initialize pointers for merging
    first = head
    second = prev

    # Interleave the two LinkedLists
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next

    return head



# def reorder_list(head):
#     if not head:
#         return head
#     slow = fast = head
    
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next 
#     prev, curr = None, slow

#     while curr:
#         curr.next, prev, curr = prev, curr, curr.next     
#     first, second = head, prev

#     while second.next:
#         first.next, first = second, first.next
#         second.next, second = first, second.next
    
#     return head



# Time Complexity = O(n)
# Space Complexity = O(1)



############################################################



# Driver Code
def main():
    input_list = [
        [1, 1, 2, 2, 3, -1, 10, 12],
        [10, 20, -22, 21, -12],
        [1, 1, 1],
        [-2, -5, -6, 0, -1, -4],
        [3, 1, 5, 7, -4, -2, -1, -6]
    ]

    for i, inp in enumerate(input_list):
        obj = LinkedList()
        obj.create_linked_list(inp)

        print(i + 1, ".\tOriginal list: ", end="", sep="")
        print_list_with_forward_arrow(obj.head)

        obj.head = reorder_list(obj.head)

        print("\n\tAfter folding: ", end="")
        print_list_with_forward_arrow(obj.head)
        if i != len(input_list) - 1:
            print("\n", "-"*100, sep="")


if __name__ == '__main__':
    main()

