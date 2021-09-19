from typing import List


def hex_output(hex_number: str) -> int:
    hexs = "0123456789ABCDEF"
    decimal_value = 0
    for power, num in enumerate(reversed(hex_number)):
        val = hexs.index(num)
        decimal_value += val * (16 ** power)
    return decimal_value


def hex_ord_chr(hex_number: str) -> int:
    arg = f"0x{hex_number}"
    return ord(chr(arg))


def name_triangle(name: str) -> List[str]:
    triangle = []
    for i in range(0, len(name)):
        sub = name[:i + 1]
        triangle.append(sub)
        print(sub)
    return triangle


if __name__ == "__main__":
    hex_number = input("Enter a hex number: ")
    dec_number = hex_output(hex_number)
    print(f"The decimal equivalent is {dec_number}")
