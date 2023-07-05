from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'confi'
    PLAYERS_PER_GROUP = 16
    NUM_ROUNDS = 1
    Prize_correct = cu(25)
    timeout_seconds = 120


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    average = models.FloatField()


class Player(BasePlayer):
    statistics_before = models.BooleanField(
    choices=[
            [False, 'Nein'],
            [True, 'Ja'],
    ],
    label='Haben Sie einen Kurs belegt, der Wahrscheinlichkeitstheorie beinhaltet (z. B. Statistik)?',
    widget=widgets.RadioSelect,
    )

    difficulty = models.StringField(
        choices=[['Sehr schwierig', 'Sehr schwierig'],
                ['Schwierig', 'Schwierig'],
                ['Leicht', 'Leicht'],
                ['Sehr leicht', 'Sehr leicht']],
        label='Wie schwierig war das Experiment?',
        widget=widgets.RadioSelect,
    )

    crt_bat = models.IntegerField(
                                  min=0, max=1000,
                                  label="Ein Schläger und ein Ball kosten insgesamt 22 Euro. Der Schläger kostet 20 Euro mehr als der Ball. Wie viele Euro kostet der Ball?",
    )
    crt_widget = models.IntegerField(
    label='''
        Wenn 5 Maschinen 5 Minuten brauchen, um 5 Geräte herzustellen, wie viele Minuten bräuchten dann 100 Maschinen, um 100 Geräte herzustellen?
        ''',
    )
    crt_lake = models.IntegerField(min=0, max=1000,
    label='''
        In einem See gibt es einen Fleck mit Seerosenblättern.
        Jeden Tag verdoppelt sich die Größe des Flecks.
        Wenn es 48 Tage dauert, bis der Fleck den ganzen See bedeckt,
        wie viele Tage würde es dauern, bis der Fleck die Hälfte des Sees bedeckt hat?
        ''',
    )

    sheep = models.IntegerField(  # (intuitive response = 7; correct response = 8; Thomson and Oppenheimer 2016)
    label='''
    Ein Bauer hatte 15 Schafe, von denen alle bis auf 8 starben. Wie viele sind übrig geblieben?
    ''',
    )

    line = models.IntegerField(  # (intuitive    responses=31 or 30; correct response=29; Ackerman    2014)
    label='''
    Steve stand in einer langen Schlange. Um sich zu amüsieren, zählte er die Wartenden und stellte fest, dass er der 15. vom Anfang und der 15. vom Ende der Schlange war. Wie viele Leute standen in der Schlange?
    ''',
    )

    run = models.IntegerField(  # (intuitive response = 90;    correct response=40; Van Dooren et al. 2005)
    label='''
    Ellen und Kim laufen auf einer Laufbahn. Sie laufen gleich schnell, aber Ellen hat später angefangen. Wenn Ellen 5 Runden gelaufen ist, ist Kim 15 Runden gelaufen. Wenn Ellen 30 Runden gelaufen ist, wie viele Runden ist Kim gelaufen?
''',
    )

    month = models.IntegerField (
    label='''
    Ein Monat des Jahres hat in der Regel nur 28 Tage. Wie viele der übrigen 11 Monate haben 30 Tage?
    ''',
    )

    second = models.IntegerField(
    label='''
    Wenn Sie ein Rennen laufen würden und den Zweitplatzierten überholen würden, welchen Platz würden Sie jetzt einnehmen?
    ''',
    )


# Self evaluation and Performance
    crt_confidence = models.IntegerField(
    label='''
       Wie viele richtige Antworten haben Sie bei den eben gestellten 8 Fragen gegeben?''',
    min=0,
    max=8
    )
    crt_better = models.BooleanField(
    label='''
        Haben Sie im vorherigen Test besser abgeschnitten als der Durchschnitt der Teilnehmer?''',
    choices=[
        [False, 'Nein'],
        [True, 'Ja'],
    ]
    )

    self_better = models.BooleanField()
    correct_relative_performance = models.BooleanField()
    crt_performance = models.IntegerField(
        min=0,
        max=8)
    self_evaluation = models.BooleanField()
    


# FUNCTIONS
def evaluation(group):
    players = group.get_players()
    group.average = sum(p.crt_performance for p in players)/len(players)
    for p in players:
        p.self_evaluation = p.crt_confidence == p.crt_performance
        p.self_better = p.crt_performance > group.average
        p.correct_relative_performance = p.self_better == p.crt_better


# PAGES
class Intro(Page):
    pass

class CRT1(Page):
    timeout_seconds = 120
    form_model = 'player'
    form_fields = ['crt_bat', 'crt_widget', 'crt_lake', 'second']


class CRT2(Page):
    timeout_seconds = 120
    form_model = 'player'
    form_fields = ['sheep', 'line', 'run', 'month']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.crt_performance = ((player.crt_bat == 1) +
                                  (player.crt_widget == 5) +
                                  (player.crt_lake == 47) +
                                  (player.sheep == 8) +
                                  (player.line == 29) + 
                                  (player.run == 40 ) + 
                                  (player.month == 11) +
                                  (player.second == 2)
                                  )


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'evaluation'


class Weiter(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # Accuracy of prediction
        self_evaluation = player.crt_confidence == player.crt_performance
        accuracy = self_evaluation

        player.payoff = (accuracy + player.crt_performance +
                         player.correct_relative_performance) * C.Prize_correct


class Confi(Page):
    form_model = 'player'
    form_fields = ['crt_confidence', 'crt_better']


class Results(Page):
    pass


page_sequence = [
    Intro,
    CRT1,
    CRT2,
    Confi,
    ResultsWaitPage,
    Weiter,
    Results
]
