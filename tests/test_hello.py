from lib.hello import *

def test_hello_sarah_returns_hello_sarah():
    expected = 'Hello, Sarah!'
    actual = hello('Sarah')

    assert actual == expected

def test_hello_james_returns_hello_james():
    expected = 'Hello, James!'
    actual = hello('James')

    assert actual == expected


# we want to get 'Hello, Sarah!' back when called hello('Sarah') 