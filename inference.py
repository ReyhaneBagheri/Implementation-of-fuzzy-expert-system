
import fuzzification

def rules(chest_pain,blood_pressure,cholesterol,blood_sugar,ECG,maximum_heart_rate,exercise,old_peak,thallium,sex,age):
       sick_1 = []
       sick_2 = []
       sick_3 = []
       sick_4 = []
       healthy= []
       
       sick_4.append(min(fuzzification.age_fuzzy().age_dic(age)['very_old'],fuzzification.chest_pain_fuzzy().chest_pain_dic(chest_pain)['atypical_anginal']))
       sick_4.append(min(fuzzification.heart_rate_fuzzy().heart_rate_dic(maximum_heart_rate)['high'],fuzzification.age_fuzzy().age_dic(age)['old']))
       sick_3.append(min(fuzzification.sex_fuzzy().female_male_dic(sex)['male'],fuzzification.heart_rate_fuzzy().heart_rate_dic(maximum_heart_rate)['medium']))
       sick_2.append(min(fuzzification.sex_fuzzy().female_male_dic(sex)['female'],fuzzification.heart_rate_fuzzy().heart_rate_dic(maximum_heart_rate)['medium']))
       sick_3.append(min(fuzzification.chest_pain_fuzzy().chest_pain_dic(chest_pain)['non_aginal_pain'],fuzzification.blood_pressure_fuzzy().blood_pressure_dic(blood_pressure)['high']))
       sick_2.append(min(fuzzification.chest_pain_fuzzy().chest_pain_dic(chest_pain)['typical_anginal'],fuzzification.heart_rate_fuzzy().heart_rate_dic(maximum_heart_rate)['medium']))
       sick_3.append(min(fuzzification.blood_sugar_fuzzy().blood_sugar_dic(blood_sugar)['true'],fuzzification.age_fuzzy().age_dic(age)['mild']))
       sick_2.append(min(fuzzification.blood_sugar_fuzzy().blood_sugar_dic(blood_sugar)['false'],fuzzification.blood_pressure_fuzzy().blood_pressure_dic( blood_pressure)['very_high']))
       sick_1.append(max(fuzzification.chest_pain_fuzzy().chest_pain_dic(chest_pain)['asymptomatic'],fuzzification.age_fuzzy().age_dic(age)['very_old']))
       sick_1.append(max(fuzzification.blood_pressure_fuzzy().blood_pressure_dic(blood_pressure)['high'],fuzzification.heart_rate_fuzzy().heart_rate_dic(maximum_heart_rate)['low']))
       healthy.append(fuzzification.chest_pain_fuzzy().chest_pain_dic(chest_pain)['typical_anginal'])
       sick_1.append(fuzzification.chest_pain_fuzzy().chest_pain_dic(chest_pain)['atypical_anginal'])
       sick_2.append(fuzzification.chest_pain_fuzzy().chest_pain_dic(chest_pain)['non_aginal_pain'])
       sick_3.append(fuzzification.chest_pain_fuzzy().chest_pain_dic(chest_pain)['asymptomatic'])
       sick_4.append(fuzzification.chest_pain_fuzzy().chest_pain_dic(chest_pain)['asymptomatic'])
       sick_1.append(fuzzification.sex_fuzzy().female_male_dic(sex)['female'])
       sick_2.append(fuzzification.sex_fuzzy().female_male_dic(sex)['male'])
       healthy.append(fuzzification.blood_pressure_fuzzy().blood_pressure_dic(blood_pressure)['low'])
       sick_1.append(fuzzification.blood_pressure_fuzzy().blood_pressure_dic(blood_pressure)['medium'])
       sick_2.append(fuzzification.blood_pressure_fuzzy().blood_pressure_dic(blood_pressure)['high'])
       sick_3.append(fuzzification.blood_pressure_fuzzy().blood_pressure_dic(blood_pressure)['high'])
       sick_4.append(fuzzification.blood_pressure_fuzzy().blood_pressure_dic(blood_pressure)['very_high'])
       healthy.append(fuzzification.cholestrol_fuzzy().cholestrol_dic(cholesterol)['low'])
       sick_1.append(fuzzification.cholestrol_fuzzy().cholestrol_dic(cholesterol)['medium'])
       sick_2.append(fuzzification.cholestrol_fuzzy().cholestrol_dic(cholesterol)['high'])
       sick_3.append(fuzzification.cholestrol_fuzzy().cholestrol_dic(cholesterol)['high'])
       sick_4.append(fuzzification.cholestrol_fuzzy().cholestrol_dic(cholesterol)['very_high'])
       sick_2.append(fuzzification.blood_sugar_fuzzy().blood_sugar_dic(blood_sugar)['true'])
       healthy.append(fuzzification.ecg_fuzzy().ecg_dic(ECG)['normal'])
       sick_1.append(fuzzification.ecg_fuzzy().ecg_dic(ECG)['normal'])
       sick_2.append(fuzzification.ecg_fuzzy().ecg_dic(ECG)['abnormal'])
       sick_3.append(fuzzification.ecg_fuzzy().ecg_dic(ECG)['hypertrophy'])
       sick_4.append(fuzzification.ecg_fuzzy().ecg_dic(ECG)['hypertrophy'])
       healthy.append(fuzzification.heart_rate_fuzzy().heart_rate_dic(maximum_heart_rate)['low'])
       sick_1.append(fuzzification.heart_rate_fuzzy().heart_rate_dic(maximum_heart_rate)['medium'])
       sick_2.append(fuzzification.heart_rate_fuzzy().heart_rate_dic(maximum_heart_rate)['medium'])
       sick_3.append(fuzzification.heart_rate_fuzzy().heart_rate_dic(maximum_heart_rate)['high'])
       sick_4.append(fuzzification.heart_rate_fuzzy().heart_rate_dic(maximum_heart_rate)['high'])
       sick_2.append(fuzzification.exercise_fuzzy().exercise_dic(exercise)['true'])
       healthy.append(fuzzification.old_peak_fuzzy().old_peak_dic(old_peak)['low'])
       sick_1.append(fuzzification.old_peak_fuzzy().old_peak_dic(old_peak)['low'])
       sick_2.append(fuzzification.old_peak_fuzzy().old_peak_dic(old_peak)['terrible'])
       sick_3.append(fuzzification.old_peak_fuzzy().old_peak_dic(old_peak)['terrible'])
       sick_4.append(fuzzification.old_peak_fuzzy().old_peak_dic(old_peak)['risk'])
       healthy.append(fuzzification.thallium_scan_fuzzy().thallium_scan_dic(thallium)['normal'])
       sick_1.append(fuzzification.thallium_scan_fuzzy().thallium_scan_dic(thallium)['normal'])
       sick_2.append(fuzzification.thallium_scan_fuzzy().thallium_scan_dic(thallium)['medium'])
       sick_3.append(fuzzification.thallium_scan_fuzzy().thallium_scan_dic(thallium)['high'])
       sick_4.append(fuzzification.thallium_scan_fuzzy().thallium_scan_dic(thallium)['high'])
       healthy.append(fuzzification.age_fuzzy().age_dic(age)['young'])
       sick_1.append(fuzzification.age_fuzzy().age_dic(age)['mild'])
       sick_2.append(fuzzification.age_fuzzy().age_dic(age)['old'])
       sick_3.append(fuzzification.age_fuzzy().age_dic(age)['old'])
       sick_4.append(fuzzification.age_fuzzy().age_dic(age)['very_old'])
       output=dict(
            outputsick_sick1=max(sick_1),
            outputsick_sick2=max(sick_2),
            outputsick_sick3=max(sick_3),
            outputsick_sick4=max(sick_4),
            outputsick_healthy=max(healthy)
        )
       return output