from google.appengine.ext import ndb
from model import *
import itertools

class LineupService(object):
	@staticmethod
	def game_lineup(game_id):
		game = ndb.Key(Game, int(game_id)).get()

		home = game.home_team
		guests = game.guests_team
		players = ndb.get_multi(game.lineup)

		lineup = {
			'home': [],
			'guests': []
		}

		for p in players:
			add_to = None

			if p.team_division == home:
				add_to = lineup['home']
			else:
				add_to = lineup['guests']

			member = p.member.get()

			add_to.append({
				'name': member.name,
				'alias': member.alias,
				'number': member.number,
				'duty': member.duty,
				'role': p.role if p.role != 'd' else member.role
			})

		return lineup

