from database.DB_connect import DBConnect
from model.player import Player


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getNodi(media):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select p.PlayerId as id, p.Name as name, avg(a.Goals) as media
                    from premierleague.actions a , premierleague.players p 
                    where a.PlayerID = p.PlayerID 
                    group by p.PlayerID 
                    having media>%s"""

        cursor.execute(query, (media,))

        for row in cursor:
            result.append(Player(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi(media):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select a.PlayerID as p1 , a2.PlayerID as p2, ( sum(a.TimePlayed) - sum(a2.TimePlayed) ) as diff
                    from premierleague.actions a , premierleague.actions a2,
                                                    (select p.PlayerID, avg(a1.Goals) as media
                                                    from premierleague.actions a1 , premierleague.players p 
                                                    where a1.PlayerID = p.PlayerID 
                                                    group by p.PlayerID 
                                                    having media>%s) p1,
                                                    (select p.PlayerID, avg(a3.Goals) as media
                                                    from premierleague.actions a3 , premierleague.players p 
                                                    where a3.PlayerID = p.PlayerID 
                                                    group by p.PlayerID 
                                                    having media>%s) p2
                    where a.PlayerID = p1.PlayerID
                    and a.Starts = 1
                    and a2.PlayerID = p2.PlayerID
                    and a2.Starts = 1
                    and a.PlayerID != a2.PlayerID
                    and a.TeamID != a2.TeamID
                    and a.MatchID = a2.MatchID 
                    group by a.PlayerID , a2.PlayerID
                    having diff > 0"""

        cursor.execute(query, (media,media))

        for row in cursor:
            result.append((row["p1"], row["p2"],row["diff"]))

        cursor.close()
        conn.close()
        return result

