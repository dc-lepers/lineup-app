import webapp2
import jinja2
import os.path
from model.team import populate

from controllers.lineup import LineupPage

class Populate(webapp2.RequestHandler):
	def get(self):
		populate()
		self.response.write("Ok")

app = webapp2.WSGIApplication([
	webapp2.Route(r'/game/<game_id:\d+>/lineup.html', handler=LineupPage),
], debug=True)