# data_utils.py - part of the WordGame

import DBcm


config = {
    "user": "samc",
    "password": "webuserpasswd",
    "database": "samc$default",
    "host": "samc.mysql.pythonanywhere-services.com",
}

## config = {
##     "user": "webuser",
##     "password": "webuserpasswd",
##     "database": "webDB",
##     "host": "localhost",
## }


def add_to_scores(name, score, word, guesses) -> None:
    """Add the name and its associated score, etc., to the database, as well
    as the word (which was the sourseword)."""
    with DBcm.UseDatabase(config) as cursor:
        _SQL = """insert into leaderboard
                (name, timetaken, sourceword, guesses)
                values
                (%s, %s, %s, %s)"""
        cursor.execute(_SQL, (name, score, word, ", ".join(guesses)))


def get_sorted_leaderboard() -> list:
    """Return a sorted list of tuples - this is the leaderboard."""
    with DBcm.UseDatabase(config) as cursor:
        _SQL = """select timetaken, name, sourceword, guesses from leaderboard
                order by timetaken"""
        cursor.execute(_SQL)
        data = cursor.fetchall()
        data2 = [(float(line[0]), line[1], line[2], line[3]) for line in data]
        return data2
