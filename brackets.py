# 定义一个函数，可以替换String中特定位置的字符
def replace_char_at_index(s, index, new_char):
    if index < 0 or index >= len(s):
        return s
    return s[:index] + new_char + s[index+1:]

def check_brackets(s):
    stack = []
    result = ''
    i = 0 # String中每个字符的index

    # 遍历字符串
    for char in s: 
        if char == '(': # 若为左括号，将该左括号在字符串中的位置入栈
            stack.append(i)
            result += ' '
        elif char == ')': # 若为右括号，检查栈中是否有能与之匹配的左括号
            if stack:
                stack.pop()
                result += ' '
            else:
                result += '?'
        else:
            result += ' '
        i += 1
    
    if len(stack) > 0: # 遍历完字符串后，若栈不为空，说明有未匹配的左括号
        for j in range(len(stack)):
            # 将结果中，多余左括号的对应位置替换为“x”
            result = replace_char_at_index(result, stack[j], "x")

    return result

test_cases = [
    "bge)))))))))",
    "((IIII)))))))",
    "()()()()(uuu",
    "))))UUUU((()",
]

for test_case in test_cases:
    print(test_case)
    print(check_brackets(test_case))
    print('')
