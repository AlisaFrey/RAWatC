'eigentlich ist das hier das __init__.py'

import time

from otree import settings
from otree.api import *

from .image_utils import encode_image
import random
#import numpy as np

author = 'Alisa Frey'

doc = """
Redristribution and Voting by Feet using a RET.
Real-effort tasks. The different tasks are available in task_matrix.py, task_transcription.py, etc.
You can delete the ones you don't need. 
"""


def get_task_module(player):
    """
    This function is only needed for demo mode, to demonstrate all the different versions.
    You can simplify it if you want.
    """
    from . import task_matrix, task_transcription, task_decoding

    session = player.session
    task = session.config.get("task")
    if task == "matrix":
        return task_matrix
    if task == "transcription":
        return task_transcription
    if task == "decoding":
        return task_decoding
    # default
    return task_matrix



class Constants(BaseConstants):
    name_in_url = "new_transcription_a_i_o_d"
    players_per_group = 16
    num_rounds = 6
    timeout_seconds = 180
    starttime = time.time()
    # select the treatment from this list: ['BASE', 'TAX_RANDOM', 'INCOME_RANDOM']  not (yet) included: 'PREFERENCES'
    treatment = 'BASE'

    B_instructions_template = __name__ + "/B/instructions_short_B.html"
    B_instructions_template_before = __name__ + "/B/instructions_before_B.html"
    B_instructions_template_game = __name__ + "/B/instructions_game_B.html"
    B_instructions_template_game_short = __name__ + "/B/instructions_game_short_B.html"
    B_instructions_template_example = __name__ + "/B/new_instructions_example_B.html"
    B_instructions_template_short = __name__ + "/B/instructions_preDecision_B.html"

    TR_instructions_template = __name__ + "/TR/instructions_short_TR.html"
    TR_instructions_template_before = __name__ + "/TR/instructions_before_TR.html"
    TR_instructions_template_game = __name__ + "/TR/instructions_game_TR.html"
    TR_instructions_template_game_short = __name__ + "/TR/instructions_game_short_TR.html"
    TR_instructions_template_example = __name__ + "/TR/new_instructions_example_TR.html"
    TR_instructions_template_short = __name__ + "/TR/instructions_preDecision_TR.html"


    IR_instructions_template = __name__ + "/IR/instructions_short_IR.html"
    IR_instructions_template_before = __name__ + "/IR/instructions_before_IR.html"
    IR_instructions_template_game = __name__ + "/IR/instructions_game_IR.html"
    IR_instructions_template_game_short = __name__ + "/IR/instructions_game_short_IR.html"
    IR_instructions_template_example = __name__ + "/IR/new_instructions_example_IR.html"
    IR_instructions_template_short = __name__ + "/IR/instructions_preDecision_IR.html"


    captcha_length = 3

    MULTIPLICATOR = cu(10)
    LOW_RATE = 0.15
    HIGH_RATE = 0.85

    low_percentage_rate = LOW_RATE * 100
    high_percentage_rate = HIGH_RATE * 100
    # Player.decision muss händisch angepasst werden bei anderen Prozentsätzen
    belief_bonus = cu(50)


def percentage(part, whole):
  percentage = 100 * float(part)/float(whole)
  return str(percentage) + "%"

print(percentage(Constants.low_percentage_rate, 100))
print(percentage(Constants.high_percentage_rate, 100))

class Subsession(BaseSubsession):
    treatment = models.StringField()


def creating_session(subsession: Subsession):
    session = subsession.session
    defaults = dict(
        retry_delay=1.0, puzzle_delay=1.0, attempts_per_puzzle=1, max_iterations=None
    )
    session.params = {}
    for param in defaults:
        session.params[param] = session.config.get(param, defaults[param])

    number_players = session.config.get("num_demo_participants")
    subsession.treatment = Constants.treatment
    print('treatment:', Constants.treatment)

    if Constants.treatment == 'TAX_RANDOM':
        for player in subsession.get_players():
            # SHUFFLING TAX RATES/DECISION for different rounds (TAX_RANDOM):
            if subsession.round_number == 1:
                LOW1 = [1, 2, 6, 9, 12]
                HIGH1 = [3, 4, 5, 7, 8, 10, 11, 13, 14, 15, 16]
                print('shuffling round 1')
                print(' LOW = ', LOW1)
                print(' HIGH = ', HIGH1)
                if player.id_in_group in LOW1:  # LOW
                    player.decision = 0
                if player.id_in_group in HIGH1:  # HIGH
                    player.decision = 1
            if subsession.round_number == 2:
                LOW2 = [1, 2, 3, 13, 16]
                HIGH2 = [4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15]
                print('shuffling round 2')
                print(' LOW = ', LOW2)
                print(' HIGH = ', HIGH2)
                if player.id_in_group in LOW2:  # LOW
                    player.decision = 0
                if player.id_in_group in HIGH2:  # HIGH
                    player.decision = 1
            if subsession.round_number == 3:
                LOW3 = [1, 3, 10, 16]
                HIGH3 = [2, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15]
                print('shuffling round 3')
                print(' LOW = ', LOW3)
                print(' HIGH = ', HIGH3)
                if player.id_in_group in LOW3:  # LOW
                    player.decision = 0
                if player.id_in_group in HIGH3:  # HIGH
                    player.decision = 1
            if subsession.round_number == 4:
                LOW4 = [1, 7, 10, 15]
                HIGH4 = [2, 3, 4, 5, 6, 8, 9, 11, 12, 13, 14, 16]
                print('shuffling round 4')
                print(' LOW = ', LOW4)
                print(' HIGH = ', HIGH4)
                if player.id_in_group in LOW4:  # LOW
                    player.decision = 0
                if player.id_in_group in HIGH4:  # HIGH
                    player.decision = 1
            if subsession.round_number == 5:
                LOW5 = [4, 10, 12]
                HIGH5 = [1, 2, 3, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16]
                print('shuffling round 5')
                print(' LOW = ', LOW5)
                print(' HIGH = ', HIGH5)
                if player.id_in_group in LOW5:  # LOW
                    player.decision = 0
                if player.id_in_group in HIGH5:  # HIGH
                    player.decision = 1
            if subsession.round_number == 6:
                LOW6 = [6, 11, 14]
                HIGH6 = [1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 13, 15, 16]
                print('shuffling round 6')
                print(' LOW = ', LOW6)
                print(' HIGH = ', HIGH6)
                if player.id_in_group in LOW6:  # LOW
                    player.decision = 0
                if player.id_in_group in HIGH6:  # HIGH
                    player.decision = 1
    else:
        None

    if Constants.treatment == 'INCOME_RANDOM':
        
            # SHUFFLING CORRECT PUZZLES for different rounds (INCOME_RANDOM treatment):
            if subsession.round_number == 1:
                puzzles_correct = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
                random.shuffle(puzzles_correct) # shuffles the list
                print('puzzles round 1')
                for player in subsession.get_players():
                    # pop() removes element so that the list does not contain the element afterwards
                    player.num_correct = puzzles_correct.pop()
                    #random.choice(puzzles_correct) chooses for each player from the whole list 

            elif subsession.round_number == 2:
                puzzles_correct = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
                random.shuffle(puzzles_correct)
                print('puzzles round 2')
                for player in subsession.get_players():
                    player.num_correct = puzzles_correct.pop()

            elif subsession.round_number == 3:
                puzzles_correct = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
                random.shuffle(puzzles_correct)  # shuffles the list
                print('puzzles round 3')
                for player in subsession.get_players():
                    player.num_correct = puzzles_correct.pop()
                
            elif subsession.round_number == 4:
                puzzles_correct = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
                random.shuffle(puzzles_correct)  # shuffles the list
                print('puzzles round 4')
                for player in subsession.get_players():
                    player.num_correct = puzzles_correct.pop()

            elif subsession.round_number == 5:
                puzzles_correct = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
                random.shuffle(puzzles_correct)  # shuffles the list
                print('puzzles round 5')
                for player in subsession.get_players():
                    player.num_correct = puzzles_correct.pop()
                
            elif subsession.round_number == 6:
                puzzles_correct = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
                random.shuffle(puzzles_correct)  # shuffles the list
                print('puzzles round 6')
                for player in subsession.get_players():
                    player.num_correct = puzzles_correct.pop()


