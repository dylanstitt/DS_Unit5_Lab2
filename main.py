# Dylan Stitt
# Unit 5 Lab 2
# Doubly Linked List

# Implementation & testing of the DoublyLinkedList class

from DoublyLinkedList import DoublyLinkedList
from TEST_CODE import *
import os

'''
Testing details can be found in TEST_CODE.py

ENSURE ALL TESTS PASS BEFORE SUBMITTING

IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama
'''

def main():

    testSLL = DoublyLinkedList()

    # TEST 1 - Test SLL creation
    # BEFORE TESTING: implement SinglyLinkedList __init__
    TEST_new_DoublyLinkedList(testSLL)

    # TEST 2 - Test SinglyNode
    # BEFORE TESTING: implement SinglyNode __init__ & set_next
    TEST_singly_node(DoublyLinkedList)

    # TEST 3 - Test SLL head_insert
    # BEFORE TESTING: implement SinglyLinkedList head_insert, __str__, __len__, __is_empty
    TEST_head_insert(testSLL, DoublyLinkedList)

    # TEST 4 - Test SLL head_remove
    # BEFORE TESTING: implement SinglyLinkedList head_remove
    TEST_head_remove(testSLL)

    # TEST 4 - Test SLL tail_insert
    # BEFORE TESTING: implement SinglyLinkedList tail_insert
    TEST_tail_insert(testSLL, DoublyLinkedList)

    # TEST 5 - Test SLL head_insert & tail_insert
    # BEFORE TESTING: implement SinglyLinkedList methods
    TEST_head_tail_insert(testSLL, DoublyLinkedList)

    # TEST 6 - Test docstrings
    # BEFORE TESTING: implement all methods & docstrings
    TEST_docs(testSLL, DoublyLinkedList)

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()