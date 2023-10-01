from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    data: int
    next_node: Node | None = None


def insert_node(head: Node | None, data: int) -> Node:
    """
    Insert a new node at the end of a linked list and return the new head.
    >>> head = insert_node(None, 1)
    >>> head = insert_node(head, 2)
    >>> head = insert_node(head, 3)
    >>> print_linked_list(head)
    1->2->3
    """
    new_node = Node(data)
    # If the linked list is empty, the new_node becomes the head
    if head is None:
        return new_node

    temp_node = head
    while temp_node.next_node is not None:
        temp_node = temp_node.next_node

    temp_node.next_node = new_node  # type: ignore
    return head


def length_of_linked_list(head: Node | None) -> int:
    """
    find length of linked list
    >>> head = insert_node(None, 10)
    >>> head = insert_node(head, 9)
    >>> head = insert_node(head, 8)
    >>> length_of_linked_list(head)
    3
    """
    length = 0
    while head is not None:
        length += 1
        head = head.next_node
    return length


def print_linked_list(head: Node | None) -> None:
    """
    print the entire linked list
    >>> head = insert_node(None, 1)
    >>> head = insert_node(head, 2)
    >>> head = insert_node(head, 3)
    >>> print_linked_list(head)
    1->2->3
    """
    if head is not None:
        while head.next_node is not None:
            print(head.data, end="->")
            head = head.next_node
        print(head.data)


def reverse_k_nodes(head: Node | None, group_size: int) -> Node | None:
    """
    reverse nodes within groups of size k
    >>> head = insert_node(None, 1)
    >>> head = insert_node(head, 2)
    >>> head = insert_node(head, 3)
    >>> head = insert_node(head, 4)
    >>> head = insert_node(head, 5)
    >>> new_head = reverse_k_nodes(head, 2)
    >>> print_linked_list(new_head)
    2->1->4->3->5
    """
    if head is None or head.next_node is None:
        return head

    length = length_of_linked_list(head)

    dummy_head = Node(0)
    dummy_head.next_node = head

    previous_node = dummy_head

    while length >= group_size:
        assert previous_node
        current_node = previous_node.next_node
        assert current_node
        next_node = current_node.next_node
        for _ in range(1, group_size):
            assert next_node, current_node
            current_node.next_node = next_node.next_node
            assert previous_node
            next_node.next_node = previous_node.next_node
            assert previous_node
            previous_node.next_node = next_node
            assert current_node
            next_node = current_node.next_node
        previous_node = current_node
        length -= group_size
    assert dummy_head
    return dummy_head.next_node


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    k = 2
    head = insert_node(None, 1)
    head = insert_node(head, 2)
    head = insert_node(head, 3)
    head = insert_node(head, 4)
    head = insert_node(head, 5)

    print("Original Linked List: ", end="")
    print_linked_list(head)
    print(f"After reversing groups of size {k}: ", end="")
    new_head = reverse_k_nodes(head, k)
    print_linked_list(new_head)
