from otree.api import *


doc = """
A Test of Risk Aversion.—At the end of the session, we used a parsimonious procedure to
elicit an individual’s degree of risk aversion, taken from Charness and Uri Gneezy (forthcoming);
this allows us to control for this attribute in the analysis of the determinants of cooperative
and competitive attitudes. Each person was endowed with 100 points and was presented with a
one-shot decision task: choose how much of this endowment to invest in a risky asset and how
much to keep. People are informed that there is an even chance for the investment in the risky
asset to be a success or a failure. In case it fails, the amount invested is lost; in case of a success,
the investment returns 2.5 times its amount. In addition to the amount of the risky investment,
each person chooses one of two colors. If this color is randomly drawn (50 percent chance), the
investment is a success. Since the lottery gives an expected return of 1.25 point for each point
invested, a risk-neutral person should invest the full endowment in the risky asset. The lower the
amount invested in the risky asset, the higher is the degree of risk aversion. (Charness & Villeval AER 2009)
Task comes from "Portfolio Choice and Risk Attitudes: An Experiment" (Charness and Gneezy)
"""


class C(BaseConstants):
    NAME_IN_URL = 'risk_elicitation'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    ENDOWMENT = cu(200)
    FACTOR = 2.5


class Subsession(BaseSubsession):
    pass 

def creating_session(subsession: Subsession):
    import random
    for player in subsession.get_players():
        player.success = random.choice([True, False])
        print('set success to', player.success)

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    success = models.BooleanField()
    investment = models.IntegerField(min=0, max=200)
    color = models.BooleanField()
    resultat = models.BooleanField(initial=False)

#FUNCTIONS




def set_payoff(player: Player):
        group = player.group
        p = player
        if p.success == 1:
            if p.color == 1:
                print('richtig1')
                p.payoff = C.ENDOWMENT - p.investment + C.FACTOR * p.investment
                p.resultat = 1
            else:
                print('falsch1')
                p.payoff = C.ENDOWMENT - p.investment
                p.resultat = 0
        else:
            if p.color == 0:
                print('richtig2')
                p.payoff = C.ENDOWMENT - p.investment + C.FACTOR * p.investment
                p.resultat = 1
            else:
                print('falsch2')
                p.payoff = C.ENDOWMENT - p.investment
                p.resultat = 0


# PAGES
class Investment(Page):
    form_model = 'player'
    form_fields = ['investment']

class Color(Page):
    form_model = 'player'
    form_fields = ['color']

class Weiter(Page):

    @staticmethod
    def before_next_page(player, timeout_happened):
       return set_payoff(player)


class ResultsWaitPage(WaitPage):
    is_displayed = 'set_payoffs'


class Results(Page):
    pass


page_sequence = [Investment, Color, Weiter, Results]
