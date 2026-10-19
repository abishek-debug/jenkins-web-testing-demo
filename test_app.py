from app import welcome

def test_welcome():
    assert welcome("Jenkins") == "Hello, Jenkins!"

def test_empty_name():
    assert welcome("") == "Hello, !"