class Group(BaseGroup):
    players_low = models.IntegerField(initial=0)
    players_high = models.IntegerField(initial=0)

    sum_taxes_low = models.CurrencyField(initial=0)
    sum_taxes_high = models.CurrencyField(initial=0)

    individual_share_low = models.CurrencyField(initial=0)
    individual_share_high = models.CurrencyField(initial=0)

    puzzles_low = models.FloatField(initial=0)
    puzzles_high = models.FloatField(initial=0)
    fake_puzzles_low = models.FloatField(initial=0)
    fake_puzzles_high = models.FloatField(initial=0)



class Player(BasePlayer):
    iteration = models.IntegerField(initial=0)
    num_trials = models.IntegerField(initial=0)
    num_correct = models.IntegerField(initial=0)
    fake_num_correct = models.IntegerField(initial=0)
    num_failed = models.IntegerField(initial=0)
    loadtime = models.FloatField(initial=0)
    timeslist = models.LongStringField()
    correct_false = models.LongStringField()

    decision = models.IntegerField(
# muss händisch angepasst werden bei anderen Prozentsätzen
        choices=[[0, '15%'], [1, "85%"]],

        widget=widgets.RadioSelect,

        label="Welchen Prozentsatz wählen Sie?"
    )

    taxes_paid = models.CurrencyField(initial=0)
    taxes_paid_low = models.CurrencyField(initial=0)
    taxes_paid_high = models.CurrencyField(initial=0)

    redistribution_low = models.CurrencyField(initial=0)
    redistribution_high = models.CurrencyField(initial=0)

    income=models.CurrencyField(initial=0)
    income_at=models.CurrencyField(initial=0)
    income_ar=models.CurrencyField(initial=0)
    payoff_ab=models.CurrencyField(initial=0)

    total_taxes = models.CurrencyField(initial=0)
    individual_share = models.CurrencyField(initial=0)


    num_correct_low = models.IntegerField(initial=0)
    num_correct_high = models.IntegerField(initial=0)
    fake_num_correct_low = models.IntegerField(initial=0)
    fake_num_correct_high = models.IntegerField(initial=0)

    belief_bonus1 = models.CurrencyField(initial=0)
    belief_bonus2 = models.CurrencyField(initial=0)
    belief_bonus3 = models.CurrencyField(initial=0)
# Beliefs
    belief1 = models.IntegerField(choices=[[1, "besser als der Durchschnitt"], [0, "genau im Durchschnitt"], [-1, "schlechter als der Durchschnitt"]],
                                  widget=widgets.RadioSelect,
                                  label='Wie schätzen Sie Ihre Anzahl gelöster Encryptio ein?')
    belief2 = models.FloatField(initial=0,
        min=0, max=1000, label='Was denken Sie, wie viele Encryptio haben Teilnehmende, die den gleichen Prozentsatz wie Sie gewählt haben, durchschnittlich in dieser Runde richtig gelöst?')
        #BooleanField(choices=[(
        #1, 'Ja'), (0, 'Nein')], label='Denken Sie, dass Sie in dieser Runde überdurchschnittlich viele Encryptio gelöst haben?')
    belief3 = models.FloatField(initial=0,
        min=0, max=1000, label='Was denken Sie, wie viele Encryptio haben Sie in dieser Runde richtig gelöst?')
    belief4 = models.IntegerField(min=1, max=Constants.players_per_group,
                                  label='Was denken Sie, auf welchem Rang lägen Sie mit der Anzahl Ihrer gelösten Encryptio im Vergleich zu den anderen TeilnehmerInnen in Ihrer Gruppe?')

