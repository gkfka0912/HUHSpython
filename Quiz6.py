def std_weight(fheight, fgender):
    if fgender=="male":
        fweight=fheight*fheight*22
        return fweight

    if fgender=="female":
        fweight=fheight*fheight*21
        return fweight
    
height=float(input("키 : "))
gender=input("성별(male, female) : ")
weight=round(std_weight(height, gender)/10000,2)
if gender=="male":
    print("키",height,"남자의 표준 체중은",weight,"입니다.")
if gender=="female":
    print("키",height,"여자의 표준 체중은",weight,"입니다.")