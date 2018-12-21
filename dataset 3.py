import re
import plotly
import plotly.graph_objs as go
from plotly import tools
import csv
try:

    with open("D:/data/results.txt", encoding="utf-8", mode='r') as file:

        csv_reader = csv.reader(file, delimiter=',')

        line_number = 0

        for row in csv_reader:
            #print(row)

            line_number += 1
except IOError as e:

    print("I/O error({0}): {1}".format(e.errno, e.strerror))
except ValueError as ve:

    print("Value error {0} in line {1}".format(ve, line_number))
def getElement(line):
    result = re.split(r',', line, maxsplit=1)

    element = result[0].strip()

    return element, result[1]
def getDate(line):
    result = re.split(r',', line, maxsplit= 1)
    date = re.findall(r'\d{4}\d{0,2}\d{0,2}', result[0])[0]
    return date, result[1]
def getHome_team(line):
    home_team, line = getElement(line)
    home_team = home_team[0].upper() + home_team[1:].lower()

    return home_team, line
def getAway_team(line):
    away_team, line = getElement(line)
    away_team = away_team[0].upper() + away_team[1:].lower()

    return away_team, line
def getHome_score(line):
    result = re.split(r',', line, maxsplit=2)
    home_score = re.findall(r'\d{0,2}', result[1])[0]
    return (home_score), result[1]
try:

   with open("D:/data/results.txt", encoding="utf-8", mode='r') as file:
       file.readline()
       line_number = 1
       for line in file:
           line = line.strip().rstrip()
           line_number += 1
           if not line:
               continue
           date, line = getDate(line)
           home_team, line = getHome_team(line)
           away_team,line = getHome_team(line)
           home_score,line = getHome_score(line)
           #print(date,home_team,away_team,home_score)
except IOError as e:
   print ("I/O error({0}): {1}".format(e.errno, e.strerror))
except ValueError as ve:
    print("Value error {0} in line {1}".format(ve, line_number))
def create_dataset(filen):
    try:
        dataset=dict()
        with open("D:/data/results.txt", encoding="utf-8", mode='r') as file:
            file_line = file.readline()

            if not file_line:
                return dataset
            if date not in dataset:
                dataset[date] = dict()

            while file_line:
                dataset[date].update({
                home_team: {
                    "home_score":{home_score}
                },
                away_team:{"away_score":{}
                }
            })

            file_line = file.readline()

        return dataset
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        return dict()
figure = { "data" : [
        {
            "x": [home_team ],
            "y":[home_score],
            "type": "scatter",
            "name": "score",
        },
        {
            "x": [date],
            "y": [home_team, away_team],
            "type": "bar",
            "name": "number of teams",
            "xaxis": "x2",
            "yaxis": "y2"
        },
        {
            "labels": [home_team],
            "values": [home_score],
            "type": "pie",
            "name": "team account",
        }
    ], "layout" : go.Layout(
            xaxis=dict(domain=[0, 0.45]), yaxis=dict(domain=[0, 0.45]),
            xaxis2=dict(domain=[0.55, 1]), yaxis2=dict(domain=[0, 0.45], anchor='x2'))}
    plot(figure, filename="plot.html")