#Control Questions
    B_control1 = models.IntegerField(min=1, max=Constants.players_per_group, label='Wie viele Teilnehmende (Sie eingeschlossen) sind insgesamt in einer Gruppe?')
    B_control2 = models.IntegerField(
        min=0, max=1000, label="Nehmen Sie an Ihr Einkommen beträgt in dieser Runde 200 Punkte. In dieser Runde haben nur Sie den Prozentsatz 15% gewählt. Wie hoch ist Ihr Einkommen nach Anwendung des Prozentsatzes?")
    B_control3 = models.IntegerField(choices=[[0, "100 Punkte "], [0, "15 Punkte"], [1, "85 Punkte"], [0, "30 Punkte"]],
                                   widget=widgets.RadioSelect,
                                   label='Ihr Einkommen in dieser Runde beträgt 100 Punkte. Ihr gewählter Prozentsatz lautet 85%. Wie viele Punkte werden Ihnen zunächst abgezogen?'
                                   )
    B_control4 = models.IntegerField(choices=[[1, "100 Punkte "], [0, "15 Punkte"], [0, "85 Punkte"], [0, "30 Punkte"]],
                                   widget=widgets.RadioSelect,
                                   label='Mit Ihnen haben insgesamt 10 Teilnehmende den gleichen Prozentsatz (85%) gewählt. Durchschnittlich wurden jedem dieser 10 Teilnehmenden zunächst 100 Punkte abgezogen. Wie hoch ist Ihre Auszahlung (indirekte Vergütung) nach Anwendung des Prozentsatzes?'
                                   )
    B_control5 = models.IntegerField(choices=[[0, "100 Punkte "], [1, "15 Punkte"], [0, "85 Punkte"], [0, "30 Punkte"]],
                                   widget=widgets.RadioSelect,
                                   label='Ihr Einkommen in dieser Runde beträgt 100 Punkte. Ihr gewählter Prozentsatz lautet 15%. Wie viele Punkte werden Ihnen zunächst abgezogen?'
                                   )
    B_control6 = models.IntegerField(choices=[[0, "100 Punkte "], [0, "15 Punkte"], [0, "85 Punkte"], [1, "30 Punkte"]],
                                   widget=widgets.RadioSelect,
                                     label='Mit Ihnen haben insgesamt 10 Teilnehmende den gleichen Prozentsatz (15%) gewählt. Durchschnittlich wurden jedem dieser 10 Teilnehmenden zunächst 30 Punkte abgezogen. Wie hoch ist Ihre Auszahlung (indirekte Vergütung) nach Anwendung des Prozentsatzes?'
                                   )
    B_control7 = models.IntegerField(choices=[[0, "105 Punkte "], [0, "15 Punkte"], [0, "85 Punkte"], [1, "35 Punkte"]],
                                     widget=widgets.RadioSelect
                                     )

    TR_control1 = models.IntegerField(min=1, max=Constants.players_per_group,
                                      label='Wie viele Teilnehmende (Sie eingeschlossen) sind insgesamt in einer Gruppe?')
    TR_control2 = models.IntegerField(
        min=0, max=1000, label="Nehmen Sie an Ihr Einkommen beträgt in dieser Runde 200 Punkte. In dieser Runde haben nur Sie den Prozentsatz 15% zufällig zugewiesen bekommen. Wie hoch ist Ihr Einkommen nach Anwendung des Prozentsatzes?")
    TR_control3 = models.IntegerField(choices=[[0, "100 Punkte "], [0, "15 Punkte"], [1, "85 Punkte"], [0, "30 Punkte"]],
                                     widget=widgets.RadioSelect,
                                     label='Ihr Einkommen in dieser Runde beträgt 100 Punkte. Ihr zufällig zugewiesener Prozentsatz lautet 85%. Wie viele Punkte werden Ihnen zunächst abgezogen?'
                                     )
    TR_control4 = models.IntegerField(choices=[[1, "100 Punkte "], [0, "15 Punkte"], [0, "85 Punkte"], [0, "30 Punkte"]],
                                     widget=widgets.RadioSelect,
                                      label='Mit Ihnen haben insgesamt 10 Teilnehmende den gleichen Prozentsatz (85%) zufällig zugewiesen bekommen. Durchschnittlich wurden jedem dieser 10 Teilnehmenden zunächst 100 Punkte abgezogen. Wie hoch ist Ihre Auszahlung (indirekte Vergütung) nach Anwendung des Prozentsatzes?'
                                     )
    TR_control5 = models.IntegerField(choices=[[0, "100 Punkte "], [1, "15 Punkte"], [0, "85 Punkte"], [0, "30 Punkte"]],
                                     widget=widgets.RadioSelect,
                                      label='Ihr Einkommen in dieser Runde beträgt 100 Punkte. Ihr zufällig zugewiesener Prozentsatz lautet 15%. Wie viele Punkte werden Ihnen zunächst abgezogen?'
                                     )
    TR_control6 = models.IntegerField(choices=[[0, "100 Punkte "], [0, "15 Punkte"], [0, "85 Punkte"], [1, "30 Punkte"]],
                                     widget=widgets.RadioSelect,
                                      label='Mit Ihnen haben insgesamt 10 Teilnehmende den gleichen Prozentsatz (15%) zufällig zugewiesen bekommen. Durchschnittlich wurden jedem dieser 10 Teilnehmenden zunächst 30 Punkte abgezogen. Wie hoch ist Ihre Auszahlung (indirekte Vergütung) nach Anwendung des Prozentsatzes?'
                                     )
    TR_control7 = models.IntegerField(choices=[[0, "105 Punkte "], [0, "15 Punkte"], [0, "85 Punkte"], [1, "35 Punkte"]],
                                     widget=widgets.RadioSelect
                                     )

    IR_control1 = models.IntegerField(min=1, max=Constants.players_per_group,
                                      label='Wie viele Teilnehmende (Sie eingeschlossen) sind insgesamt in einer Gruppe?')
    IR_control2 = models.IntegerField(
        min=0, max=1000, label="Nehmen Sie an Ihr Einkommen beträgt in dieser Runde 200 Punkte. In dieser Runde haben nur Sie den Prozentsatz 15% gewählt. Wie hoch ist Ihr Einkommen nach Anwendung des Prozentsatzes?")
    IR_control3 = models.IntegerField(choices=[[0, "100 Punkte "], [0, "15 Punkte"], [1, "85 Punkte"], [0, "30 Punkte"]],
                                     widget=widgets.RadioSelect,
                                     label='Ihr Einkommen in dieser Runde beträgt 100 Punkte. Ihr gewählter Prozentsatz lautet 85%. Wie viele Punkte werden Ihnen zunächst abgezogen?'
                                     )
    IR_control4 = models.IntegerField(choices=[[1, "100 Punkte "], [0, "15 Punkte"], [0, "85 Punkte"], [0, "30 Punkte"]],
                                     widget=widgets.RadioSelect,
                                     label='Mit Ihnen haben insgesamt 10 Teilnehmende den gleichen Prozentsatz (85%) gewählt. Durchschnittlich wurden jedem dieser 10 Teilnehmenden zunächst 100 Punkte abgezogen. Wie hoch ist Ihre Auszahlung (indirekte Vergütung) nach Anwendung des Prozentsatzes?'
                                     )
    IR_control5 = models.IntegerField(choices=[[0, "100 Punkte "], [1, "15 Punkte"], [0, "85 Punkte"], [0, "30 Punkte"]],
                                     widget=widgets.RadioSelect,
                                     label='Ihr Einkommen in dieser Runde beträgt 100 Punkte. Ihr gewählter Prozentsatz lautet 15%. Wie viele Punkte werden Ihnen zunächst abgezogen?'
                                     )
    IR_control6 = models.IntegerField(choices=[[0, "100 Punkte "], [0, "15 Punkte"], [0, "85 Punkte"], [1, "30 Punkte"]],
                                     widget=widgets.RadioSelect,
                                     label='Mit Ihnen haben insgesamt 10 Teilnehmende den gleichen Prozentsatz (15%) gewählt. Durchschnittlich wurden jedem dieser 10 Teilnehmenden zunächst 30 Punkte abgezogen. Wie hoch ist Ihre Auszahlung (indirekte Vergütung) nach Anwendung des Prozentsatzes?'
                                     )
    IR_control7 = models.IntegerField(choices=[[0, "105 Punkte "], [0, "15 Punkte"], [0, "85 Punkte"], [1, "35 Punkte"]],
                                     widget=widgets.RadioSelect
                                     )

#Functions
# probleme mit Objekten "UnboundLocalError: local variable 'player' referenced before assignment"

def group_size(group: Group):
        players = group.get_players()
        decision = [round(p.decision) for p in players]
        group.players_low = Constants.players_per_group - sum(decision)
        print('group.players_low', group.players_low)
        group.players_high = sum(decision)
        print('group.players_high', group.players_high)
def evaluation(group: Group):
        print('evaluation')
        players = group.get_players()
        decision = [round(p.decision) for p in players]
        for p in players:
            final_round = Constants.num_rounds
            if p.round_number == final_round:
                if Constants.treatment == 'BASE' or Constants.treatment == 'TAX_RANDOM':
                    print('player')
                    if (p.num_correct-1) <= p.belief3 <= (p.num_correct+1):
                        p.belief_bonus3 = Constants.belief_bonus
                        print("correct guess")
                    else:
                        p.belief_bonus3 = 0
                        print("wrong guess")

                    if p.decision == 1:
                        print("high")
                        if (group.puzzles_high - 1) <= p.belief2 <= (group.puzzles_high + 1):
                            print("correct guess average")
                            p.belief_bonus2 = Constants.belief_bonus
                        else:
                            print("wrong guess average")
                            p.belief_bonus2 = 0
                    elif p.decision == 0:
                        print("low")
                        if (group.puzzles_low - 1) <= p.belief2 <= (group.puzzles_low + 1):
                            print("correct guess average")
                            p.belief_bonus2 = Constants.belief_bonus
                        else:
                            print("wrong guess average")
                            p.belief_bonus2 = 0

                elif Constants.treatment == 'INCOME_RANDOM':
                    print('player fake')
                    if (p.fake_num_correct -1) <= p.belief3 <= (p.fake_num_correct +1):
                        p.belief_bonus3 = Constants.belief_bonus
                        print("correct guess")
                    else:
                        p.belief_bonus3 = 0
                        print("wrong guess")

                    if p.decision == 1:
                        if (group.fake_puzzles_high -1) <= p.belief2 <= (group.fake_puzzles_high +1):
                            print("correct guess average")
                            p.belief_bonus2 = Constants.belief_bonus
                        else:
                            print("wrong guess")
                            p.belief_bonus2 = 0
                    elif p.decision == 0:
                        if (group.fake_puzzles_low -1) <= p.belief2 <= (group.fake_puzzles_low +1):
                            print("correct guess average")
                            p.belief_bonus2 = Constants.belief_bonus
                        else:
                            print("wrong guess average")
                            p.belief_bonus2 = 0
                else:
                    p.belief_bonus2 = 0
                    p.belief_bonus3 = 0
                    print("no paid guess")

