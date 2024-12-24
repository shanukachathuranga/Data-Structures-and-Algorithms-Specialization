def printN(x):
    if x >= 5:
        return

    print(f"{x}")

    printN(x + 1)
    printN(x + 2)


# Call the function
printN(1)
