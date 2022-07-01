from scipy.integrate import quad as q

def mohasebeantegral(mini , maxi ,a , b):
    step=0.0001
    i=mini
    n1=0
    nn1=0.0
    while i<maxi:
        n1+=(i*(a*i+b))*step
        nn1+=(a*i+b)*step
        i+=step
    return n1,nn1


def center_(output_):
    array1=[]
    array2=[]
    array3=[]
    array4=[]
    array5=[]
    n=0
    dn=0
    #فعال بودن 
    if(output_['outputsick_healthy']>0):
        array1=health_def(output_['outputsick_healthy'])
        n+=array1[0]
        dn+=array1[1]
        print(array1)
    if(output_['outputsick_sick1']>0):
        array2=sick1_def(output_['outputsick_sick1'])
        n+=array2[0]
        dn+=array2[1]
        print(array2)
    if(output_['outputsick_sick2']>0):
        array3=sick2_def(output_['outputsick_sick2'])
        n+=array3[0]
        dn+=array3[1]
        print(array3)
    if(output_['outputsick_sick3']>0):
        array4=sick3_def(output_['outputsick_sick3'])
        n+=array4[0]
        dn+=array4[1]
        print(array4)
    if(output_['outputsick_sick4']>0):
        array5=sick4_def(output_['outputsick_sick4'])
        n+=array5[0]
        dn+=array5[1]
        print(array5)
        
    center= n/dn
    #print(center)
    #print(n)
    #print(dn)
    
    return center


def health_def(value):
    #y=ax+b
    a=(0 - 1) / (1 - 0.25)
    b= - a
    #if value is 1 and all dagram compute for defuzzy
    if(value==1):
        n1,dn1=mohasebeantegral(0, 0.25, 0, 1)
        n2,dn2=mohasebeantegral(0.25,1, a, b)
        return (n1+n2),(dn1+dn2)
       
    else:
        n1,dn1=mohasebeantegral(0, (value-b)/a , 0, value)
        n2,dn2=mohasebeantegral((value-b)/a ,1, a, b)
        return (n1+n2),(dn1+dn2)   
       
        
   



def sick4_def(value):
    #y=ax+b
    a=(1 - 0) / (3.75 - 3)
    b= -4
    #if value is 1 and all dagram compute for defuzzy
    if(value==1):
        n1,dn1=mohasebeantegral(3.75, 4, 0, 1)
        n2,dn2=mohasebeantegral(3,3.75, a, b)
        return (n1+n2),(dn1+dn2)
       
    else:
        n1,dn1=mohasebeantegral((value-b)/a , 4, 0, value)
        n2,dn2=mohasebeantegral(3 , (value-b)/a , a, b)
        return (n1+n2),(dn1+dn2)   
       
        

    


def sick1_def(value):
    #y=ax+b
    a1=1   #(1 - 0) / (1-0)
    b1= 0
    a2= -1 #(1 - 0) / (1 - 2)
    b2= 2
    
    #if value is 1 and all dagram compute for defuzzy
    if(value==1):
        n1,dn1=mohasebeantegral(0, 1, a1, b1)
        n2,dn2=mohasebeantegral(1,2, a2, b2)
        return (n1+n2),(dn1+dn2)
       
    else:
        n1,dn1=mohasebeantegral(0, (value-b1)/a1 , a1, b1)
        n2,dn2=mohasebeantegral((value-b2)/a2 , 2 , a2, b2)
        n3,dn3=mohasebeantegral((value-b1)/a1 ,(value-b2)/a2 , 0 , value)
        return (n1+n2+n3),(dn1+dn2+dn3)   
       
        

    
def sick2_def(value):
    #y=ax+b
    a1=1
    #(1 - 0) / (2 - 1)
    b1= -1
    a2= -1
    #(0 - 1) / (3 - 2)
    b2= 3
    
    #if value is 1 and all dagram compute for defuzzy
    if(value==1):
        n11,dn11=mohasebeantegral(1, 2, a1, b1)
        n22,dn22=mohasebeantegral(2,3, a2, b2)
        return (n11+n22),(dn11+dn22)
       
    else:
        n1,dn1=mohasebeantegral(1, (value-b1)/a1 , a1, b1)
        n2,dn2=mohasebeantegral((value-b2)/a2 , 3 , a2, b2)
        n3,dn3=mohasebeantegral((value-b1)/a1 ,(value-b2)/a2 , 0 , value)
        return (n1+n2+n3),(dn1+dn2+dn3)   



    
def sick3_def(value):
    #y=ax+b
    a1=1
    #(1 - 0) / (3 - 2)
    b1= -2
    a2=-1
    #(0 - 1) / (4 - 3)
    b2= 4
    
    #if value is 1 and all dagram compute for defuzzy
    if(value==1):
        n11,dn11=mohasebeantegral(2, 3, a1, b1)
        n22,dn22=mohasebeantegral(3 ,4, a2, b2)
        return (n11+n22),(dn11+dn22)
       
    else:
        n1,dn1=mohasebeantegral(2, (value-b1)/a1 , a1, b1)
        n2,dn2=mohasebeantegral((value-b2)/a2 , 4 , a2, b2)
        n3,dn3=mohasebeantegral((value-b1)/a1 ,(value-b2)/a2 , 0 , value)
        return (n1+n2+n3),(dn1+dn2+dn3)   
       
        

    

def defuzzification(output_):
    center=center_(output_)
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


#print(defuzzification(dict(outputsick_sick1= 1.0, outputsick_sick2= 1, outputsick_sick3= 0.5714285714285714, outputsick_sick4= 0.32142857142857145, outputsick_healthy= 1)))

#{'outputsick_sick1': 1.0, 'outputsick_sick2': 1, 'outputsick_sick3': 0.5714285714285714, 'outputsick_sick4': 0.32142857142857145, 'outputsick_healthy': 1}