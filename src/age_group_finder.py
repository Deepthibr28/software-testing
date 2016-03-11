def find(age):
    if age in range(0,3):
        age_group = "Baby"
    elif age in range(3,6):
        age_group = "Toddler"
    elif age >= age in range(6,13):
        age_group = "Children"
    elif age in range(13,20):
        if(age==18 or age ==19):
            age_group = "Teen and Young adult"
        else:
            age_group = "Teen"
    elif age in range(18,25):
        age_group = "Young adult"
    elif age in range(25,65):
        age_group = "Adult"
    else:
        age_group = "Old"
    return age_group