def set_payoffs(group: Group):
        print('set_payoffs')
        #if group==1:
        players = group.get_players()
        decision = [round(p.decision) for p in players]
        print("decision list", decision)
        #players
            #p1 = group.get_player_by_id(1)
            #p2 = group.get_player_by_id(2)
            #p3 = group.get_player_by_id(3)
            #p4 = group.get_player_by_id(4)
            #p5 = group.get_player_by_id(5)
            #p6 = group.get_player_by_id(6)

        #for p in players:
        #    p.taxes_paid = p.income * p.decision
        #    print("taxes_paid", p.taxes_paid)

        for p in players:
            p.taxes_paid_low = p.income * (1 - p.decision) * Constants.LOW_RATE
            print("taxes_paid_l", p.taxes_paid_low)
            p.taxes_paid_high = p.income * p.decision * Constants.HIGH_RATE
            print("taxes_paid_h", p.taxes_paid_high)

            p.num_correct_low = p.num_correct * (1 - p.decision)
            print("p.num_correct_low", p.num_correct_low)
            p.num_correct_high = p.num_correct * p.decision
            print("p.num_correct_high", p.num_correct_high)
            
            p.fake_num_correct_low = p.fake_num_correct * (1 - p.decision)
            print("p.fake_num_correct_low", p.fake_num_correct_low)
            p.fake_num_correct_high = p.fake_num_correct * p.decision
            print("p.fake_num_correct_high", p.fake_num_correct_high)
            

        group.players_low = Constants.players_per_group - sum(decision)
            #Constants.players_per_group - round(p1.decision) + round(p2.decision) + round(p3.decision) + round(p4.decision) + round(p5.decision) + round(p6.decision)
        print('group.players_low', group.players_low)
            #sum(round((decision)))
            #round(p1.decision) + round(p2.decision) + round(p3.decision) + round(p4.decision) + round(p5.decision) + round(p6.decision)
        group.players_high = sum(decision)
            #round(p1.decision) + round(p2.decision) + round(p3.decision) + round(p4.decision) + round(p5.decision) + round(p6.decision)
        print('group.players_high', group.players_high)
            #sum(round(player.decision))
            #round(p1.decision) + round(p2.decision) + round(p3.decision) + round(p4.decision) + round(p5.decision) + round(p6.decision)
        
        #for p in players:
        #    if p.decision == Constants.LOW_RATE:
        #            taxes_paid_low = p.taxes_paid #[p.taxes_paid for p in players and p.decision == Constants.LOW_RATE]
        #            print("p.taxes_paid_low", taxes_paid_low)
        #    elif p.decision == Constants.HIGH_RATE:
        #            taxes_paid_high = p.taxes_paid #[p.taxes_paid for p in players and p.decision == Constants.HIGH_RATE]
        #            print("p.taxes_paid_high", taxes_paid_high)
        #    else:
        #            print("Done Iteration 1")

        group.sum_taxes_low = sum(p.taxes_paid_low  for p in players)
        print("group.sum_taxes_low", group.sum_taxes_low)
        group.sum_taxes_high = sum(p.taxes_paid_high  for p in players)
        print("group.sum_taxes_high", group.sum_taxes_high)

        if Constants.treatment == 'BASE':
            if group.players_low == 0:
                group.puzzles_low = 0
                print("group.puzzles_low", group.puzzles_low)
            else:
                group.puzzles_low = round(sum(p.num_correct_low for p in players)/ group.players_low, 2)
                print("group.puzzles_low", group.puzzles_low)

            if group.players_high == 0:
                group.puzzles_high = 0
                print("group.puzzles_high", group.puzzles_high)
            else: 
                group.puzzles_high = round(sum(p.num_correct_high for p in players)/group.players_high, 2)
                print("group.puzzles_high", group.puzzles_high)
        elif Constants.treatment == 'TAX_RANDOM':
            if group.players_low == 0:
                group.puzzles_low = 0
                print("group.puzzles_low", group.puzzles_low)
            else:
                group.puzzles_low = round(sum(p.num_correct_low for p in players)/ group.players_low, 2)
                print("group.puzzles_low", group.puzzles_low)

            if group.players_high == 0:
                group.puzzles_high = 0
                print("group.puzzles_high", group.puzzles_high)
            else: 
                group.puzzles_high = round(sum(p.num_correct_high for p in players)/group.players_high, 2)
                print("group.puzzles_high", group.puzzles_high)
        elif Constants.treatment == 'INCOME_RANDOM':
            if group.players_low == 0:
                group.puzzles_low = 0
                group.fake_puzzles_low = 0
                print("group.puzzles_low", group.puzzles_low)
            else:
                group.puzzles_low = round(sum(p.num_correct_low for p in players)/ group.players_low,2)
                group.fake_puzzles_low = round(sum(p.fake_num_correct_low for p in players)/ group.players_low, 2)
                print("group.puzzles_low", group.puzzles_low)

            if group.players_high == 0:
                group.puzzles_high = 0
                group.fake_puzzles_high = 0
                print("group.puzzles_high", group.puzzles_high)
            else: 
                group.puzzles_high = round(sum(p.num_correct_high for p in players)/group.players_high, 2)
                group.fake_puzzles_high = round(
                    sum(p.fake_num_correct_high for p in players)/group.players_high, 2)
                print("group.puzzles_high", group.puzzles_high)

        group.individual_share_low = (group.sum_taxes_low + (group.players_low*cu(0.49)))/max(1, group.players_low) #aufrunden
        print("max(1, group.players_low)", max(1, group.players_low))
        print("individual_share_low", group.individual_share_low)
        group.individual_share_high = (group.sum_taxes_high + (group.players_high*cu(0.49)))/max(1, group.players_high)
        print("max(1, group.players_high)", max(1, group.players_high))
        print("individual_share_high", group.individual_share_high)

        #if p.decision == Constants.LOW_RATE:
        #        total_taxes = [p.taxes_paid_low for p in players and p.decision == Constants.LOW_RATE] #sum(taxes_paid_low)
        #        print("total_taxes low", total_taxes)
        #        individual_share = total_taxes / max(1, group.players_low)
        #        print("max(1, group.players_low)", max(1, group.players_low))
        #        print("individual_share", individual_share)

        #elif p.decision == Constants.HIGH_RATE:
        #        total_taxes = sum(taxes_paid_high)
        #        print("total_taxes high", total_taxes)
        #        individual_share = total_taxes / max(1, group.players_high)
        #        print("max(1, group.players_high)", max(1, group.players_high))
        #        print("individual_share", individual_share)
        #else:
        #        print("Done Iteration 2")

        for p in players:
            print("player number", p)
            p.redistribution_low = group.individual_share_low * (1 - p.decision)
            print("(1 - p.decision)", (1 - p.decision))
            print("p.redistribution_low", p.redistribution_low)
            p.redistribution_high = group.individual_share_high * p.decision
            print("p.decision", p.decision)
            print("p.redistribution_high", p.redistribution_high)
            #for player in players:
            p.payoff = p.income - p.taxes_paid_low - p.taxes_paid_high + \
                p.redistribution_low + p.redistribution_high + cu(p.belief_bonus1) + cu(p.belief_bonus2) + cu(p.belief_bonus3)
            print("player.income", p.income)
            print("player.taxes_paid_low", p.taxes_paid_low)
            print("player.taxes_paid_high", p.taxes_paid_high)
            print("p.redistribution_low", p.redistribution_low)
            print("p.redistribution_high", p.redistribution_high)
            print("player.payoff", p.payoff)
            p.income_ar = p.income - p.taxes_paid_low - p.taxes_paid_high + p.redistribution_low + p.redistribution_high
            print("player.income_ar", p.income_ar)


        #elif player.group==2:
        #    print("group2")
        #else:
        #    print("else reached")


# puzzle-specific stuff


class Puzzle(ExtraModel):
    """A model to keep record of all generated puzzles"""

    player = models.Link(Player)
    iteration = models.IntegerField(initial=0)
    attempts = models.IntegerField(initial=0)
    timestamp = models.FloatField(initial=0)
    timeslist = models.LongStringField()
    loadtime = models.FloatField(initial=0)
    correct_false = models.LongStringField()
    # can be either simple text, or a json-encoded definition of the puzzle, etc.
    text = models.LongStringField()
    # solution may be the same as text, if it's simply a transcription task
    solution = models.LongStringField()
    response = models.LongStringField()
    response_timestamp = models.FloatField()
    is_correct = models.BooleanField()


