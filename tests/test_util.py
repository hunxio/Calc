import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util import *

def test_add():
    assert add(1, 1) == 2
    assert add(-1, 1) == 0
    assert add(1, -1) == 0
    assert add(-1, -1) == -2

def test_substr():
    assert substract(1, 1) == 0
    assert substract(-1, 1) == -2
    assert substract(1, -1) == 2
    assert substract(-1, -1) == 0

def test_multiply():
    assert multiply(1, 1) == 1
    assert multiply(-1, 1) == -1
    assert multiply(1, -1) == -1
    assert multiply(-1, -1) == 1
    assert multiply(0, 1) == 0
    assert multiply(2, 2.5) == 5

def test_divide():
    assert divide(1, 1) == 1
    assert divide(-1, 1) == -1
    assert divide(1, -1) == -1
    assert divide(-1, -1) == 1
    assert divide(0, 1) == 0
    assert divide(100, 33) == 3.0