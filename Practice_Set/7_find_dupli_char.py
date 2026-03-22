# ============= Find Duplicate Character ===============
word = "Programmingr"

# for i in range(len(word)):
#     for j in range(i+1,len(word)):
#         if word[i] == word[j]:
#             is_duplicate = False
#             for k in range(i):
#                 if word[i] == word[k]:
#                     is_duplicate = True
#                     break
#             if not is_duplicate:
#                 print("Duplicate : ",word[i])


# ------ Method 2 -----
visited = ""
for i in range(len(word)):
    for j in range(i+1, len(word)):
        if word[i] == word[j] and word[i] not in visited:
            print("Duplicae : ", word[i])
            visited += word[i]
