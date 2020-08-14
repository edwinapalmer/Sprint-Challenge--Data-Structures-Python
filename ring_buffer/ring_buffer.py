# from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        elif len(self.storage) == self.capacity:
            to_delete = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if to_delete == self.current:
                self.current = self.storage.tail


        # self.storage[self.current] = item
        # self.current += 1
        # if self.current == self.capacity:
        #     self.current = 0


    def get(self):
        list_buffer_contents = []
        initial_node = self.current
        list_buffer_contents.append(initial_node.value)

        if initial_node.next is not None:
            next_node = initial_node.next
        else:
            next_node = self.storage.head

        while next_node != initial_node:
            list_buffer_contents.append(next_node.value)
            if next_node.next is not None:
                next_node = next_node.next
            else:
                next_node = self.storage.head

        return list_buffer_contents


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
                self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
     

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value
        
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return 
        self.add_to_head(node.value)
        self.delete(node)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
       if node is self.tail:
           return
       self.add_to_tail(node.value)
       self.delete(node)
       

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # Planning
        if self.head is None and self.tail is None:
            return
        # TODO: Do we need error checking if node not in list?
       
        # This is the only node
        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        # It's the head
        elif node is self.head:
            self.head = node.next
            node.delete()
        # It's the tail
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        # It's in the middle
        else:
            node.delete()

        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # How to get max
        if self.head is None and self.tail is None:
            return 

        max_val = self.head.value
        current = self.head.next
        # Loop through nodes
        while current is not None:
            # compare value in node to max found
            if current.value > max_val:
                max_val = current.value
            current = current.next
        # return max found
        return max_val

        # return [item for item in self.storage if item is not None]