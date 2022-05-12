import addnum
def test_add():
    assert addnum.add("3,5")==8;

def test_inputemptyString():
    assert addnum.add("")==0;

def test_singleinputString():
    assert addnum.add("1")==1;

def test_nInputString():
    assert addnum.add("1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20")==210;

def test_inputWithNewLinesString():
    assert addnum.add("1\n2,3")==6;

def test_inputWithDelimiterString():
    assert addnum.add("//;\n1;2")==3;
    assert addnum.add("//;\n1;2\\-*/")==3;
    assert addnum.add("//;\n1;\n2,3")==6;

def test_negativeadd():
    assert addnum.add("-1,4")=="negatives not allowed -1";
    assert addnum.add("1,-4")=="negatives not allowed -4";
    
