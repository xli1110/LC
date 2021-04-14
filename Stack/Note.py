"""
1 - Design

    Problems:
    155(min stack)



2 - Pattern Matching

    Model:
    stack = []
    loop the string:
        if find pattern end:
            stack.pop() until pattern start or empty stack
        else:
            stack.append(char)
    check if stack is empty

    Problems:
    20(valid parentheses)
    394(decode string) - num_left and num_right help us determine current location
    Airbnb(Simplified XML Validator)
"""
