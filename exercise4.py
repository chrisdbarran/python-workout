def hex_output(hex_number: str) -> int:
    hexs = "0123456789ABCDEF"
    decimal_value = 0
    for power, num in enumerate(reversed(hex_number)):
        val = hexs.index(num)
        decimal_value += val * (16 ** power)
    return decimal_value


if __name__ == "__main__":
    hex_number = input("Enter a hex number: ")
    dec_number = hex_output(hex_number)
    print(f"The decimal equivalent is {dec_number}")
