def isValid(self, s):
    stack = []
    mapping = {
        ")":"(",
        "]":"[",
        "}":"{"
    }

    for item in s:
        if item in "({[":
            stack.append(item)
        elif item in "]})":
            if stack:
                if mapping[item] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
    return len(stack) == 0