import pytest
from src.exercise import print_from_number_to_one

def test_exercise(capsys):
    print_from_number_to_one(4)
    out, err = capsys.readouterr()
    assert out == "4\n3\n2\n1\n", "Should read '4\n3\n2\n1\n'"
