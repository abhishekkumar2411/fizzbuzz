    file1 = open("BOOK1.txt", "r")
    file2 = open("BOOK2.txt", "r")
    file3 = open("BOOK3.txt", "r")
    file4 = open("20k.txt", "r")
    file5 = open("book1uniquelist", "a")
    file6= open("book2uniquelist", "a")
    file7= open("book3uniquelist", "a") 
    file8= open("rarelist", "a")
    list1 = file1.readlines().split()
    list2 = file2.readlines().split()
    list3 = file3.readlines().split()
    list4 = file4.readlines().split()
