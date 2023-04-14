import json

# first_date = datetime.datetime.now()
# print(first_date)

emergency = input("Input Emergency: ")
description = input("Input Description: ")
area = input("Input Area: ")
startDate = input("Input StartDate: ")
endDate = input("Input EndDate: ")

data = {"emergency": emergency, "description": description,
        "area": area, "startDate": startDate, "endDate": endDate}
tmp = []
# .dumps() as a string
with open("./json_data.json", 'r+', encoding='utf8') as outfile:
    tmp = json.load(outfile)
    tmp.append(data)
    outfile.seek(0)
    json.dump(tmp, outfile)

# second_date = datetime.datetime.now()
# print(second_date)


# difference_in_seconds = (second_date - first_date).total_seconds()
# print(difference_in_seconds)

# print(f"First Date: {first_date} \nSecond Date: {second_date} \nSeconds Difference: {difference_in_seconds}")
