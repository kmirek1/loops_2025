# Loops video  https://www.youtube.com/watch?v=KWgYha0clzw&t=1s&pp=ygUOYnJvIGNvZGUgbG9vcHM%3D
# While loops  
# for loops = excute block of code a fixed number of times
# you can iterate over a range, string, sequence, etc.

# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)


for x in range(1,21):
    if x== 13:
        continue
    else:
        print(x)

for x in range(1,21):
    if x== 13:
        break
    else:
        print(x)