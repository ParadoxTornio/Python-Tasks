n = input()
stack = []
tokens = n.split()
for token in tokens:
    if token.isdigit():
        stack.append(int(token))
    else:
        num1 = stack[-2]
        num2 = stack[-1]
        stack.pop(-1)
        stack.pop(-1)
        match token:
            case '+':
                stack.append(num1 + num2)
            case '-':
                stack.append(num1 - num2)
            case '*':
                stack.append(num1 * num2)

print(stack[0])
