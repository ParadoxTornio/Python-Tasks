import math

n = input()
stack = []
tokens = n.split()
for token in tokens:
    if token.isdigit():
        stack.append(int(token))
    else:
        match token:
            case '+':
                num1 = stack[-2]
                num2 = stack[-1]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(num1 + num2)
            case '-':
                num1 = stack[-2]
                num2 = stack[-1]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(num1 - num2)
            case '*':
                num1 = stack[-2]
                num2 = stack[-1]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(num1 * num2)
            case '/':
                num1 = stack[-2]
                num2 = stack[-1]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(num1 // num2)
            case '~':
                num1 = stack[-1]
                stack.pop(-1)
                stack.append(-num1)
            case '!':
                num1 = stack[-1]
                stack.pop(-1)
                stack.append(math.factorial(num1))
            case '#':
                num1 = stack[-1]
                stack.append(num1)
            case '@':
                num1 = stack[-3]
                num2 = stack[-2]
                num3 = stack[-1]
                stack.pop(-1)
                stack.pop(-1)
                stack.pop(-1)
                stack.append(num2)
                stack.append(num3)
                stack.append(num1)

print(stack[0])
