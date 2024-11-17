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



def reverse_between(head, left, right):

    # Verify that a head node is specified and that left and right are not the same
    if not head or left == right:
        return head

    # Initialize a dummy node and pointers
    dummy = LinkedListNode(0)
    dummy.next = head
    prev = dummy

    # Traverse LinkedList until prev reaches node before left node
    for _ in range(left - 1):
        prev = prev.next

    # Initialize current pointer
    current = prev.next

    # Traverse 
    for _ in range(right - left):
        next_node = current.next
        current.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node

    # Return dummy.next (i.e. modified head)
    return dummy.next



# Time Complexity = O(n)
# Space Complexity = O(1)



############################################################



# Driver Code
def main():
    input_list = [
        [1, 2, 3, 4, 5, 6, 7],
        [6, 9, 3, 10, 7, 4, 6],
        [6, 9, 3, 4],
        [6, 2, 3, 6, 9],
        [6, 2]
    ]
    left = [1, 3, 2, 1, 1]
    right = [5, 6, 4, 3, 2]

    for i in range(len(input_list)):

        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input_list[i])

        print(i + 1, ".\tOriginal linked list: ", end="", sep="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tleft:", left[i], ", right:", right[i])

        if left[i] <= 0:
            print("\n\tThe expected 'left' and 'right' to have \
            value from 1 to length of the linked list only.")
        else:
            result = reverse_between(input_linked_list.head, left[i], right[i])
            print("\n\tReversed linked list: ", end="")
            print_list_with_forward_arrow(result)
        print("\n", "-"*100, sep="")

if __name__ == '__main__':
    main()


