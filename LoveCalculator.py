def calculate_love_score(x,y):
    str1=list(x.upper()+y.upper())
    lis=["TRUE","LOVE"]
    strr=""
    count=0
    total=0
    for word in lis:
        for K in word:
            for x in str1:
                if K in x:
                    count+=1
                    total+=1
                else:
                    count = count
            print(f"{K} occours {count} times")
            count=0
        print(f"Total = {total}")
        strr=strr+str(total)
        total=0
    print(strr)
calculate_love_score("Jack Sparrow","Angelina")
