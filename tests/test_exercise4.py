import exercise4 as ex


def test_hex_number():
    assert ex.hex_output("50") == 80
    assert ex.hex_output("FF") == 255

    
def test_hex_ord_chr():
    assert ex.hex_output("50") == 80
    assert ex.hex_output("FF") == 255


def test_name_triangle():
    # act
    triangle = ex.name_triangle("Don Quixote")
    assert triangle[0] == "D"
    assert triangle[10] == "Don Quixote"