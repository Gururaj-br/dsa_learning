s = "python is easy language"

output = []

temp_ch = ""
for i in range(len(s)):
    if s[i].isalnum():
        temp_ch+=s[i]
        i+=1
    else:
        output.append(temp_ch)
        temp_ch = ""
        i+=1
output.append(temp_ch)
print(output[::-1])

# for char in s:
#     import ipdb;ipdb.set_trace()

#     temp_ch = ""
#     if char.isalnum():
#         temp_ch+=char
#     else:
#         import ipdb;ipdb.set_trace()
#     output.append(temp_ch)

# print(output)