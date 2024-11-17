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



def reverse_k_groups(head, k):
   
    # Initialize a dummy node at the start of the LinkedList
    dummy = LinkedListNode(0)
    dummy.next = head
    
    # Initialize pointers
    pointer = dummy

    # Use pointer to traverse the entire LinkedList
    while pointer is not None:
        
        # Initialize k_tracker pointer (tracks steps within group of k)
        k_tracker = pointer

        # Verify we have enough nodes to form a group
        for i in range(k):
            
            # If we reach the end of the list (i.e. don't have k elements), we're done
            if k_tracker == None:
                break
            
            # If we haven't hit None, keep checking the next node until we've check k nodes
            k_tracker = k_tracker.next

        # Verify if the last node (i.e. k) is not Null
        if k_tracker == None:
            break

        # If requirements met, reverse group of k elements by specifying head and k
        prev, current  = reverse(pointer.next, k)

        # Updated nodes/pointers to add reveresed section back to LinkedList
        last_node_reverse_group = pointer.next
        last_node_reverse_group.next = current
        pointer.next = prev
        pointer = last_node_reverse_group

    # Return dummy.next (i.e. modified head)
    return dummy.next



# Update to take additional parameter, k
def reverse(head, k):

    # Initialize pointers
    prev = None 
    next = None 
    current = head
    
    # Traverse LinkedList until current pointer reaches the end 
    for _ in range(k):
      # Update pointers 
      next = current.next
      current.next = prev
      
      # Move pointers up a step
      prev = current 
      current = next

    # Return previous (new head)  
    return prev, current



# Time Complexity = O(n)
# Space Complexity = O(1)



############################################################



# Driver code
def main():
    input_list = [[1, 2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 2, 8, 7, 7], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7], [1]]
    k = [3, 2, 1, 7, 1]

    for i in range(len(input_list)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input_list[i])

        print(i + 1, ".\tLinked list: ", end=" ")
        print_list_with_forward_arrow(input_linked_list.head)
        print('\n')
        print("\tReversed linked list: ", end=" ")
        result = reverse_k_groups(input_linked_list.head, k[i])
        print_list_with_forward_arrow(result)
        print("\n")
        print('-'*100)

if __name__ == '__main__':
    main()