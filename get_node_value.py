"""
- Single pass through the linked list using two pointers, Ahead and Behind. 

- Behind pointer is at the start, and the Ahead pointer is n places ahead of the Behind pointer, where n represents the position from the tail that we want to get the data from.

- If they then traverse the linked list, the behind pointer will be n from the end when the ahead pointer reaches the end, and we can then just return behind.data.

"""

def getNode(head, positionFromTail):
    if head == None:
        return None
    behind, ahead = head, head
    i = 0
    while i < positionFromTail:
        ahead = ahead.next
        i += 1
    while ahead.next:
        ahead = ahead.next
        behind = behind.next
    return behind.data