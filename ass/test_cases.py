import addnum
def test_add():
    assert addnum.add("3,5")==8;

def test_inputemptyString():
    assert addnum.add("")==0;