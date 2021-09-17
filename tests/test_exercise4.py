import exercise4 as ex


def test_hex_number():
    assert ex.hex_output("50") == 80
    assert ex.hex_output("FF") == 255
