import pytest
from SingleObject import SingleObject

def test_singleton():
    assert SingleObject.instance().counter() == 1
    assert SingleObject.instance().counter() == 2
    assert SingleObject.instance().counter() == 3
    assert SingleObject.instance().counter() == 4
    assert SingleObject.instance().counter() == 5
