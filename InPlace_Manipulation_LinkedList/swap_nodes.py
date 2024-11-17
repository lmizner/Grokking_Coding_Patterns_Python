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


def swap(node1, node2):
    temp = node1.data
    node1.data = node2.data
    node2.data = temp



############################################################



def swap_nodes(head, k):

    # Initialize pointer and counter
    current = head
    count = 0
    
    # Initialize variables to store front and end 
    front = None
    end = None

    # Traverse the the full LinkedList using current as the pointer
    while current:
        count += 1
        
        # Once end is set to head, begin iterating    
        if end is not None:
            end = end.next

        # Once we reach k, front and end variables get set
        if count == k:
            front = current
            end = head
        
        # Move to next step in the loop
        current = current.next
    
    # Swap nodes
    swap(front, end)

    return head



# Time Complexity = O(n)
# Space Complexity = O(1)



############################################################



# Driver code
def main():
    input_list = [
        [1, 2, 3, 4, 5, 6, 7],
        [6, 9, 3, 10, 7, 4, 6],
        [6, 9, 3, 4],
        [6, 2, 3, 6, 9],
        [6, 2]
    ]
    k = [2, 3, 2, 3, 1]

    for i in range(len(input_list)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input_list[i])
        print(i + 1, ".\tOriginal linked list is: ", end="", sep="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tk:", k[i])
        if k[i] <= 0:
            print("\tThe expected 'k' to have value from 1 \
            to length of the linked list only.")
        else:
            result = swap_nodes(input_linked_list.head, k[i])
            print("\tLinked list with swapped values: ", end="")
            print_list_with_forward_arrow(result)
        print("\n", "-"*100, sep="")


if __name__ == '__main__':
    main()



