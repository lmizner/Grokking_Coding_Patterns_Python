class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


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



############################################################ 



def swap_pairs(head):

    # Verify at least 2 nodes exist
    if not head or not head.next:
        return head

    # Initialize dummy node and pointers
    prev = LinkedListNode(0)  # Dummy node to handle the head
    prev.next = head
    current = head
    new_head = current.next

    # Traverse LinkedList
    while current and current.next:
        
        # Obtain the two nodes that need to be swapped
        first = current
        second = current.next

        # Swap the nodes
        first.next = second.next
        second.next = first

        # Link previous node to second node
        prev.next = second

        # Iterate ahead to the next pair of nodes
        prev = first
        current = first.next

    # Replace this placeholder return statement with your code
    return new_head



# Time Complexity = O(n)
# Space Complexity = O(1)



############################################################



# Driver Cod
def main():
    test_cases = [
        [10, 1, 2, 3, 4, 5],
        [28, 21, 14, 7],
        [11, 12, 13, 14, 15],
        [1, 2]
    ]

    for idx, test_case in enumerate(test_cases):
        print(f"Test case {idx + 1}: {test_case}")
        
        # Creating a linked list
        linked_list = LinkedList()
        linked_list.create_linked_list(test_case)

        # Printing the original linked list
        print("Original list: ", end="")
        print_list_with_forward_arrow(linked_list.head)
        print()  # To add a newline for clarity

        # Swapping pairs
        swapped_head = swap_pairs(linked_list.head)

        # Printing the swapped linked list
        print("Swapped list: ", end="")
        print_list_with_forward_arrow(swapped_head)
        print("\n")  # To separate test cases


if __name__ == '__main__':
    main()
