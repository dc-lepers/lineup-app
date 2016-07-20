from google.appengine.ext import ndb
from model import *
from services import LineupService

class GameService(object):
	@staticmethod
	def game(game_id):
		game = ndb.Key(Game, int(game_id)).get()

		home_division = game.home_team.get()
		guests_division = game.guests_team.get()

		home_team = home_division.team.get()
		guests_team = guests_division.team.get()

		lineup = LineupService.game_lineup(game_id)

		return {
			"place": game.place,
			"date": game.date_time,
			"home": {
				"team": home_team.name,
				"division": home_division.name,
				"lineup": lineup["guests"]
			},
			"guests": {
				"team": guests_team.name,
				"division": guests_division.name,
				"lineup": lineup["guests"]
			}
		}