def generate_puzzle(player: Player) -> Puzzle:
    """Create new puzzle for a player"""
    task_module = get_task_module(player)
    fields = task_module.generate_puzzle_fields()
    player.iteration += 1
    return Puzzle.create(
        player=player, iteration=player.iteration, timestamp=time.time(), **fields
    )


def get_current_puzzle(player):
    puzzles = Puzzle.filter(player=player, iteration=player.iteration)
    if puzzles:
        [puzzle] = puzzles
        return puzzle


def encode_puzzle(puzzle: Puzzle):
    """Create data describing puzzle to send to client"""
    task_module = get_task_module(puzzle.player)  # noqa
    # generate image for the puzzle
    image = task_module.render_image(puzzle)
    data = encode_image(image)
    return dict(image=data)


def get_progress(player: Player):
    """Return current player progress"""
    return dict(
        num_trials=player.num_trials,
        num_correct=player.num_correct,
        fake_num_correct=player.fake_num_correct,
        num_incorrect=player.num_failed,
        iteration=player.iteration,
        timeslist=timelist,
        correct_false=c_f_list
    )


timelist = []
c_f_list = []

def play_game(player: Player, message: dict):
    """Main game workflow
    Implemented as reactive scheme: receive message from vrowser, react, respond.

    Generic game workflow, from server point of view:
    - receive: {'type': 'load'} -- empty message means page loaded
    - check if it's game start or page refresh midgame
    - respond: {'type': 'status', 'progress': ...}
    - respond: {'type': 'status', 'progress': ..., 'puzzle': data} -- in case of midgame page reload

    - receive: {'type': 'next'} -- request for a next/first puzzle
    - generate new puzzle
    - respond: {'type': 'puzzle', 'puzzle': data}

    - receive: {'type': 'answer', 'answer': ...} -- user answered the puzzle
    - check if the answer is correct
    - respond: {'type': 'feedback', 'is_correct': true|false, 'retries_left': ...} -- feedback to the answer

    If allowed by config `attempts_pre_puzzle`, client can send more 'answer' messages
    When done solving, client should explicitely request next puzzle by sending 'next' message

    Field 'progress' is added to all server responses to indicate it on page.

    To indicate max_iteration exhausted in response to 'next' server returns 'status' message with iterations_left=0
    """
    session = player.session
    my_id = player.id_in_group
    params = session.params
    task_module = get_task_module(player)

    if player.num_trials == 0:
        timelist.clear()
        c_f_list.clear()
    else:
        pass

    if player.loadtime == 0:
        player.loadtime = time.time() - Constants.starttime
    else:
        pass

    now = time.time()
    # the current puzzle or none
    current = get_current_puzzle(player)

    message_type = message['type']

    # page loaded
    if message_type == 'load':
        p = get_progress(player)
        if current:
            return {
                my_id: dict(type='status', progress=p, puzzle=encode_puzzle(current))
            }
        else:
            return {my_id: dict(type='status', progress=p)}

    if message_type == "cheat" and settings.DEBUG:
        return {my_id: dict(type='solution', solution=current.solution)}

    # client requested new puzzle
    if message_type == "next":
        if current is not None:
            if current.response is None:
                raise RuntimeError("trying to skip over unsolved puzzle")
            if now < current.timestamp + params["puzzle_delay"]:
                raise RuntimeError("retrying too fast")
            if current.iteration == params['max_iterations']:
                return {
                    my_id: dict(
                        type='status', progress=get_progress(player), iterations_left=0
                    )
                }
        # generate new puzzle
        z = generate_puzzle(player)
        p = get_progress(player)
        return {my_id: dict(type='puzzle', puzzle=encode_puzzle(z), progress=p)}

    # client gives an answer to current puzzle
    if message_type == "answer":
        if current is None:
            raise RuntimeError("trying to answer no puzzle")

        if current.response is not None:  # it's a retry
            if current.attempts >= params["attempts_per_puzzle"]:
                raise RuntimeError("no more attempts allowed")
            if now < current.response_timestamp + params["retry_delay"]:
                raise RuntimeError("retrying too fast")

            # undo last updation of player progress
            player.num_trials -= 1
            if current.is_correct:
                player.num_correct -= 1
                player.fake_num_correct -= 1
            else:
                player.num_failed -= 1

        # check answer
        answer = message["answer"]

        if answer == "" or answer is None:
            raise ValueError("bogus answer")

        current.response = answer
        current.is_correct = task_module.is_correct(answer, current)
        current.response_timestamp = now
        current.attempts += 1

        # update player progress
        if current.is_correct:
            if Constants.treatment != 'INCOME_RANDOM': player.num_correct += 1
            player.fake_num_correct += 1
            z = 1
            time1 = time.time()
            time_per_puzzle = time1 - Constants.starttime - player.loadtime - sum(timelist)
            starttime1 = time.time()
        else:
            player.num_failed += 1
            z = 0
            time1 = time.time()
            time_per_puzzle = time1 - Constants.starttime - \
                player.loadtime - sum(timelist)
            starttime1 = time.time()
        player.num_trials += 1
        timelist.append(round(time_per_puzzle, 2))
        c_f_list.append(z)

        liststring = ''
        for x in timelist:
            liststring = liststring + str(x) + ',  '
        player.timeslist = str(liststring)

        c_f_string = ''
        for x in c_f_list:
            c_f_string = c_f_string + str(x) + ',  '
        player.correct_false = str(c_f_string)


        retries_left = params["attempts_per_puzzle"] - current.attempts
        p = get_progress(player)
        return {
            my_id: dict(
                type='feedback',
                is_correct=current.is_correct,
                retries_left=retries_left,
                progress=p,
            )
        }

    raise RuntimeError("unrecognized message from client")

class GBATWaitPage(WaitPage):
    group_by_arrival_time = True

    #@staticmethod
    #def after_all_players_arrive(group: Group):
        #import random
        #group.treatment = random.choice([True, False])

