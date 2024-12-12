def month_to_season(month):
    
    if not 1 <= month <= 12:
        return "Invalid month number."

    if 3 <= month <= 5:
        return "Весна"
    elif 6 <= month <= 8:
        return "Лето"
    elif 9 <= month <= 11:
        return "Осень"
    else:
        return "Зима"


print(month_to_season(2))  
print(month_to_season(5))  
print(month_to_season(8))  
print(month_to_season(11)) 
print(month_to_season(13)) 