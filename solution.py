def is_balanced(s):
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0


# Taking input
string = input("Enter brackets: ")

if is_balanced(string):
    print("Balanced")
else:
    print("Not Balanced")
