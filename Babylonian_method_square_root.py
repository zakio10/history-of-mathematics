def babylonian_method(rep, first_value, square_num, output_process = False):
    """Calculating square root by babylonian method

    This program is for calculating square root by babylonian method.
    When you input the number of babylonian algorithm's repetitions, first approximate value
    and aimed square number, this function will return the better approximate square root.

    Args:
        rep (int): the number of babylonian algorithm's repetitions.
        first_value (double): first approximate value.(you can input rough or guessing square root value.)
        square_num (int): the square of the aimed square root.(e.g. if you want value of √2, you have to input 2)
        output_process (boolean): If you want to see the report of calcilateing, you have to choose true.

    Returns:
        double: The final value of calculating square root by babylonian method.
    """
    now_value = first_value
    if output_process is True:
        print("Input value is " + str(now_value) +".")
    for i in range(rep):
        next_value = 0.5*(now_value + (square_num / now_value))
        if output_process is True:
            print(str((i + 1)) + "th calculated value is " + str(next_value))
        now_value = next_value
    
    return now_value

repnum = int(input("the number of babylonian algorithm's repetitions:"))
firstval = float(input("first approximate value:"))
squval = int(input("the square of the aimed square root:"))

ans = babylonian_method(repnum, firstval, squval, True)
print("Final value is " + str(ans))