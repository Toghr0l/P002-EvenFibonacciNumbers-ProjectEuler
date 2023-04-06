def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False


first = 1
seccond = 2
total = 0

while first < 4000000:
    if isEven(first):
        total += first
    new = first + seccond
    first = seccond
    seccond = new

print(total)