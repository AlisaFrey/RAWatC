from os import environ
DEBUG = False
#DATABASE_URL = "postgres://postgres@localhost/django_db"

SESSION_CONFIGS = [
    dict(
        name="RAWatC",
        display_name="RAWatC",
        num_demo_participants=16,
        expShortName="RAWatC",
        expId=9,
        sessId=1,
        app_sequence=["BASELINE_encryptio", #"risk_elicitation",  "guess",
                      #"dictator", "confi", "altruism_elicitation",
                       "after_survey", "AnonPay"],
        # choose treatment from list ['BASE', 'TAX_RANDOM', 'INCOME_RANDOM', 'PREFERENCES'],
        # treatment='BASE',
        task='decoding',
        attempts_per_puzzle=1,
    ),
    # when updating num_demo_participants=x, also init.py in BASELINE_encryptio, confi, guess


    dict(
        name="RAW",
        display_name="RAW",
        num_demo_participants=16,
        expShortName="RAW",
        expId=9,
        sessId=69,
        app_sequence=["BASELINE_encryptio", "risk_elicitation",  "guess",
                      "dictator", "confi", "altruism_elicitation", "after_survey", "payment"],
        # choose treatment from list ['BASE', 'TAX_RANDOM', 'INCOME_RANDOM', 'PREFERENCES'],
        # treatment='BASE',
        task='decoding',
        attempts_per_puzzle=1,
        ),
    # when updating num_demo_participants=x, also init.py in BASELINE_encryptio, confi, guess

    dict(
        name="RAW2",
        display_name="RAW2",
        num_demo_participants=16,
        expShortName="RAW",
        expId=9,
        sessId=69,
        app_sequence=["risk_elicitation",  "guess",
                      "dictator", "confi", "altruism_elicitation", "after_survey", "payment"],
        # choose treatment from list ['BASE', 'TAX_RANDOM', 'INCOME_RANDOM', 'PREFERENCES'],
        # treatment='BASE',
        task='decoding',
        attempts_per_puzzle=1,
        ),
    # when updating num_demo_participants=x, also init.py in BASELINE_encryptio, confi, guess
    
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee'] decoding


SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.01, participation_fee=5.00, doc=""
)

PARTICIPANT_FIELDS = ['decision','is_dropout','num_correct', 'fake_num_correct','income']
SESSION_FIELDS = ['params','players_per_group']

ROOMS = [
    dict(
        name='dice_lab',
        display_name ='DICE Lab',
        #participant_label_file='C:/otree/dicelab_otree_labels.txt'
    )
]

OTREE_PRODUCTION =1
# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'de'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '8466309363695'
