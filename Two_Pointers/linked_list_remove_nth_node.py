# Template for linked list node class
class LinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Template for the linked list
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to insert a node at the head of the linked list
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
        self.head = node

    # Method to create a linked list from a list of values
    def create_linked_list(self, values):
        for value in reversed(values):
            self.insert_node_at_head(LinkedListNode(value))





def remove_nth_last_node(head, n):
    right = head
    left = head
    
    # Move the right pointer forward n steps
    for i in range(n):
        right = right.next
    
    # If right is None after moving n steps, we need to remove the head (i.e. n exceeds length of linked list)
    if right is None:
        return head.next  # Removing the head
    
    # Move both pointers forward until right reaches the end
    while right.next is not None:
        right = right.next
        left = left.next
    
    # Remove the Nth node from the end
    left.next = left.next.next

    return head





# Function to print the linked list
def print_list_with_forward_arrow(head):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "")
        current = current.next
    print()

# Driver code
def main():
    lists = [
        [23, 89, 10, 5, 67, 39, 70, 28],
        [34, 53, 6, 95, 38, 28, 17, 63, 16, 76],
        [288, 224, 275, 390, 4, 383, 330, 60, 193],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [69, 8, 49, 106, 116, 112, 104, 129, 39, 14, 27, 12]
    ]
    n = [4, 1, 6, 9, 11]

    for i in range(len(n)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(lists[i])
        print(i + 1, ". Linked List:\t", end='')
        print_list_with_forward_arrow(input_linked_list.head)
        print("n = ", n[i])
        result = remove_nth_last_node(input_linked_list.head, n[i])
        print("Updated Linked List:\t", end='')
        print_list_with_forward_arrow(result)
        print("-" * 100)

if __name__ == '__main__':
    main()
