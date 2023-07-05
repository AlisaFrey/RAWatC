from otree.api import *


doc = """
AF.5. Altruism 1. (Hypothetical situation:) Imagine the following situation:
 Today you unexpectedly received 1,000 Euro. How much of this amount would you donate to a good cause?
  (Values between 0 and 1000 are allowed.) 
  2. (Willingness to act:) 
  How willing are you to give to good causes without expecting anything in return?
  QJE Falk, Becker, Dohmen, Enke, Huffman, Sunde (2018)
"""


class C(BaseConstants):
    NAME_IN_URL = 'altruism_elicitation'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
    WP13421 = models.IntegerField(
    label= 'Wie sehr wären Sie bereit, für einen guten Zweck zu geben, ohne etwas als Gegenleistung zu erwarten?' ,
        choices=[[0, '0'],
                 [1, '1'],
                 [2, '2'],
                 [3, '3'],
                 [4, '4'],
                 [5, '5'],
                 [6, '6'],
                 [7, '7'],
                 [8, '8'],
                 [9, '9'],
                 [10, '10']],
        widget=widgets.RadioSelectHorizontal(),
    )

    WP13459 = models.IntegerField(min=0, max=1000, blank=True,
        label= 'Stellen Sie sich die folgende Situation vor:<br> Heute haben Sie unerwartet 1000 Euro erhalten. Wie viel von dem Geld würden Sie einem guten Zweck spenden?',
    )


# PAGES
class Frage(Page):
    pass
    form_model = 'player'
    form_fields = ['WP13421']

class Abgabe(Page):
    pass
    form_model = 'player'
    form_fields = ['WP13459']

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Frage, Abgabe] #, Results
