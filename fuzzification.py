class chest_pain_fuzzy:
    def __init__(self):
        self.typical_anginal= 0
        self.atypical_anginal=0
        self.non_aginal_pain=0
        self.asymptomatic=0

    def chest_pain_dic(self, x):
        if x==1: 
           self.typical_anginal=1
           self.atypical_anginal=0
           self.non_aginal_pain=0
           self.asymptomatic=0
        elif x==2:
           self.typical_anginal=0
           self.atypical_anginal=1
           self.non_aginal_pain=0
           self.asymptomatic=0
        elif x==3:
           self.typical_anginal=0
           self.atypical_anginal=0
           self.non_aginal_pain=1
           self.asymptomatic=0
           
        elif x==4:
           self.typical_anginal=0
           self.atypical_anginal=0
           self.non_aginal_pain=0
           self.asymptomatic=1
           
        return dict(typical_anginal=self.typical_anginal,atypical_anginal=self.atypical_anginal,non_aginal_pain=self.non_aginal_pain,
           asymptomatic=self.asymptomatic ) 





class sex_fuzzy:
    def __init__(self):
        self.female=0
        self.male=0
        
    def female_male_dic(self , x):
        
        if x==1: 
           self.female=1
           self.male=0
        else:
            self.female=0
            self.male=1
        return dict(female=self.female,male=self.male)


#age: ["young", "mild", "old", "very_old"]
####  y-y0=m(x-x0)
class age_fuzzy:
    
    def __init__(self):
       pass
   
    def young(self, x):
        if 0 <= x <29:
            return 1
        elif 29 <= x <38:
            return (38-x)/9
        elif 38 <= x:
            return 0
    def mild(self, x):
        if 33 <= x <=38:
            return (x-33)/5
        elif 38 < x <=45:
            return (45-x)/7
        else:
            return 0
        
    def old(self, x):
        if 40 <= x <=48:
            return (x-40)/8
        elif 48 < x <=58:
            return (58-x)/10
        else:
            return 0
        
        
    def very_old(self, x):
        if 0 <= x <52:
            return 0
        elif 52 <= x <=60:
            return (x-52)/8
        else:
            return 1 


    def age_dic(self , x):
        
        return dict(young=self.young(x),mild=self.mild(x) ,old= self.old(x) ,very_old= self.very_old(x))
    
  
  
  
  
class exercise_fuzzy:
    def __init__(self):
        self.true=0
        self.false=1
    def exercise_dic(self, x):
        if x==1: 
           self.true=1
           self.false=0
        else:
            self.true=0
            self.false=1
        return dict(true=self.true,false=self.false) 
    
    
    
#blood_pressure: ["low", "medium", "high", "very_high"]
class blood_pressure_fuzzy:
    
    def __init__(self):
        pass
    
    def low(self,x):
        if 0 <= x <111:
            return 1
        elif 111 <= x <=134:
            return (134-x)/23
        else:
            return 0
        

    def medium(self,x):
        if 127 <= x <=139:
            return (x-127)/12
        elif 139 < x <=153:
            return (153-x)/14
        else:
            return 0
        

    def high(self,x):
        if 142 <= x <=157:
            return (x-142)/16
        elif 157 < x <=172:
            return (172-x)/15
        else:
            return 0
        

    def very_high(self,x):
        if 0 <= x <=154:
            return 0
        elif 154 <= x <=171:
            return (x-154)/17
        else:
            return 1
        
        
    def blood_pressure_dic(self , x):
        
        return dict(low=self.low(x),medium=self.medium(x) ,high= self.high(x) ,very_high= self.very_high(x))


class cholestrol_fuzzy:
    
    def __init__(self):
        pass
    
    def low(self,x):
        if 0 <= x <151:
            return 1
        elif 151 <= x <=197:
            return (197-x)/46 
        else:
            return 0
        

    def medium(self,x):
        if 188 <= x <=215:
            return (x-188)/27
        elif 215 < x <=250: 
            return (250-x)/35 
        else:
            return 0
        

    def high(self,x):
        if 217 <= x <=263:
            return (x-217)/46
        elif 263 < x <=307:
            return (307-x)/44
        else:
            return 0
        

    def very_high(self,x):
        if 0 <= x <=281:
            return 0
        elif 281 <= x <=347:
            return (x-281)/66
        else:
            return 1
        
        
    def cholestrol_dic(self , x):
        
        return dict(low=self.low(x),medium=self.medium(x) ,high= self.high(x) ,very_high= self.very_high(x))

