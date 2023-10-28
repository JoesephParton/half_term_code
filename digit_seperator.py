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

dg = Digit_Seperator(input("Number to seperate: "))
print(dg.digit_seperator())

