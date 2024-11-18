class LinkedListNode:
  # __init__ will be used to make a LinkedListNode type object
  def __init__(self, data, next=None):
    self.data = data
    self.next = next


class LinkedList:
    
    # __init__ will be used to make a LinkedList type object
    def __init__(self):
        self.head = None
    
    # insert_node_at_head method will insert a LinkedListNode at head of a linked list
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
    
    # create_linked_list method will create the linked list using the given 
    # integer array with the help of InsertAthead method
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)


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



def remove_duplicates(head):

    # Initialize pointer to traverse through LinkedList
    current = head

    while current and current.next:

        # Check if duplicate detected
        if current.data == current.next.data:
            current.next = current.next.next
        
        # No duplicate
        else:
            current = current.next

    # Return the head of the modified linked list (with duplicates removed)
    return head



# Time Complexity = O(n)
# Space Complexity = O(1)



############################################################


   
# Driver code
def main():
    input_list = [
        [1, 2, 2, 3, 3, 3],
        [-21, -21, -21, -21, -21, -21, -21],
        [3, 7, 9],
        [-100, -100, -100, -10, -10, 0, 10, 10, 100, 100, 100],
        [-77, -77, -7, -7, -7, -7, 7, 7, 7, 7, 77, 77, 77, 77]
    ]
    
    for i in range(len(input_list)):

        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input_list[i])

        print(i + 1, ".\tInput: ", end="", sep="")
        print_list_with_forward_arrow(input_linked_list.head)
        
        print("\n\n\tOutput: ", end="", sep="")
        print_list_with_forward_arrow(remove_duplicates(input_linked_list.head))
        
        print("\n", "-"*100, sep="")
        
if __name__ == '__main__':
    main()

