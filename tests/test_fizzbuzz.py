from src import fizzbuzz

import pytest

def test_fizz():
    assert(fizzbuzz.fizzbuzz(3)) == "fizz" 

def test_buzz(): 
    assert(fizzbuzz.fizzbuzz(5)) == "buzz"

def test_fizzbuzz():
    assert(fizzbuzz.fizzbuzz(15)) == "fizzbuzz"

def test_return_num(): 
  assert(fizzbuzz.fizzbuzz(1)) == 1
