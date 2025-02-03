##### Global color variables #####
from colorama import Fore

R = Fore.RED
G = Fore.GREEN
B = Fore.BLUE
W = Fore.RESET
P = Fore.CYAN

'''IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama'''


##################################

def result(flag):
    if flag:
        return f"{G}PASSED{W}"

    return f"{R}FAILED{W}"


def test_sequence(DLL, forw_sequ):
    try:
        walk = DLL.head
        for el in forw_sequ:
            if el != walk.value:
                return False

            walk = walk.next

        rev_sequ = forw_sequ[::-1]
        walk = DLL.tail
        for el in rev_sequ:
            if el != walk.value:
                return False

            walk = walk.prev

        return True

    except:
        return False


def TEST_new_dll(DLL):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: New DLL Creation{W}\n")

    test = DLL.head == None
    print(f"New DLL head pointer is set to None: {result(test)}")

    test = DLL.tail == None
    print(f"New DLL tail pointer is set to None: {result(test)}")

    sz = DLL._DoublyLinkedList__size
    print(f"New DLL size attribute is private: {result(True)}")

    test = sz == 0
    print(f"Size of new DLL is zero: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_doubly_node(class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: The DoublyNode Class{W}\n")

    try:
        node1 = class_ref().DoublyNode("A")
        print(f"{B}A temporary test node was created: {node1}{W}\n")
        print(f"DoublyNode class is nested within DoublyLinkedList: {result(True)}")
    except:
        print(f"DoublyNode class is nested within DoublyLinkedList: {result(False)}")

    test = node1.value == "A"
    print(f"DoublyNode value is set properly: {result(test)}")

    test = node1.prev == None
    print(f"New DoublyNode prev is set to None: {result(test)}")

    test = node1.next == None
    print(f"New DoublyNode next is set to None: {result(test)}\n")

    try:
        node1.set_prev("B")
        print(f"set_prev() raises exception if prev is not type DoublyNode: {result(False)}")
    except:
        print(f"set_prev() raises exception if prev is not type DoublyNodee: {result(True)}")

    node2 = class_ref().DoublyNode("B")
    node1.set_prev(node2)
    test = node1.prev == node2 and node1.prev.value == "B"
    print(f"DoublyNode set_prev updates self.prev: {result(test)}")

    test = node2.next == node2.prev == None
    print(f"DoublyNode set_prev does not change other node: {result(test)}")

    try:
        node1.set_prev(None)
        test = node1.prev == None
        print(f"DoublyNode prev can be set to None: {result(test)}")
    except:
        print(f"DoublyNode prev can be set to None: {result(False)}")

    try:
        node1.set_next("B")
        print(f"\nset_next() raises exception if next is not type DoublyNode: {result(False)}")
    except:
        print(f"\nset_next() raises exception if next is not type DoublyNode: {result(True)}")

    node3 = class_ref().DoublyNode("C")
    node1.set_next(node3)
    test = node1.next == node3 and node1.next.value == "C"
    print(f"DoublyNode set_next updates self.next: {result(test)}")

    test = node3.prev == node3.next == None
    print(f"DoublyNode set_next does not change other node: {result(test)}")

    try:
        node1.set_next(None)
        test = node1.next == None
        print(f"DoublyNode next can be set to None: {result(test)}")
    except:
        print(f"DoublyNode next can be set to None: {result(False)}")

    print("~" * 50, "\n\n")


