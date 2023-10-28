class Digit_Seperator():
    def __init__(self, number):
        self.number = number

    def digit_seperator(self):
        num = self.number[::-1]
        result = ""
        for i in range(0, len(num)):
            if i % 3 == 0 and i != 0:
                result += ","
            result += num[i]

        return result[::-1]

running = True
while running:
    digit = input("Number to seperate: ")
    if digit.isnumeric() is True:
        dg = Digit_Seperator(digit)
        print(dg.digit_seperator())
    else:
        if digit == "X":
            print("Exit")
            running = False
        else:
            print("incorrect Input")
