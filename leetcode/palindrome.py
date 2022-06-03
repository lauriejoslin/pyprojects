head = [1, 2, 3, 4, 3, 2, 1]
def isPalindrome(ls):
    length = int(len(ls) / 2)
    cap = len(ls) -1
    while length < cap:
        if ls[length] != ls[-length-1]:
            return False
        else:
            length += 1
    return True
print(isPalindrome(head))


