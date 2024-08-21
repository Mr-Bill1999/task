s = '(a+b-(a+c))'

def check(string):
    stack = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == ')':
           if s[i] == '(':
               stack.append(s[i])
           else:
               if stack == [] or stack[len(stack)-1] != stack[len(stack)-2]:
                   return False
               else:
                   stack.pop()
    if stack:
        return False
    else:
        return True


print(check(s))