def solution(arrangement):
    stack = []  # empty stack
    answer = 0
    new = arrangement.replace('()', 'c')  # replace '()' as 'c'
    for p in new:
        if p == '(':  # new stick
            stack.append(p)  # add to stack
            answer += 1  # increase number of sticks
        elif p == ')':  # end of stick
            stack.pop()
        else:  # 'c', cut stick
            answer += len(stack)  # double number of current sticks

    return answer

print(solution('()(((()())(())()))(())'))