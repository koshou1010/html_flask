list = [1,2,3,4,5,6,7,8,9,0]
tmplist = []
tmplist2 = []
for i in list:
    if i % 2 == 0:
        tmplist.append(i)
    else:
        tmplist2.append(i)
finallist = tmplist + tmplist2
print(finallist)
