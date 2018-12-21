def create_dataset(file):
    try:

        dataset = dict()

        with open("results.txt", encoding="utf-8") as f:
            file_line = f.readline()

            if not file_line:
                return dataset

            header = file_line.rstrip().split(",")

            file_line = f.readline()

            while file_line:

                [date, home_team, away_team, home_score,away_score,tournament, city,country,neutral] = [element.strip() for element in
                                                            file_line.rstrip().split(",")]

                if date not in dataset:
                    dataset[date] = dict()
                if country not in dataset[date]:
                    dataset[date][country] = dict()
                if city not in dataset[date][country]:
                    dataset[date][country][city] = dict()

                dataset[date][country][city].update({
                    tournament: {
                        'tournament': {home_team:home_score,away_team:away_score},
                        'neutral':{neutral}

                    }})

                file_line = f.readline()

        return dataset

    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        return dict()

print(create_dataset('../data/results.csv'))
"""def max(file):
    max_tournament = dict()
    dataset = create_dataset(file)
    for date in dataset:
        max_tournament[date]=0
        for country in dataset[date]:
            for city in dataset[date][country]:
                for tournament in dataset[date][country][city]:
                    max_tournament[date][country][city] += int(dataset[date][country][city][tournament][ 'tournament'])
                    return max_tournament
print(max('../data/results.csv'))
def team(file):
    max_team = dict()
    dataset = create_dataset(file)
    for date in dataset:
        for country in dataset[date]:
            max_team[date][country]=0
            for city in dataset[date][country]:
                for  tournament in dataset[date][country][city]:
                    if "tournament" in dataset[date][country][city][tournament]:
                        max_team[date][country][city][tournament]["tournament"] += int(dataset[date][country][city][tournament]["tournament"][home_team])
                        return max_team
print(team('../data/results.csv'))"""