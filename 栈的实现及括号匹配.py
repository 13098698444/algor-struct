
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
    def pop(self):         
        return self.stack.pop()
    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            raise IndexError('栈是空的, 你个傻逼')
    def is_empty(self):
        return len(self.stack) == 0
# stack = Stack()
# stack.push(1)
# stack.push(5)
# stack.pop()
# stack.pop()
# print(stack.get_top())
"""
eg:
()[]{}
"""
def Brace_match(s):
    match = {'}':'{', ']':'[', ')':'('}
    stack = Stack()
    for i in s:
        if i in {'(', '{', '['}:
            stack.push(i)
        else:   # i 在'}'  ']'   ')'
            if stack.is_empty():
                return False
            elif stack.get_top() == match[i]:
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False

print(Brace_match('{[([])]}[[[([([])])]][][]]([])'))


#法二
s = '[(({{]]'
while '{}' in s or '()' in s or '[]' in s:
        s = s.replace('{}', '')
        s = s.replace('[]', '')
        s = s.replace('()', '')
print(s == '')