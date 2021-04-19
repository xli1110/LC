"""
The input is an ASCII string, we have to write a Java program to check if the given String is valid XML or not.
For simplicity purposes, the XML string only has content and tags.

The output should be a String for whether the text is valid XML or not.
If the XML is invalid, output one of the three error strings:
1. "missing closing tag for <start_tag>"
2. "encountered closing tag without matching open tag for </end tag>"
3. "parse error"

Example 1:
Input: <a>some text</a>
Output: valid

Example 2:
Input: <a>
Output: missing closing tag for <a>
"""


def validate_xml(xml):
    stack = []

    i = 0
    while i <= len(xml) - 1:
        if xml[i] == "<":  # find tag start
            j = xml.find(">", i + 1)  # find tag end
            if j == -1:  # end not found, xxx<xxx
                return "parse error"
            if j == i + 1:  # empty tag, <>
                return "parse error"
            if "<" in xml[i + 1:j + 1]:  # another start is set between this pair, xxx<xxx<xxx>xxx
                return "parse error"

            tag = xml[i + 1:j]
            if tag[0] != "/":  # left tag, <a>
                stack.append(tag)
            else:  # right tag, </a>
                if not stack:  # isolated right tag
                    return "parse error"
                elif stack.pop() != tag[1:]:  # left/right do not match, <a> and </b>
                    return "encountered closing tag without matching open tag for <{0}>".format(tag)
            i = j + 1  # iterate after the tag end
        else:
            i += 1  # iterate at the next character

    if not bool(stack):  # all match
        return "valid"
    else:  # isolated left tag
        return "missing closing tag for <{0}>".format(stack[-1])


if __name__ == '__main__':
    xml = "2sddaq<qwe><ww></qwe>"

    print(validate_xml(xml))
