n = int(input())
dividend = 1
unique_div = []
out = ""

while not (dividend in unique_div):
    unique_div.append(dividend)
    out += str(dividend // n)
    dividend = (dividend % n) * 10

print(out[unique_div.index(dividend):])
