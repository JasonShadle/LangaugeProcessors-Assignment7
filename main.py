def postfix(tokens):

    stack = []
    output = []
    for token in tokens:
        # check if it is number or character (variable)
        if token.isalnum():
            output.append(token)
        else:
            # if is left parenthesis, always pop
            if token == '(':
                stack.append(token)
            if token == ')':
                # pop everything until closing parenthesis
                while stack[len(stack) - 1] != '(':
                    output.append(stack.pop())
                # get rid of left parenthesis
                stack.pop()
            if token in '*/':
                if len(stack) == 0:
                    stack.append(token)
                # if operator is less precedence -> add it
                elif stack[len(stack) - 1] in '+-':
                    stack.append(token)
                # if operator is same precedence -> pop then add token
                elif stack[len(stack) - 1] in '*/':
                    output.append(stack.pop())
                    stack.append(token)
                else:
                    stack.append(token)

            if token in '+-':
                # if stack is empty, always add it
                if len(stack) == 0:
                        stack.append(token)
                else:
                    while 1 == 1:
                        if len(stack) > 0:
                            # if last index is another operator, have to pop until no more
                            if stack[len(stack) - 1] in '+-*/':
                                output.append(stack.pop())
                            else:
                                # if not, no need to check again
                                break
                        else:
                            break
                    stack.append(token)
    # once all tokens are used, pop rest of stack to output
    while len(stack) != 0:
        output += stack.pop()
    return output

def printLineCode(i,z):
    a = open('output.txt', 'a')
    temps = 0
    line = i

    x = 0
    if len(line) == 1:
        if line[0].isdigit():
            a.write('LDA #' + line[0] + '\n')
        else:
            a.write('LDA ' + line[0] + '\n')
        a.write('STA ' + z)
    else:
        while len(line) != 1:
            if len(line) == 1:
                break;
            else:
                if line[x+2] in "+-*/":
                    op = line[x+2]
                    num1 = '' + line[x]
                    num2 = '' + line[x+1]
                    placehold = ''

                    if num2.isdigit():
                        placehold = '#'

                    if num1.isdigit():
                        a.write('LDA #' + num1 + '\n')
                    else:
                        a.write('LDA ' + num1 + '\n')

                    if op == '+':
                        a.write('ADD ' + placehold + num2 + '\n')
                    elif op == '-':
                        a.write('SUB ' + placehold + num2 + '\n')
                    elif op == '*':
                        a.write('MUL ' + placehold + num2 + '\n')
                    else:
                        a.write('DIV ' + placehold + num2 + '\n')

                    a.write('STA temp' + str(temps) + '\n')
                    b = 1
                    # replace current spot, pop the next 2
                    line[x] = 'temp' + str(temps)
                    temps += 1
                    line.pop(x + 1)
                    # note: after popping first element, second one replaces that index
                    line.pop(x + 1)
                    x = 0
                else:
                    x += 1

        a.write('LDA temp' + str(temps - 1) + '\n')
        a.write('STA ' + z + '\n')
        a.close()


# erase output file
open('output.txt', 'w').close()
totalTemp = 0
file = open('input.txt', 'r')
variables = []
for line in file:
    # remove trailing ;
    line = line.strip()
    line = line[0:-1]
    # split by space into array
    tokens = line.split(" ")
    # pass tokens past the equals sign
    variables.append(tokens[0])
    postList = postfix(tokens[tokens.index('=') + 1: len(tokens)])

    # check to see how many total temp variables will be used
    ops = 0
    for token in postList:
        if token in '+-*/':
            ops += 1
    if ops > totalTemp:
        totalTemp = ops

    printLineCode(postList, line[0])
file.close()

output = open('output.txt', 'a')
for v in variables:
    output.write(v + ' RESW 1' + '\n')
for z in range(0,totalTemp):
    output.write('temp' + str(z) + ' RESW 1' + '\n')
output.close()