class Welcome(Page):
        @staticmethod
        def is_displayed(player):
            return player.round_number == 1

        @staticmethod
        def vars_for_template(player: Player):
            low_percentage = percentage(Constants.low_percentage_rate,100)
            high_percentage = percentage(Constants.high_percentage_rate,100)
            r_income = Constants.MULTIPLICATOR * 25
            subtraction_l = r_income * Constants.LOW_RATE
            subtraction_h = r_income * Constants.HIGH_RATE
            r_income_sub_l = r_income - subtraction_l
            r_income_sub_h = r_income - subtraction_h
            new_r_income_sub_l_1 = r_income - subtraction_l
            new_r_income_sub_h_1 = r_income - subtraction_h
            new_r_income_sub_l_2 = r_income - subtraction_l
            new_r_income_sub_h_2 = r_income - subtraction_h
            r_other_income_D = Constants.MULTIPLICATOR * 15
            r_other_income_E = Constants.MULTIPLICATOR * 30
            r_other_income = r_other_income_D + r_other_income_E
            new_r_all_other_income_1 = Constants.MULTIPLICATOR * 150
            new_r_all_other_income_2 = Constants.MULTIPLICATOR * 250
            new_num_high = round(Constants.players_per_group - (Constants.players_per_group/2))
            new_num_low = round(Constants.players_per_group - new_num_high)
            new_average_income_l_1 = (r_income + new_r_all_other_income_1)/new_num_low
            new_average_income_h_1 = (r_income + new_r_all_other_income_1)/new_num_high
            new_average_income_l_2 = (r_income + new_r_all_other_income_2)/new_num_low
            new_average_income_h_2 = (r_income + new_r_all_other_income_2)/new_num_high
            num_others = 2
            num_p = num_others + 1
            subtraction_other_l = r_other_income  * Constants.LOW_RATE
            subtraction_other_l_D = r_other_income_D  * Constants.LOW_RATE
            subtraction_other_l_E = r_other_income_E  * Constants.LOW_RATE
            subtraction_other_h_D = r_other_income_D  * Constants.HIGH_RATE
            subtraction_other_h_E = r_other_income_E  * Constants.HIGH_RATE
            r_income_other_sub_l_D = r_other_income_D - subtraction_other_l_D
            r_income_other_sub_l_E = r_other_income_E - subtraction_other_l_E
            r_income_other_sub_h_D = r_other_income_D - subtraction_other_h_D
            r_income_other_sub_h_E = r_other_income_E - subtraction_other_h_E
            subtraction_other_h = r_other_income  * Constants.HIGH_RATE
            new_sum_subtractions_l_1 = new_r_all_other_income_1 * Constants.LOW_RATE
            new_sum_subtractions_h_1 = new_r_all_other_income_1 * Constants.HIGH_RATE
            new_sum_subtractions_l_2 = new_r_all_other_income_2 * Constants.LOW_RATE
            new_sum_subtractions_h_2 = new_r_all_other_income_2 * Constants.HIGH_RATE
            sum_subtractions_h = subtraction_h + subtraction_other_h
            sum_subtractions_l = subtraction_l + subtraction_other_l
            new_help_ind_share_substractions_l = (new_sum_subtractions_l_1 + cu(1.4997))/(new_num_low)  # aufrunden
            new_ind_share_substractions_l_1 = new_help_ind_share_substractions_l
            new_ind_share_substractions_l_2 = new_sum_subtractions_l_2 / new_num_low
            new_ind_share_substractions_h_1 = new_sum_subtractions_h_1 / new_num_high
            new_ind_share_substractions_h_2 = new_sum_subtractions_h_2 / new_num_high
            
            help_ind_share_substractions_l = (sum_subtractions_l +cu(1.4997))/(num_others + 1) # aufrunden
            ind_share_substractions_l = help_ind_share_substractions_l
            new_sum_round_l_1 = r_income - subtraction_l + new_ind_share_substractions_l_1
            new_sum_round_h_1 = r_income - subtraction_h + new_ind_share_substractions_h_1
            new_sum_round_l_2 = r_income - subtraction_l + new_ind_share_substractions_l_2
            new_sum_round_h_2 = r_income - subtraction_h + new_ind_share_substractions_h_2
            sum_round_l = r_income - subtraction_l + ind_share_substractions_l
            sum_round_l_D = r_other_income_D - subtraction_other_l_D + ind_share_substractions_l
            sum_round_l_E = r_other_income_E - subtraction_other_l_E + ind_share_substractions_l
            ind_share_substractions_h = sum_subtractions_h/(num_others + 1)
            sum_round_h = r_income - subtraction_h + ind_share_substractions_h
            sum_round_h_D = r_other_income_D - subtraction_other_h_D + ind_share_substractions_h
            sum_round_h_E = r_other_income_E - subtraction_other_h_E + ind_share_substractions_h
            point_euro = Constants.MULTIPLICATOR * 10
            return dict(low_percentage=low_percentage,
            high_percentage=high_percentage,
            new_num_high = new_num_high,
            new_num_low = new_num_low,
            new_sum_subtractions_l_1 = new_sum_subtractions_l_1,
            new_sum_subtractions_h_1 = new_sum_subtractions_h_1,
            new_sum_subtractions_l_2 = new_sum_subtractions_l_2,
            new_sum_subtractions_h_2 = new_sum_subtractions_h_2,
            new_ind_share_substractions_l_1 = new_ind_share_substractions_l_1,
            new_ind_share_substractions_h_1 = new_ind_share_substractions_h_1,
            new_ind_share_substractions_l_2 = new_ind_share_substractions_l_2,
            new_ind_share_substractions_h_2 = new_ind_share_substractions_h_2,
            new_r_income_sub_l_1  = new_r_income_sub_l_1 ,
            new_r_income_sub_h_1  = new_r_income_sub_h_1 ,
            new_r_income_sub_l_2=new_r_income_sub_l_2,
            new_r_income_sub_h_2=new_r_income_sub_h_2,
            new_sum_round_l_1 = new_sum_round_l_1 ,
            new_sum_round_h_1 = new_sum_round_h_1 ,
            new_sum_round_l_2 = new_sum_round_l_2 ,
            new_sum_round_h_2 = new_sum_round_h_2 ,
            new_average_income_l_1 = new_average_income_l_1 ,
            new_average_income_h_1 = new_average_income_h_1 ,
            new_average_income_l_2 = new_average_income_l_2 ,
            new_average_income_h_2 = new_average_income_h_2 ,
            num_p =num_p ,
            r_income =r_income,
            subtraction_l =subtraction_l ,
            r_income_sub_l =r_income_sub_l ,
            r_other_income =r_other_income ,
            subtraction_other_l = subtraction_other_l ,
            sum_subtractions_l =sum_subtractions_l ,
            ind_share_substractions_l =ind_share_substractions_l,
            sum_round_l =sum_round_l,
            subtraction_h =subtraction_h ,
            r_income_sub_h =r_income_sub_h ,
            subtraction_other_h = subtraction_other_h ,
            sum_subtractions_h =sum_subtractions_h ,
            ind_share_substractions_h =ind_share_substractions_h,
            sum_round_h =sum_round_h,
            r_other_income_D =r_other_income_D ,
            r_other_income_E =r_other_income_E ,
            subtraction_other_l_D = subtraction_other_l_D,
            subtraction_other_l_E = subtraction_other_l_E,
            subtraction_other_h_D = subtraction_other_h_D,
            subtraction_other_h_E = subtraction_other_h_E,
            point_euro =point_euro,
            r_income_other_sub_l_D =r_income_other_sub_l_D ,
            r_income_other_sub_l_E =r_income_other_sub_l_E ,
            r_income_other_sub_h_D =r_income_other_sub_h_D ,
            r_income_other_sub_h_E =r_income_other_sub_h_E ,
            sum_round_l_D =sum_round_l_D ,
            sum_round_l_E =sum_round_l_E ,
            sum_round_h_D =sum_round_h_D ,
            sum_round_h_E =sum_round_h_E ,
            )


