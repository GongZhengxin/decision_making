from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'StaticVo'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    vo1_b1 = models.IntegerField(label='')
    vo1_b2 = models.IntegerField(label='')
    vo3_p1 = models.IntegerField(label='')
    vo3_p2 = models.IntegerField(label='')
    vo3_p3 = models.IntegerField(label='')
    vo2_m1 = models.IntegerField(label='')
    vo2_m2 = models.IntegerField(label='')

    vt_check = models.BooleanField(label='', choices=[[1, '我明白上述问题均要求我推测*参与者是怎么想的*，而不是我是怎么想的']], widget=widgets.RadioSelectHorizontal)
