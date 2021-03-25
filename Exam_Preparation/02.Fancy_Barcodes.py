import re
n = int(input())
regex = r"@#+([A-Z][a-zA-Z\d]{4,}[A-Z])@#+"


for i in range(n):
    line = input()
    if re.findall(regex, line):
        digits = re.findall(r"\d", line)
        if digits:
            print(f"Product group: {''.join(digits)}")
        else:
            print(f"Product group: 00")
    else:
        print(f"Invalid barcode")