class Examples(Page):
        @staticmethod
        def is_displayed(player):
            return player.round_number == 1

        @staticmethod
        def vars_for_template(player: Player):
            low_percentage = percentage(Constants.low_percentage_rate, 100)
            high_percentage = percentage(Constants.high_percentage_rate, 100)
            r_income = Constants.MULTIPLICATOR * 25
            subtraction_l = r_income * Constants.LOW_RATE
            subtraction_h = r_income * Constants.HIGH_RATE
            r_income_sub_l = r_income - subtraction_l
            r_income_sub_h = r_income - subtraction_h
            new_r_income_sub_l_1 = r_income - subtraction_l
            new_r_income_sub_h_1 = r_income - subtraction_h
            new_r_income_sub_l_2 = r_income - subtraction_l
            new_r_income_sub_h_2 = r_income - subtraction_h
            r_other_income_D = Constants.MULTIPLICATOR * 15
            r_other_income_E = Constants.MULTIPLICATOR * 30
            r_other_income = r_other_income_D + r_other_income_E
            new_r_all_other_income_1 = Constants.MULTIPLICATOR * 150
            new_r_all_other_income_2 = Constants.MULTIPLICATOR * 250
            new_num_high = round(
                Constants.players_per_group - (Constants.players_per_group/2))
            new_num_low = round(Constants.players_per_group - new_num_high)
            new_average_income_l_1 = (
                r_income + new_r_all_other_income_1)/new_num_low
            new_average_income_h_1 = (
                r_income + new_r_all_other_income_1)/new_num_high
            new_average_income_l_2 = (
                r_income + new_r_all_other_income_2)/new_num_low
            new_average_income_h_2 = (
                r_income + new_r_all_other_income_2)/new_num_high
            num_others = 2
            num_p = num_others + 1
            subtraction_other_l = r_other_income * Constants.LOW_RATE
            subtraction_other_l_D = r_other_income_D * Constants.LOW_RATE
            subtraction_other_l_E = r_other_income_E * Constants.LOW_RATE
            subtraction_other_h_D = r_other_income_D * Constants.HIGH_RATE
            subtraction_other_h_E = r_other_income_E * Constants.HIGH_RATE
            r_income_other_sub_l_D = r_other_income_D - subtraction_other_l_D
            r_income_other_sub_l_E = r_other_income_E - subtraction_other_l_E
            r_income_other_sub_h_D = r_other_income_D - subtraction_other_h_D
            r_income_other_sub_h_E = r_other_income_E - subtraction_other_h_E
            subtraction_other_h = r_other_income * Constants.HIGH_RATE
            new_sum_subtractions_l_1 = new_r_all_other_income_1 * Constants.LOW_RATE
            new_sum_subtractions_h_1 = new_r_all_other_income_1 * Constants.HIGH_RATE
            new_sum_subtractions_l_2 = new_r_all_other_income_2 * Constants.LOW_RATE
            new_sum_subtractions_h_2 = new_r_all_other_income_2 * Constants.HIGH_RATE
            sum_subtractions_h = subtraction_h + subtraction_other_h
            sum_subtractions_l = subtraction_l + subtraction_other_l
            new_help_ind_share_substractions_l = (
                new_sum_subtractions_l_1 + cu(1.4997))/(new_num_low)  # aufrunden
            new_ind_share_substractions_l_1 = new_help_ind_share_substractions_l
            new_ind_share_substractions_l_2 = new_sum_subtractions_l_2 / new_num_low
            new_ind_share_substractions_h_1 = new_sum_subtractions_h_1 / new_num_high
            new_ind_share_substractions_h_2 = new_sum_subtractions_h_2 / new_num_high

            help_ind_share_substractions_l = (sum_subtractions_l + cu(1.4997))/(num_others + 1)  # aufrunden
            ind_share_substractions_l = help_ind_share_substractions_l
            new_sum_round_l_1 = r_income - subtraction_l + new_ind_share_substractions_l_1
            new_sum_round_h_1 = r_income - subtraction_h + new_ind_share_substractions_h_1
            new_sum_round_l_2 = r_income - subtraction_l + new_ind_share_substractions_l_2
            new_sum_round_h_2 = r_income - subtraction_h + new_ind_share_substractions_h_2
            sum_round_l = r_income - subtraction_l + ind_share_substractions_l
            sum_round_l_D = r_other_income_D - \
                subtraction_other_l_D + ind_share_substractions_l
            sum_round_l_E = r_other_income_E - \
                subtraction_other_l_E + ind_share_substractions_l
            ind_share_substractions_h = sum_subtractions_h/(num_others + 1)
            sum_round_h = r_income - subtraction_h + ind_share_substractions_h
            sum_round_h_D = r_other_income_D - \
                subtraction_other_h_D + ind_share_substractions_h
            sum_round_h_E = r_other_income_E - \
                subtraction_other_h_E + ind_share_substractions_h
            point_euro = Constants.MULTIPLICATOR * 10
            return dict(low_percentage=low_percentage,
                        high_percentage=high_percentage,
                        new_num_high= new_num_high,
                        new_num_low= new_num_low,
                        new_sum_subtractions_l_1= new_sum_subtractions_l_1,
                        new_sum_subtractions_h_1= new_sum_subtractions_h_1,
                        new_sum_subtractions_l_2= new_sum_subtractions_l_2,
                        new_sum_subtractions_h_2= new_sum_subtractions_h_2,
                        new_ind_share_substractions_l_1= new_ind_share_substractions_l_1,
                        new_ind_share_substractions_h_1= new_ind_share_substractions_h_1,
                        new_ind_share_substractions_l_2= new_ind_share_substractions_l_2,
                        new_ind_share_substractions_h_2= new_ind_share_substractions_h_2,
                        new_r_income_sub_l_1  = new_r_income_sub_l_1,
                        new_r_income_sub_h_1  = new_r_income_sub_h_1,
                        new_r_income_sub_l_2=new_r_income_sub_l_2,
                        new_r_income_sub_h_2=new_r_income_sub_h_2,
                        new_sum_round_l_1 = new_sum_round_l_1,
                        new_sum_round_h_1 = new_sum_round_h_1,
                        new_sum_round_l_2 = new_sum_round_l_2,
                        new_sum_round_h_2 = new_sum_round_h_2,
                        new_average_income_l_1 = new_average_income_l_1,
                        new_average_income_h_1 = new_average_income_h_1,
                        new_average_income_l_2 = new_average_income_l_2,
                        new_average_income_h_2 = new_average_income_h_2,
                        num_p =num_p,
                        r_income=r_income,
                        subtraction_l =subtraction_l,
                        r_income_sub_l =r_income_sub_l,
                        r_other_income =r_other_income,
                        subtraction_other_l = subtraction_other_l,
                        sum_subtractions_l =sum_subtractions_l,
                        ind_share_substractions_l=ind_share_substractions_l,
                        sum_round_l=sum_round_l,
                        subtraction_h =subtraction_h,
                        r_income_sub_h =r_income_sub_h,
                        subtraction_other_h = subtraction_other_h,
                        sum_subtractions_h =sum_subtractions_h,
                        ind_share_substractions_h=ind_share_substractions_h,
                        sum_round_h=sum_round_h,
                        r_other_income_D =r_other_income_D,
                        r_other_income_E =r_other_income_E,
                        subtraction_other_l_D= subtraction_other_l_D,
                        subtraction_other_l_E= subtraction_other_l_E,
                        subtraction_other_h_D= subtraction_other_h_D,
                        subtraction_other_h_E= subtraction_other_h_E,
                        point_euro=point_euro,
                        r_income_other_sub_l_D =r_income_other_sub_l_D,
                        r_income_other_sub_l_E =r_income_other_sub_l_E,
                        r_income_other_sub_h_D =r_income_other_sub_h_D,
                        r_income_other_sub_h_E =r_income_other_sub_h_E,
                        sum_round_l_D =sum_round_l_D,
                        sum_round_l_E =sum_round_l_E,
                        sum_round_h_D =sum_round_h_D,
                        sum_round_h_E =sum_round_h_E,
                        )
class Control1(Page):
        form_model = 'player'
        if Constants.treatment == 'BASE':
            form_fields = ['B_control1']
        elif Constants.treatment == 'TAX_RANDOM':
            form_fields = ['TR_control1']
        elif Constants.treatment == 'INCOME_RANDOM':
            form_fields = ['IR_control1']

        @staticmethod
        def is_displayed(player):
            return player.round_number == 1
        
        def error_message(player: Player, values):
            if Constants.treatment == 'BASE':
                solutions = dict(B_control1=Constants.players_per_group)
            elif Constants.treatment == 'TAX_RANDOM':
                solutions = dict(TR_control1=Constants.players_per_group)
            elif Constants.treatment == 'INCOME_RANDOM':
                solutions = dict(IR_control1=Constants.players_per_group)

            if values != solutions:
                return "Diese Antwort ist falsch. Bitte versuchen Sie es nochmal."


class Control2(Page):
        form_model = 'player'
        if Constants.treatment == 'BASE':
            form_fields = ['B_control2']
        elif Constants.treatment == 'TAX_RANDOM':
            form_fields = ['TR_control2']
        elif Constants.treatment == 'INCOME_RANDOM':
            form_fields = ['IR_control2']

        @staticmethod
        def is_displayed(player):
            return player.round_number == 1

        def error_message(player: Player, values):
            if Constants.treatment == 'BASE':
                solutions = dict(B_control2=200)
            elif Constants.treatment == 'TAX_RANDOM':
                solutions = dict(TR_control2=200)
            elif Constants.treatment == 'INCOME_RANDOM':
                solutions = dict(IR_control2=200)

            if values != solutions:
                return "Diese Antwort ist falsch. Bitte versuchen Sie es nochmal."


