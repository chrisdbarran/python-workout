import exercise6 as ex

def test_pl_sentence():
    assert ex.pl_sentence('this is a test translation') == "histay isway away esttay ranslationtay"

def test_nonsense():
    filename = './tests/text_file_ex5.txt'
    assert ex.nonsense(filename) == "Thus, assuming translate version away, it string with good a"

def test_transpose():
    provided = ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']
    expected = ['abc jkl stu', 'def mno vwx', 'ghi pqr yz']

    assert ex.transpose(provided) == expected

def test_apache_log():
    filename = './tests/apache.txt'
    assert ex.apache(filename) == "192.168.2.21"