def defuzzification(center):
    
    a=[]
    str1=''
    if center < 1.78:
        a.append('healthy')
    if 1 <= center <= 2.51:
        if len(a) > 0:
            a.append(' & sick1')
        else :
            a.append('sick1')
    if 1.78 <= center <= 3.25:
        if len(a) > 0:
            a.append(' & sick2')
        else:
            a.append('sick1')
    if 1.5 <= center <= 4.5:
        if len(a) > 0:
            a.append(' & sick3')
        else:
            a.append('sick3')
    if center > 3.25:
        if len(a) > 0:
            a.append(' & sick4')
        else:
            a.append('sick4')
    a.append(' : ')
    a.append(str(center))
    for i in a :
        str1+=i
    return str1

print(defuzzification(1.25))