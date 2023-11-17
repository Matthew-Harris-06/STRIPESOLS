def decodeString(s):
        curr_num = 0
        res = ""
        stack = []
        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c == '[':
                stack.append(curr_num)
                stack.append(res)
                curr_num = 0
                res = ""
            elif c == ']':
                res = stack.pop() + res * stack.pop()
            else:
                res += c
        
        return res
print(decodeString("3[a]2[bc]4[2[cc]]"))
