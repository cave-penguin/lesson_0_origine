def calc(line):
    operand_1, operation, operand_2 = line.split(" ")
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    """match operation:
        case "+":
            print(f"Result: {operand_1 + operand_2}")
        case "-":
            print(f"Result: {operand_1 - operand_2}")
        case "*":
            print(f"Result: {operand_1 * operand_2}")
        case "/":
            print(f"Result: {operand_1 / operand_2}")"""


cnt = 0

with open("data.txt", "r") as file:
    for line in file:
        cnt += 1
        try:
            calc(line)
        except ValueError as exc:
            if "unpack" in exc.args[0]:
                print(f"Wrong data format in line {cnt}, not enough data for answer")
            else:
                print(
                    f"Wrong data format in line {cnt}, cannot be converted to a number"
                )
