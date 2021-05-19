def cal_BMR(gender, weight, height, age):
    BMR = 0.0
    if gender.lower() == 'male':
        BMR = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
    elif gender.lower() == 'female':
        BMR = 665 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
    else:
        BMR = None
    return BMR