#heart_rate: ["low", "medium", "high"]


class heart_rate_fuzzy:
    
    def __init__(self):
        pass
    
    def low(self,x):
        if 0 <= x <101:
            return 1
        elif 101 <= x <=141:
            return (141-x)/40
        else:
            return 0
        

    def medium(self,x):
        if 111 <= x <=152:
            return (x-111)/41
        elif 152 < x <=194: 
            return (194-x)/42 
        else:
            return 0
        

    def high(self,x):
        if 0 <= x <=152:
            return 0
        elif 152 < x <=210:
            return (x-152)/56
        else:
            return 1
        

    
    def heart_rate_dic(self , x):
        
        return dict(low=self.low(x),medium=self.medium(x) ,high= self.high(x))


#ecg: ["normal", "abnormal", "hypertrophy"]


class ecg_fuzzy:
    
    def __init__(self):
        pass
    
    def normal(self,x):
        if  x <0:
            return 1
        elif 0 <= x <=0.4:
            return (0-x)/0.4
        else:
            return 0
        

    def abnormal(self,x):
        if 0.2 <= x <=1:
            return (x-0.2)/0.8
        elif 1 < x <=1.8: 
            return (1.8-x)/0.8 
        else:
            return 0
        

    def hypertrophy(self,x):
        if  x <=1.4:
            return 0
        elif 1.4 < x <=1.9:
            return (x-1.4)/0.5
        else:
            return 1
        

    
    def ecg_dic(self , x):
        
        return dict(normal=self.normal(x),abnormal=self.abnormal(x) ,hypertrophy= self.hypertrophy(x))


###old_peak: ["low", "risk", "terrible"]

class old_peak_fuzzy:
    
    def __init__(self):
        pass
    
    def low(self,x):
        if  x <1:
            return 1
        elif 1 <= x <=2:
            return (2-x)
        else:
            return 0
        

    def risk(self,x):
        if 1.5 <= x <=2.8:
            return (x-1.5)/1.3
        elif 2.8 < x <=4.2: 
            return (4.2-x)/1.4 
        else:
            return 0
        

    def terrible(self,x):
        if  x <=2.5:
            return 0
        elif 2.5 < x <=4:
            return (x-2.5)/1.5
        else:
            return 1
        

    
    def old_peak_dic(self , x):
        
        return dict(low=self.low(x),risk=self.risk(x) ,terrible= self.terrible(x))


###thallium_scan: ["normal", "medium", "high"]
class thallium_scan_fuzzy:
    def __init__(self):
        self.normal=0
        self.medium=0
        self.high=0
    
    def thallium_scan_dic(self, x):
        
        if x==3:
          self.normal=1
          self.medium=0
          self.high=0  
          
        elif x==6:   
          self.normal=0
          self.medium=1
          self.high=0
            
        elif x==7:
          self.normal=0
          self.medium=0
          self.high=1  
          
        return dict(normal= self.normal,medium=self.medium,high=self.high ) 
          
###blood_sugar: [true, false] 
class blood_sugar_fuzzy:
    def init(self):
        pass

    def veryHigh(self, x):
        if x <= 105:
            return 0
        if 105 <= x < 120:
            return (x-105)/15
        else:
            return 1

    def blood_sugar_dic(self, x):
        return dict(
            true=self.veryHigh(x),
            false=1 - self.veryHigh(x)
        )
        
class output_fuzzy:
    
    def __init__(self):
        pass
    def o_healthy(x):
        if x <= 0.25:
            return 1
        elif 0.25 < x < 1:
            return (1-x)/0.75
        else:
            return 0


    def o_sick1(x):
        if x <= 0 or x >= 2:
            return 0
        elif 0 < x <= 1:
            return x
        else:
            return 2-x


    def o_sick2(x):
        if x <= 1 or x >= 3:
            return 0
        elif 1 < x <= 2:
            return x-1
        else:
            return 3-x


    def o_sick3(x):
        if x <= 2 or x >= 4:
            return 0
        elif 2 < x <= 3:
            return x-2
        else:
            return 3-x


    def o_sick4(x):
        if x <= 3:
            return 0
        elif 3 < x <= 3.75:
            return (x-3) /0.75
        else:
            1


    def output_dic(x):
        output = {
            'healthy': o_healthy(x),
            'sick_1': o_sick1(x),
            'sick_2': o_sick2(x),
            'sick_3': o_sick3(x),
            'sick_4': o_sick4(x)
        }
        return output