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

    testDLL = DoublyLinkedList()

    # TEST 1 - Test DLL creation
    # BEFORE TESTING: implement DoublyLinkedList __init__
    TEST_new_dll(testDLL)

    # TEST 2 - Test DoublyNode
    # BEFORE TESTING: implement DoublyNode class
    TEST_doubly_node(DoublyLinkedList)

    # TEST 3 - Test DLL head_insert
    # BEFORE TESTING: implement DoublyLinkedList head_insert, __str__, __len__, __is_empty
    TEST_head_insert(testDLL, DoublyLinkedList)

    # TEST 4 - Test DLL head_remove
    # BEFORE TESTING: implement DoublyLinkedList head_remove
    TEST_head_remove(testDLL)

    # TEST 5 - Test DLL tail_insert
    # BEFORE TESTING: implement DoublyLinkedList tail_insert
    TEST_tail_insert(testDLL, DoublyLinkedList)

    # TEST 6 - Test DLL tail_remove
    # BEFORE TESTING: implement DoublyLinkedList tail_remove
    TEST_tail_remove(testDLL)

    # TEST 7 - Test DLL head_insert & tail_insert
    # BEFORE TESTING: implement DoublyLinkedList head_insert & tail_insert
    TEST_insert_methods(testDLL, DoublyLinkedList)

    # TEST 8 - Test DLL head_remove & tail_remove
    # BEFORE TESTING: implement DoublyLinkedList head_remove & tail_remove
    TEST_remove_methods(testDLL)

    # TEST 9 - Test docstrings
    # BEFORE TESTING: implement all methods & docstrings
    TEST_docs(testDLL, DoublyLinkedList)


if __name__ == "__main__":
    os.system("cls")
    main()
