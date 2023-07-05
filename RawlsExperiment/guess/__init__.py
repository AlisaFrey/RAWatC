from otree.api import *
import random

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'guess'
    players_per_group = 16
    num_rounds = 1
    max_guess = 0
    min_guess = 100
    reward = cu(1000)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    average_guess = models.FloatField()
    two_thirds = models.FloatField()
    rounded_two_thirds = models.FloatField()
    rounded_average_guess = models.FloatField()
    random_winner = models.IntegerField()
    more_than_one = models.IntegerField()


def set_payoffs(group: Group):
        print('set_payoff works')
        players = group.get_players()

        guesses = [p.guess for p in players]
        print('guesses', guesses)
        group.average_guess = sum(guesses) / len(guesses)
        group.rounded_average_guess = round(group.average_guess, 2)
        print('average_guess', group.average_guess)
        group.two_thirds = group.average_guess *2/3
        group.rounded_two_thirds = round(group.average_guess * 2/3, 2)

        for p in players:
            p.proximity = abs(p.guess - group.two_thirds)

        proximities = [p.proximity for p in players]
        min_proximity = min(proximities)

        for p in players:
            if p.proximity == min_proximity:
                p.is_winner = True

        winners = [p.id_in_group for p in players if p.is_winner == True]
        group.more_than_one = len(winners)
        print('winners', winners)
        group.random_winner = random.choice(winners)
        print('group.random_winner', group.random_winner)
        
        for p in players:
            if p.id_in_group == group.random_winner:
                p.payoff = Constants.reward

class Player(BasePlayer):
    guess = models.IntegerField(min= 0,
                                max= 100,
                                label="Ihre Zahl:")


    proximity = models.FloatField()

    is_winner = models.BooleanField(initial=False)


# PAGES
class Guessing(Page):
    form_model = 'player'
    form_fields = ['guess']

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        session = group.session
        points = Constants.reward
        money = points.to_real_world_currency(session)
        return dict(points=points, money=money)


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        guesses = [p.guess for p in group.get_players()]
        return dict(
            guesses=guesses,
        )


page_sequence = [Guessing, ResultsWaitPage, Results]
