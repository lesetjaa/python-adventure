# TODO - Use the squirrel data to create a csv file, counting the number of squirrels fur color 

import pandas

raw_data = pandas.read_csv("../resources/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_occurrence = raw_data["Primary Fur Color"].value_counts()

color_occurrence = color_occurrence.reset_index()
color_occurrence.to_csv("../resources/squirrel_count.csv")

# squirrel_count_data = {
#     "Fur Color": ["grey", "red", "black"],
#     "Count": [grey_occ, red_occ, black_occ]
# }
# new_data = pandas.DataFrame(squirrel_count_data)
# new_data.to_csv("../resources/squirrel_count.csv")