line = input()
minutes = int(input())
seconds = int(input())
total_time = 0
text = ""
while line != "Finish":
    total_time = minutes*60 + seconds
    if total_time < 55:
        text = "Gold"
    elif 55 <= total_time <= 85:
        text = "Silver"

    elif 85 < total_time <= 120:
        text = "Bronze"

    line = input()
    minutes = int(input())
    seconds = int(input())






