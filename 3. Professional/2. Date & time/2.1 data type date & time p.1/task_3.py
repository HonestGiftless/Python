# Floride

# Считайте, что переменная florida_hurricane_dates объявлена и доступна вашей программе.

early_hurricanes = 0

for hurricane in florida_hurricane_dates:
    if hurricane.month < 6:
        early_hurricanes += 1

print(early_hurricanes)