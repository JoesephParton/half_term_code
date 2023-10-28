def stan_form(num):
    exponent = 0
    while num >= 10:
        num /= 10
        exponent += 1
    return (str(num) + "x10^" + str(exponent))

print(stan_form(int(input("Number: "))))
