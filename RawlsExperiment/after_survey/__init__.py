from otree.api import *


doc = """
Survey after the Experiment for Feedback
"""


class C(BaseConstants):
    NAME_IN_URL = 'after_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # https://max.pm/posts/attribution/

    question_0 = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    )

    question_1 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10']],
        widget=widgets.RadioSelectHorizontal(),
        label="Ich habe in jeder Runde versucht so viel Einkommen wie möglich zu erwirtschaften"
    )
# (questions from Cappelen et al.,2022 - wp1277 from 2019, see Drucker 2022)
    question_2 = models.IntegerField(
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

        label="Ich finde es fair, wenn Talent die Einkommensungleichheit bestimmt."
    )

    question_3 = models.LongStringField(
        label="Haben Sie Anmerkungen, Feedback oder möchten Sie uns sonst etwas mitteilen?",blank=True,
    )
# (growth mindset question from Dweck "Mindset:TheNewPsychologyofSuccess." 2006, see Drucker 2022)
    question_4 = models.IntegerField(
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

        label="Ganz gleich, wie viel Talent man hat, man kann es immer noch ein bisschen ändern."
    )
#
    question_5 = models.IntegerField(
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
        label="Man kann jederzeit die eigenen Talente wesentlich verändern.",
    )

   # question_6 = models.LongStringField(
    #    label="Gibt es noch weitere Anmerkungen? Wir freuen uns über jegliches Feedback!",
    #)

    age = models.IntegerField(label='Wie alt sind Sie?', min=13, max=99, blank=True)

    gender = models.IntegerField(
        choices=[[1, 'weiblich'], [2, "männlich"], [3, "divers"]],

        widget=widgets.RadioSelect,

        label="Welchem Geschlecht fühlen Sie sich zugehörig?"
    )

    field = models.StringField(
        choices=[['Wirtschaftswissenschaften', 'Wirtschaftswissenschaften'],
         ['Naturwissenschaften', 'Naturwissenschaften'],
          ['Geisteswissenschaften', 'Geisteswissenschaften'],
           ['Rechtswissenschaften','Rechtswissenschaften'],
            ['Sonstige','Sonstige'],
             ],
        label='Was ist Ihr Studienfach/Ihre Tätigkeit?',
        widget=widgets.RadioSelect,
    )

    experiments = models.StringField(
        choices=[['0', '0'],
         ['1 bis 5', '1 bis 5'],
          ['6 bis 10', '6 bis 10'],
           ['mehr als 10','mehr als 10'],
            ],
        label='An wie vielen wirtschaftswissenschaftlichen Experimenten haben Sie (ungefähr) bereits teilgenommen?',
        widget=widgets.RadioSelect,
    )

# PAGES


class Page0(Page):
    form_model = 'player'
    form_fields = ['question_0']

class Page1(Page):
    form_model = 'player'
    form_fields = ['question_1']

class Page2(Page):
    pass
    form_model = 'player'
    form_fields = ['question_2']

class Page3(Page):
    pass
    form_model = 'player'
    form_fields = ['question_4','question_5']

class Page4(Page):
    form_model = 'player'
    form_fields = ['question_3']

class Page5(Page):
    form_model = 'player'
    form_fields = ['age','gender', 'field', 'experiments']


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Page0, Page1, Page2, Page3, Page4, Page5, Results]
