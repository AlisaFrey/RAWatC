from otree.api import *
import random

doc = """
One player decides how to divide a certain amount between himself and the other
player.
See: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness
and the assumptions of economics." Journal of business (1986):
S285-S300.
"""


class C(BaseConstants):
    NAME_IN_URL = 'dict'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    INSTRUCTIONS_TEMPLATE = 'dictator/instructions.html'
    # Initial amount allocated to the dictator
    ENDOWMENT = cu(1000)


class Subsession(BaseSubsession):
    pass

def creating_session(subsession):
    import random
    subsession.group_randomly()
    group_list = subsession.get_groups()
    num_groups = len(group_list)
    print("group_list", group_list)
    list = [num_groups]
    for x in range(0, 10):
        number = num_groups - x
        if number >0:
            list.append(number)
        else:
            break
    group_selected = random.choice(list)
    print("group_selected", group_selected)
    for g in subsession.get_groups():
        g.group_selected = group_selected


class Group(BaseGroup):
    kept = models.CurrencyField()
    group_selected = models.IntegerField()
    


class Player(BasePlayer):
    keep = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself""",
        min=0,
        max=C.ENDOWMENT,
        label="Ich behalte",
    )

# FUNCTIONS



def set_payoffs(group):
    subsession = group.subsession
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    group.kept = p1.keep
    
    if group.id_in_subsession == group.group_selected:
        p1 = group.get_player_by_id(1)
        p2 = group.get_player_by_id(2)
        p1.payoff = p1.keep
        p2.payoff = C.ENDOWMENT - group.kept
    else:
        p1.payoff = 0
        p2.payoff = 0
    #p1.participant.vars['earning_1'] = p1.payoff
    #p2.participant.vars['earning_1'] = p2.payoff

#def get_players(player: Player):
#    participant_name = player.participant
#    return dict(participant_name=participant_name)


# PAGES
class Introduction(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        subsession = group.subsession
        session = group.session
        points = C.ENDOWMENT
        money = points.to_real_world_currency(session)
        return dict(points = points, money = money)
    

class ResultsWaitPage1(WaitPage):
    group_by_arrival_time = False

class Offer(Page):
    form_model = 'player'
    form_fields = ['keep']


    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        subsession = group.subsession
        session = group.session
        points = C.ENDOWMENT
        money = points.to_real_world_currency(session)
        return dict(points=points, money=money)


class ResultsWaitPage2(WaitPage):
    after_all_players_arrive = set_payoffs


class Weiter(Page):
    pass

class ResultsWaitPage3(WaitPage):
    wait_for_all_groups = True

class Results(Page):
    
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        session = group.session
        points = C.ENDOWMENT
        money = points.to_real_world_currency(session)
        return dict(offer=C.ENDOWMENT - group.kept, points=points, money=money)

    @staticmethod
    def js_vars(player: Player):
        group = player.group
        return dict(
            taken=group.kept,
        )


page_sequence = [ResultsWaitPage1, Introduction,
                 Offer, ResultsWaitPage2, Weiter, ResultsWaitPage3, Results]