class Control3(Page):
        form_model = 'player'
        #form_fields = ['B_control3', 'B_control4', 'B_control5', 'B_control6']
        if Constants.treatment == 'BASE':
            form_fields = ['B_control3', 'B_control5']
        elif Constants.treatment == 'TAX_RANDOM':
            form_fields = ['TR_control3', 'TR_control5']
        elif Constants.treatment == 'INCOME_RANDOM':
            form_fields = ['IR_control3', 'IR_control5']

        @staticmethod
        def is_displayed(player):
            return player.round_number == 1

        def error_message(player: Player, values):
            #solutions = dict(B_control3=1, B_control5=1)
            if Constants.treatment == 'BASE':
                solutions = dict(B_control3=1,
                                 B_control5=1)
            elif Constants.treatment == 'TAX_RANDOM':
                solutions = dict(TR_control3=1,
                             TR_control5=1)
            elif Constants.treatment == 'INCOME_RANDOM':
                solutions = dict(IR_control3=1, 
                                 IR_control5=1)

            if values != solutions:
                return "Diese Antwort ist falsch. Bitte versuchen Sie es nochmal."


class Control4(Page):
        form_model = 'player'
       # form_fields = ['B_control3', 'B_control4', 'B_control5', 'B_control6']
        if Constants.treatment == 'BASE':
            form_fields = ['B_control7']
        elif Constants.treatment == 'TAX_RANDOM':
            form_fields = ['TR_control7']
        elif Constants.treatment == 'INCOME_RANDOM':
            form_fields = ['IR_control7']

        @staticmethod
        def is_displayed(player):
            return player.round_number == 1

        def error_message(player: Player, values):
            # solutions = dict(B_control3=1, B_control5=1)
            if Constants.treatment == 'BASE':
                solutions = dict(B_control7=1)
            elif Constants.treatment == 'TAX_RANDOM':
                solutions = dict(TR_control7=1)
            elif Constants.treatment == 'INCOME_RANDOM':
                solutions = dict(IR_control7=1)

            if values != solutions:
                return "Diese Antwort ist falsch. Bitte versuchen Sie es nochmal."
        
        @staticmethod
        def vars_for_template(player: Player):
            low_percentage = percentage(Constants.low_percentage_rate, 100)
            return dict(low_percentage=low_percentage)

class PreDecision(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Decision(Page):
    if Constants.treatment == 'BASE' or Constants.treatment == 'INCOME_RANDOM':
        form_model = 'player'
        form_fields = ['decision']

        @staticmethod
        def vars_for_template(player: Player):
            low_percentage = percentage(Constants.low_percentage_rate, 100)
            high_percentage = percentage(
                Constants.high_percentage_rate, 100)
            return dict(low_percentage=low_percentage,
                        high_percentage=high_percentage,
                        )
    if Constants.treatment == 'TAX_RANDOM':
        @staticmethod
        def vars_for_template(player: Player):
            low_percentage = percentage(Constants.low_percentage_rate, 100)
            high_percentage = percentage(
                Constants.high_percentage_rate, 100)
            return dict(low_percentage=low_percentage,
                        high_percentage=high_percentage,
                        )


class Instruction_Game(Page):
        @staticmethod
        def is_displayed(player):
            return player.round_number == 1

        @staticmethod
        def vars_for_template(player: Player):
            timeout_minutes = int(Constants.timeout_seconds/60)
            return dict(timeout_minutes=timeout_minutes,
            )

class PlayersWaitPage(WaitPage):
    template_name = __name__ + '/MyEncryptioWaitPage.html'
    after_all_players_arrive = 'group_size'

    @staticmethod
    def vars_for_template(player: Player):
            timeout_minutes = int(Constants.timeout_seconds/60)
            low_percentage = percentage(Constants.low_percentage_rate, 100)
            high_percentage = percentage(Constants.high_percentage_rate, 100)
            return dict(timeout_minutes=timeout_minutes, low_percentage=low_percentage, high_percentage=high_percentage,
            )

class Go_Game(Page):

        @staticmethod
        def vars_for_template(player: Player):
            timeout_minutes = int(Constants.timeout_seconds/60)
            low_percentage = percentage(Constants.low_percentage_rate, 100)
            high_percentage = percentage(Constants.high_percentage_rate, 100)
            return dict(timeout_minutes=timeout_minutes, low_percentage=low_percentage, high_percentage=high_percentage,
            )

class Game_cleaned(Page):
    timeout_seconds = Constants.timeout_seconds

    live_method = play_game

    @staticmethod
    def js_vars(player: Player):
        return dict(params=player.session.params)

    @staticmethod
    def vars_for_template(player: Player):
        task_module = get_task_module(player)
        timeout_minutes = int(Constants.timeout_seconds/60)
        return dict(DEBUG=settings.DEBUG,
                    input_type=task_module.INPUT_TYPE,
                    placeholder=task_module.INPUT_HINT,
                    timeout_minutes=timeout_minutes,
                    )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if not timeout_happened and not player.session.params['max_iterations']:
            raise RuntimeError("malicious page submission")

        participant = player.participant
        participant.num_correct = player.num_correct
        participant.fake_num_correct = player.fake_num_correct
        participant.income = player.num_correct * Constants.MULTIPLICATOR
        player.income = participant.income

class ResultsWaitPage(WaitPage):
    template_name = __name__ + '/MyWaitPage.html'
    after_all_players_arrive = 'set_payoffs'
    #   <meta http-equiv="refresh" content="30">

class InitialBelief(Page):
    form_model = 'player'
    form_fields = ['belief1']
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class ResultsWaitPage2(WaitPage):
    template_name = __name__ + '/MyWaitPage.html'
    after_all_players_arrive = 'evaluation'
    #   <meta http-equiv="refresh" content="30">


class Weiter(Page):
    pass

class Beliefs_Intro(Page):
    @staticmethod
    def is_displayed(player: Player):
            final_round = Constants.num_rounds
            return player.round_number == final_round #and Constants.treatment == 'Base' or Constants.treatment == 'TAX_RANDOM'
class Beliefs1(Page):
    form_model = 'player'
    form_fields = ['belief3']

    @staticmethod
    def is_displayed(player: Player):
            final_round = Constants.num_rounds
            return player.round_number == final_round #and Constants.treatment == 'Base' or Constants.treatment == 'TAX_RANDOM'
class Beliefs2(Page):
    form_model = 'player'
    form_fields = ['belief2']

    @staticmethod
    def is_displayed(player: Player):
            final_round = Constants.num_rounds
            return player.round_number == final_round #and Constants.treatment == 'Base' or Constants.treatment == 'TAX_RANDOM'


class Feedback(Page):
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        participant.income = player.num_correct * Constants.MULTIPLICATOR
        player.income_at = participant.income - player.taxes_paid_low - player.taxes_paid_high
        low_percentage = percentage(Constants.low_percentage_rate,100)
        high_percentage = percentage(Constants.high_percentage_rate,100)
        correct = int(player.belief_bonus1/50) + int(player.belief_bonus2/50) + int(player.belief_bonus3/50)
        belief_bonus = cu(player.belief_bonus1) + \
            cu(player.belief_bonus2) + cu(player.belief_bonus3)

        return dict(
            income_at = player.income_at,
            low_percentage = low_percentage,
            high_percentage = high_percentage,
            correct=correct,
            belief_bonus = belief_bonus,

        )

class Results(Page):
    pass

class Transmission(Page):
        def is_displayed(player: Player):
            final_round = Constants.num_rounds
            return player.round_number == final_round


page_sequence = [Welcome, Examples, Control3, Control4, PreDecision, Decision, Instruction_Game, PlayersWaitPage,
                 Go_Game, Game_cleaned, InitialBelief, Beliefs_Intro, Beliefs1, Beliefs2, ResultsWaitPage2, Weiter, ResultsWaitPage, Feedback, Transmission]
# page_sequence = [Welcome, Decision, Instruction_Game, PlayersWaitPage, Go_Game, Game_cleaned, ResultsWaitPage, Beliefs, Feedback, Transmission]
