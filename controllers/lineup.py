import webapp2
from services import LineupService, GameService
from controllers import JINJA_ENVIRONMENT

class LineupPage(webapp2.RequestHandler):
    def get(self, game_id):
        template = JINJA_ENVIRONMENT.get_template('lineup.html')
        game = GameService.game(game_id)
        game['date'] = game["date"].strftime("%Y-%m-%d")


        self.response.write(template.render({"game": game}))

