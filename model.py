#model.py
import csv

BB_FILE_NAME = 'umbball.csv'
FB_FILE_NAME = 'umfootball.csv'
bb_seasons = []

def get_bball_seasons(sortby='year', sortorder='desc'):
    if sortby == 'year':
        sortcol = 1
    elif sortby == 'wins':
        sortcol = 3
    elif sortby == 'pct':
        sortcol = 5
    else:
        sortcol = 0

    rev = (sortorder == 'desc')
    sorted_list = sorted(bb_seasons, key=lambda row: row[sortcol], reverse=rev)
    return sorted_list


def init_bball(csv_file_name = 'umbball.csv'):
    global bb_seasons
    with open('umbball.csv') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        next(reader)
        global bb_seasons
        bb_seasons =[]
        for r in reader:
            r[3] = int(r[3])
            r[4] = int(r[4])
            r[5] = float(r[5])
            bb_seasons.append(r)



def init_football(csv_file_name = FB_FILE_NAME):
    global bb_seasons
    with open('umfootball.csv') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        global bb_seasons
        bb_seasons =[]
        for r in reader:
            r[3] = int(r[3])
            r[4] = int(r[4])
            r[6] = float(r[6])
            bb_seasons.append(r)


def get_football_seasons(sortby='year', sortorder='desc'):
    if sortby == 'year':
        sortcol = 1
    elif sortby == 'wins':
        sortcol = 3
    elif sortby == 'pct':
        sortcol = 6
    else:
        sortcol = 0

    rev = (sortorder == 'desc')
    sorted_list = sorted(bb_seasons, key=lambda row: row[sortcol], reverse=rev)
    return sorted_list
