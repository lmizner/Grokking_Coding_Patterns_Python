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



def reverse_even_length_groups(head):

    # Initialize a pointer for prev node and variable for current group length
    prev = head
    group_len = 2

    # Iterate through the LinkedList
    while prev.next:

        # Initialize current node pointer and counter for current group
        node = prev
        num_nodes = 0

        # Traverse all nodes in current group
        for _ in range(group_len):

            # If we find the end of the LinkedList (i.e. None), stop
            if not node.next:
                break

            # Otherwise, update the count and move to the next node
            num_nodes += 1
            node = node.next

        # Check if odd length
        if num_nodes % 2:
            prev = node

        # Otherwise, reversal of even length group
        else:
            reverse = node.next
            current = prev.next
            
            # Reverse
            for _ in range(num_nodes):
                current_next = current.next
                current.next = reverse
                reverse = current
                current = current_next
            
            # Update prev pointer after reversal of even group
            prev_next = prev.next
            prev.next = node
            prev = prev_next

        # Increment group_len by 1 to move to next group
        group_len += 1

    return head



# Time Complexity = O(n)
# Space Complexity = O(1)



############################################################



# Driver Code
def to_list(head):
    lst = []
    temp = head
    while temp:
        lst.append(temp.data)
        temp = temp.next
    return lst


def main():
    input = [
        [1, 2, 3, 4],
        [10, 1, 2, 3, 4, 5],
        [28,21,14,7],
        [11,12,13,14,15],
        [1,2]
    ]

    for i in range(len(input)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        print(
            i+1, ".\tIf we reverse the even length groups of the linked list: ", end='\n\t', sep="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\n\tWe will get: ", end='\n\t')
        print_list_with_forward_arrow(
            reverse_even_length_groups(input_linked_list.head))
        print("\n", "-" * 100)


if __name__ == '__main__':
    main()



