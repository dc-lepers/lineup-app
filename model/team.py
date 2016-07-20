from google.appengine.ext import ndb


class Team(ndb.Model):
	name = ndb.StringProperty()

class TeamDivision(ndb.Model):
	name = ndb.StringProperty()
	team = ndb.KeyProperty(Team)

class TeamMember(ndb.Model):
	name = ndb.StringProperty()
	alias = ndb.StringProperty()
	number = ndb.IntegerProperty()
	duty = 	ndb.StringProperty(choices=('n', 'a', 'c'))
	team = ndb.KeyProperty(Team)
	role = ndb.StringProperty(choices=('g', 'f1', 'f2', 'f3', 'd1', 'd3'))
	
class Lineup(ndb.Model):
	team_division = ndb.KeyProperty(TeamDivision)
	member = ndb.KeyProperty(TeamMember)
	role = ndb.StringProperty(choices=('d', 'g', 'f1', 'f2', 'f3', 'd1', 'd3'))

class Game(ndb.Model):
	place = ndb.StringProperty()
	home_team = ndb.KeyProperty(TeamDivision)
	guests_team = ndb.KeyProperty(TeamDivision)
	date_time = ndb.DateTimeProperty()
	score_home = ndb.IntegerProperty()
	score_guest = ndb.IntegerProperty()
	lineup = ndb.KeyProperty(Lineup, repeated=True)

def populate():
	team = Team(name="DC Lepers").put()

	black = TeamDivision(name="Black", team=team).put()
	white = TeamDivision(name="White", team=team).put()

	import datetime

	black_members = []
	white_members = []
	for i in range(5):
		black_members.append(
			TeamMember(name="player_{}".format(i), alias="player_{}".format(i), number=i, duty='n', team=team, role='f1').put())

	for i in range(10, 15):
		white_members.append(
			TeamMember(name="player_{}".format(i), alias="player_{}".format(i), number=i, duty='n', team=team, role='f1').put())

	lineup = []
	for m in black_members:
		lineup.append(Lineup(team_division=black, member=m, role='d').put())

	for m in white_members:
		lineup.append(Lineup(team_division=white, member=m, role='d').put())

	game = Game(
		place="Morozovo arena", home_team=black, guests_team=white, 
		date_time=datetime.datetime.now(), score_home=-1, score_guest=-1, lineup=lineup).put()
	
