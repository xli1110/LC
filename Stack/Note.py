"""
1 - Pattern Matching

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



2 - Monotonic Stack
    Four Steps: mono; res; push; ite
    Loop from the End:
        monotonic stack with x >= arr[stack[-1]]
        res[i] = stack[-1]
        push(x)
        i -= 1

    Problems:
    739(next greater element) - classic model
"""
