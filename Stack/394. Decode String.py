class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        stack = []
        num_left = 0
        num_right = 0
        digits = set(str(i) for i in range(10))  # ten digits

        for char in s:
            if char == "]":
                num_right += 1

                temp = ""  # the sub-string, [temp]
                while stack[-1] != "[":
                    temp = stack.pop() + temp

                stack.pop()  # pop the "["

                num = ""  # the number of repeating, num[temp]
                while stack and stack[-1] in digits:  # note stack may be empty
                    num = stack.pop() + num

                sub_string = temp * int(num) if not num else temp

                if num_left != num_right:
                    # sub_string is between brackets, [xx num[temp] xxx] => [xx sub_string xx]
                    # push it into the stack
                    stack.append(sub_string)
                else:
                    res += sub_string
            elif char == "[":
                num_left += 1
                stack.append(char)
            elif char in digits:
                stack.append(char)
            else:  # letter
                if num_left != num_right:
                    # char is between brackets, [xxx char xxx]
                    stack.append(char)
                else:
                    res += char

        return res
