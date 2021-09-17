import statistics as stat
from decimal import Decimal

def run_timing() -> None:
    times = []

    while time := input('Enter a 10K time: '):
        try:
            times.append(float(time))
        except ValueError:
            print(f"{time} is not a valid 10K time.")

    print(f"Your average time is {stat.mean(times):.2f}")


def before_and_after(number: float, before: int, after: int) -> float:
    str_number = str(number)
    (str_before, str_after) = tuple(str_number.split('.'))
    str_before = str_before[-before:]
    str_after = str_after[:after]
    str_result = '.'.join((str_before, str_after))
    return float(str_result)

def add_floats(number1: str, number2: str) -> float:
    decimal1 = Decimal(number1)
    decimal2 = Decimal(number2)
    return float(decimal1 + decimal2)


if __name__ == "__main__":
    run_timing()
