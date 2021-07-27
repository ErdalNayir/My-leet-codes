def reverse(x):

    if x<0:

        number = str(x)

        numberSplitted= number.split("-")

        symbol = "-"

        numberNew = numberSplitted[1]

        numberNew = numberNew[::-1]

        result = int(symbol+numberNew)

        if result>= (-2**31) and result <= (2**31) -1:

            return result
        else:
            return 0

    elif x>0:

        number = str(x)

        number = number[::-1]

        result = int(number)

        if result>= (-2**31) and result <= (2**31) -1:

            return result
        else:
            return 0

    elif x== 0:

        return 0




print(reverse(-34356470))
print(reverse(0))
print(reverse(34546540))
print(reverse(1534236469))