def TEST_head_insert(DLL, class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: The DoublyLinkedList head_insert{W}\n")

    temp_node = class_ref().DoublyNode("temp")

    DLL.head_insert("A")
    print(f"{B}A node was inserted: {DLL}{W}\n")

    test = type(DLL.head) == type(temp_node)
    print(f"DLL head_insert inserts new DoublyNode object: {result(test)}")

    test = DLL.head.value == "A" and DLL.tail.value == "A"
    print(f"Insert into an empty DLL updates head and tail pointers: {result(test)}")

    test = type(DLL.head) == type(DLL.tail) == type(temp_node)
    print(f"DLL head and tail pointers reference DoublyNode objects: {result(test)}")

    test = len(DLL) == 1
    print(f"DLL head_insert increases size attribute: {result(test)}")

    DLL.head_insert("B")
    print(f"\n{B}A second node was inserted: {DLL}{W}\n")

    test = DLL.head.value == "B" and DLL.tail.value == "A"
    print(f"Insert into a non-empty DLL updates head pointer: {result(test)}")

    test = DLL.head.prev == None and DLL.head.next == DLL.tail
    print(f"New node inserted at head has no prev and its next is the tail: {result(test)}")

    test = DLL.tail.prev == DLL.head and DLL.tail.next == None
    print(f"Old DLL head prev is the new head and old head next is preserved: {result(test)}")

    for el in "CDEF":
        DLL.head_insert(el)

    print(f"\n{B}Several nodes were inserted: {DLL}{W}\n")

    test = DLL.head.value == "F" and DLL.tail.value == "A"
    print(f"Head and Tail pointers are correct: {result(test)}")

    test = test_sequence(DLL, "FEDCBA")
    print(f"Connections between nodes are correctly linked: {result(test)}")

    test = len(DLL) == 6
    print(f"DLL head_insert increases size appropriately: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_head_remove(DLL):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: The DoublyLinkedList head_remove{W}\n")

    print(f"{B}Current state of DLL: {DLL}{W}\n")

    val = DLL.head_remove()
    print(f"{B}Head element |{val}| was removed: {DLL}{W}\n")

    test = type(val) == str
    print(f"DLL head_remove returns node value, not DoublyNode object: {result(test)}")

    test = val == "F"
    print(f"DLL head_remove returns correct value: {result(test)}")

    test = DLL.head.value == "E"
    print(f"\nDLL head_remove affects DLL head pointer: {result(test)}")

    test = DLL.head.prev == None
    print(f"New head node has no prev: {result(test)}")

    test = DLL.tail.value == "A"
    print(f"DLL head_remove does not affect DLL tail pointer: {result(test)}")

    test = len(DLL) == 5
    print(f"\nDLL head_remove decreases list size: {result(test)}")

    test = test_sequence(DLL, "EDCBA")
    print(f"Node sequencing is correct, all pointers validated: {result(test)}")

    for i in range(4):
        DLL.head_remove()

    print(f"\n{B}DLL reduced to length one with head_remove: {DLL}{W}\n")

    test = DLL.head == DLL.tail
    print(f"DLL of length one sets head and tail pointers to the same node: {result(test)}")

    try:
        val = DLL.head_remove()
        print(f"DLL head_remove from list length one follows altered protocol: {result(True)}")
    except:
        print(f"DLL head_remove from list length one follows altered protocol: {result(False)}")

    test = len(DLL) == 0 and DLL.head == None and DLL.tail == None
    print(f"Emptied DLL resets head and tail pointers to None: {result(test)}")

    print(f"\n{B}DLL has been emptied: {DLL}{W}\n")

    try:
        DLL.head_remove()
        print(f"Remove from empty DLL raises exception: {result(False)}")
    except:
        print(f"Remove from empty DLL raises exception: {result(True)}")

    print("~" * 50, "\n\n")


def TEST_tail_insert(DLL, class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: The DoublyLinkedList tail_insert{W}\n")

    temp_node = class_ref().DoublyNode("temp")

    DLL.tail_insert("A")
    print(f"{B}A node was inserted: {DLL}{W}\n")

    test = type(DLL.tail) == type(temp_node)
    print(f"DLL tail_insert inserts new DoublyNode object: {result(test)}")

    test = DLL.head.value == "A" and DLL.tail.value == "A"
    print(f"Insert into an empty DLL updates head and tail pointers: {result(test)}")

    test = type(DLL.head) == type(DLL.tail) == type(temp_node)
    print(f"DLL head and tail pointers reference DoublyNode objects: {result(test)}")

    test = len(DLL) == 1
    print(f"DLL tail_insert increases size attribute: {result(test)}")

    DLL.tail_insert("B")
    print(f"\n{B}A second node was inserted: {DLL}{W}\n")

    test = DLL.tail.value == "B" and DLL.head.value == "A"
    print(f"Insert into a non-empty DLL updates tail pointer: {result(test)}")

    test = DLL.tail.next == None and DLL.head.next == DLL.tail
    print(f"New node inserted at tail has no next and its prev is the head: {result(test)}")

    test = DLL.tail.prev == DLL.head and DLL.head.prev == None
    print(f"Old DLL tail next is the new tail and old tail prev is preserved: {result(test)}")

    for el in "CDEF":
        DLL.tail_insert(el)

    print(f"\n{B}Several nodes were inserted: {DLL}{W}\n")

    test = DLL.tail.value == "F" and DLL.head.value == "A"
    print(f"Head and Tail pointers are correct: {result(test)}")

    test = test_sequence(DLL, "ABCDEF")
    print(f"Connections between nodes are correctly linked: {result(test)}")

    test = len(DLL) == 6
    print(f"DLL tail_insert increases size appropriately: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_tail_remove(DLL):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: The DoublyLinkedList tail_remove{W}\n")

    print(f"{B}Current state of DLL: {DLL}{W}\n")

    val = DLL.tail_remove()
    print(f"{B}Tail element |{val}| was removed: {DLL}{W}\n")

    test = type(val) == str
    print(f"DLL tail_remove returns node value, not DoublyNode object: {result(test)}")

    test = val == "F"
    print(f"DLL tail_remove returns correct value: {result(test)}")

    test = DLL.tail.value == "E"
    print(f"\nDLL tail_remove affects DLL tail pointer: {result(test)}")

    test = DLL.tail.next == None
    print(f"New tail node has no next: {result(test)}")

    test = DLL.head.value == "A"
    print(f"DLL tail_remove does not affect DLL head pointer: {result(test)}")

    test = len(DLL) == 5
    print(f"\nDLL tail_remove decreases list size: {result(test)}")

    test = test_sequence(DLL, "ABCDE")
    print(f"Node sequencing is correct, all pointers validated: {result(test)}")

    for i in range(4):
        DLL.tail_remove()

    print(f"\n{B}DLL reduced to length one with tail_remove: {DLL}{W}\n")

    test = DLL.head == DLL.tail
    print(f"DLL of length one sets head and tail pointers to the same node: {result(test)}")

    try:
        val = DLL.tail_remove()
        print(f"DLL tail_remove from list length one follows altered protocol: {result(True)}")
    except:
        print(f"DLL tail_remove from list length one follows altered protocol: {result(False)}")

    test = len(DLL) == 0 and DLL.head == None and DLL.tail == None
    print(f"Emptied DLL resets head and tail pointers to None: {result(test)}")

    print(f"\n{B}DLL has been emptied: {DLL}{W}\n")

    try:
        DLL.tail_remove()
        print(f"Remove from empty DLL raises exception: {result(False)}")
    except:
        print(f"Remove from empty DLL raises exception: {result(True)}")

    print("~" * 50, "\n\n")


def TEST_insert_methods(DLL, class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: The re-test head_insert & tail_insert{W}\n")

    print(f"{B}Current state of DLL: {DLL}{W}\n")

    for i, el in enumerate("ABCDEF"):
        if i % 2 == 0:
            DLL.head_insert(el)
        else:
            DLL.tail_insert(el)

    print(f"{B}Six elements were added to DLL: {DLL}{W}\n")

    test = len(DLL) == 6
    print(f"List size was updated correctly: {result(test)}")

    test = DLL.head.value == "E" and DLL.head.prev == None and DLL.head.next != None
    print(f"Head node is correct and has no prev: {result(test)}")

    test = DLL.tail.value == "F" and DLL.tail.next == None and DLL.tail.prev != None
    print(f"Tail node is correct and has no next: {result(test)}")

    test = True
    temp_node = class_ref().DoublyNode("temp")
    walk = DLL.head
    for i in range(len(DLL)):
        if type(walk) != type(temp_node):
            test = False
            break
        walk = walk.next
    print(f"DLL contains only DoublyNode objects: {result(test)}")

    test = test_sequence(DLL, "ECABDF")
    print(f"Node sequencing is correct, all pointers validated: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_remove_methods(DLL):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: The re-test head_remove & tail_remove{W}\n")

    print(f"{B}Current state of DLL: {DLL}{W}\n")

    test_dtype = True
    test_seq = True
    test_conn = True
    test_head_prev = True
    test_tail_next = True
    rem_seq = "FEDCBA"
    dll_val_order = "ECABDF"

    for i in range(len(DLL)):

        if not test_sequence(DLL, dll_val_order):
            test_conn = False

        if i % 2 == 0:
            val = DLL.tail_remove()
            dll_val_order = dll_val_order[:-1]
        else:
            val = DLL.head_remove()
            dll_val_order = dll_val_order[1:]

        if rem_seq[i] != val:
            test_seq = False
        if type(val) != str:
            test_dtype = False
        if len(DLL) > 0:
            if DLL.head.prev != None:
                test_head_prev = False
            if DLL.tail.next != None:
                test_tail_next = False

    print(f"{B}DLL was emptied: {DLL}{W}\n")

    print(f"DLL removal methods return value data type: {result(test_dtype)}")

    print(f"DLL removals methods removed correct list positions: {result(test_seq)}")

    print(f"All node connections preserved throughout removals: {result(test_conn)}")

    print(f"Head prev is always None: {result(test_head_prev)}")

    print(f"Tail next is always None: {result(test_tail_next)}")

    test = len(DLL) == 0
    print(f"Removal methods impact size: {result(test)}")

    test = DLL.head == None and DLL.tail == None
    print(f"Final head and tail pointers are None: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_docs(DLL, class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Docstrings{W}\n")

    print("DoublyNode Class Docstrings:\n")
    doc = class_ref.DoublyNode.set_prev.__doc__
    if doc != None:
        print(f"{B}set_prev() Documentation:{W} {doc}\n")
    else:
        print(f"{R}set_prev() Documentation Missing{W}\n")

    doc = class_ref.DoublyNode.set_next.__doc__
    if doc != None:
        print(f"{B}set_next() Documentation:{W} {doc}\n")
    else:
        print(f"{R}set_next() Documentation Missing{W}\n")

    doc = class_ref.DoublyNode.__str__.__doc__
    if doc != None:
        print(f"{B}str() Documentation:{W} {doc}\n")
    else:
        print(f"{R}str() Documentation Missing{W}\n")

    print("\n\nDoublyLinkedList Class Docstrings:\n")
    doc = DLL.head_insert.__doc__
    if doc != None:
        print(f"{B}head_insert() Documentation:{W} {doc}\n")
    else:
        print(f"{R}head_insert() Documentation Missing{W}\n")

    doc = DLL.tail_insert.__doc__
    if doc != None:
        print(f"{B}tail_insert() Documentation:{W} {doc}\n")
    else:
        print(f"{R}tail_insert() Documentation Missing{W}\n")

    doc = DLL.head_remove.__doc__
    if doc != None:
        print(f"{B}head_remove() Documentation:{W} {doc}\n")
    else:
        print(f"{R}head_remove() Documentation Missing{W}\n")

    doc = DLL.tail_remove.__doc__
    if doc != None:
        print(f"{B}tail_remove() Documentation:{W} {doc}\n")
    else:
        print(f"{R}tail_remove() Documentation Missing{W}\n")

    doc = DLL._DoublyLinkedList__is_empty.__doc__
    if doc != None:
        print(f"{B}is_empty() Documentation:{W} {doc}\n")
    else:
        print(f"{R}is_empty() Documentation Missing{W}\n")

    doc = DLL.__len__.__doc__
    if doc != None:
        print(f"{B}len() Documentation:{W} {doc}\n")
    else:
        print(f"{R}len() Documentation Missing{W}\n")

    doc = DLL.__str__.__doc__
    if doc != None:
        print(f"{B}str() Documentation:{W} {doc}\n")
    else:
        print(f"{R}str() Documentation Missing{W}\n")

    print("~" * 50, "\n\n")