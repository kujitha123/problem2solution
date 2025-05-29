def generate_parentheses(ind, curr_str, o, c, ans, n):
    if o > n:
        return
    if ind == 2 * n and o == c:
        ans.append(curr_str)
        return
    if o < n:
        generate_parentheses(ind + 1, curr_str + "(", o + 1, c, ans, n)
    if c < o:
        generate_parentheses(ind + 1, curr_str + ")", o, c + 1, ans, n) 
    return ans
n = int(input("Enter the number of pairs of parentheses: "))
ind = 0
o = 0
c = 0
curr_str = " "
ans = []
print(generate_parentheses(ind, curr_str, o, c, ans, n))

