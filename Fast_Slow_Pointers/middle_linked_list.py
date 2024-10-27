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





def get_middle_node(head):
  
  # Initialize slow and fast pointers
  slow_pointer = head
  fast_pointer = head
  
  # Traverse the linked list via pointers
  while fast_pointer != None and fast_pointer.next != None:
    slow_pointer = slow_pointer.next
    fast_pointer = fast_pointer.next.next
  
  return slow_pointer





# Driver code
def main():

    input = (
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6],
        [3, 2, 1],
        [10],
        [1, 2],
    )

    for i in range(len(input)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        print(i+1, ".\tLinked list: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tMiddle of the linked list: ",
              get_middle_node(input_linked_list.head).data)
        print("-"*100, "\n")

if __name__ == "__main__":
    main()

