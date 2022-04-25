import openpyxl as xl
import re as regex

workbook = xl.Workbook()
sheet = workbook.active
workbook.save("akkhor.xlsx")

# file = open('2.txt', 'r')
# f = file.readlines()
question_flag = False
ko_option_flag = False
kho_option_flag = False
go_option_flag = False
gho_option_flag = False
answer_flag = False
definition_flag = False
question = ""
option = ""

with open('2.txt', 'r') as file:
    for line in file:
        # print(line)
        if line == "৩.১ এবং ৩.২ অর্থ সমমূল্যের ধারণা ও গুরুত্ব:\n":
            break
        for word in line.split():

            # question
            if regex.search("[০-৯৯]।", word):
                # print(word)
                # raise a question flag
                gho_option_flag = False
                print(option)
                option = ""
                question_flag = True
                # continue

            # options
            ko = ""
            kho = ""
            go = ""
            gho = ""

            if word == "(ক)":
                question_flag = False
                print(question)
                question = ""
                ko_option_flag = True
                # continue

                # print("ko")

            if word == "(খ)":
                # print("kho")
                ko_option_flag = False
                print(option)
                option = ""
                kho_option_flag = True
                # continue

            if word == "(গ)":
                kho_option_flag = False
                print(option)
                option = ""
                go_option_flag = True
                # continue

            if word == "(ঘ)":
                go_option_flag = False
                print(option)
                option = ""
                gho_option_flag = True
                # continue

            if question_flag:
                question += " " + word
            if ko_option_flag:
                option += " " + word
            if kho_option_flag:
                option += " " + word
            if go_option_flag:
                option += " " + word
            if gho_option_flag:
                option += " " + word

# print(f)
# i = 0
# row = 1
# column = 1
# while i != 11:
#     # add question
#     x = ""
#     if regex.search("[০-৫০০]।", f[i]):
#         x = regex.sub("[০-৫০০]।", "", f[i])
#         i = i + 1
#     if()
#     while f[i].find("(") == -1:
#         print(f[i])
#         x += f[i]
#         i = i + 1
#     sheet.cell(row, column, x)
#     # if regex.search("[()]", f[i]):
#
#     # if regex.search()
#     row += 1
#     i += 1
#     workbook.save('akkhor.xlsx')
#     if i >= len(f):
#         break
