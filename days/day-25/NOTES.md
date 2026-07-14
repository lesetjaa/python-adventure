# NOTES

## CSV - Comma Seperated Values

```python
with open("../resources/weather_data.csv", mode="r") as file:
    data = file.readlines()
    print(data)
```

```sh
# output

['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']
```

**Working with csv files**

- Using `with open()` makes things difficult for us to extract each row or column csv files
- Therefore we can use an inbuilt python library called csv

**How to use the csv library**

- We import the `csv` library
- Then we use the reader method to create an object for the data so we can loop through the data and get each row

```python
import csv

with open("../resources/weather_data.csv", mode="r") as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(row)
```

```sh
# output

['day', 'temp', 'condition']
['Monday', '12', 'Sunny']
['Tuesday', '14', 'Rain']
['Wednesday', '15', 'Rain']
['Thursday', '14', 'Cloudy']
['Friday', '21', 'Sunny']
['Saturday', '22', 'Sunny']
['Sunday', '24', 'Sunny']
```

**Note**

- we can use `next(data)` to skip the first row!

## To make it more efficient in reading and writing data we need Pandas library

## Pandas

- With Pandas we do not have to `open()` the csv file

```python
import pandas

data = pandas.read_csv(<file path>)
print(data)
```

```sh
# output

         day  temp condition
0     Monday    12     Sunny
1    Tuesday    14      Rain
2  Wednesday    15      Rain
3   Thursday    14    Cloudy
4     Friday    21     Sunny
5   Saturday    22     Sunny
6     Sunday    24     Sunny
```

**Pandas DataTypes**

```python
import pandas

data = pandas.read_csv("../resources/weather_data.csv")
print(type(data))
print(type(data["temp"]))
```

```sh
# output
<class 'pandas.DataFrame'>
<class 'pandas.Series'>
```

- We have two types of data objects of pandas, Series and DataFrame
- This data type in `weather_data.csv` is called `DataFrame`, the equivilent of the whole table
- The `Series` data type is a single column in the table

### Get Data in Columns

```python

data["condition"]
data.condition
```

### Get Data in Rows

```python

# To get the Monday data (row)
data[data.day == "Monday"]
```

### TO create a dataframe from scratch

```python
import pandas

data_dict = {
    "student": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv") # path to csv file we want to save
```

**Note from comment section**

- The only possible issue with your solution is that the resulting csv file wont feature numerical indices in the first column. To fix that you can add "color_occurrence = color_occurrence.reset_index()" between the 7th and 8th rows.
