# -*- coding: UTF-8 -*-
'''
Created on 29/10/2013

@author: jesusropi
'''

from django.contrib import admin
from GC.models import Season, Genre, Modality, Scope, Category, Team, TeamRegistrations, Phase
from GC.models import Group, Fixture, Match, StatsMatchTeam, Person, Player, PlayerMedicalLeave
from GC.models import PlayerTeam, Position, StatsMatchPlayer


# To registar the models
admin.site.register(Season)
admin.site.register(Genre)
admin.site.register(Modality)
admin.site.register(Scope)
admin.site.register(Category)
admin.site.register(Team)
admin.site.register(TeamRegistrations)
admin.site.register(Phase)
admin.site.register(Group)
admin.site.register(Fixture)
admin.site.register(Match)
admin.site.register(StatsMatchTeam)
admin.site.register(Person)
admin.site.register(Player)
admin.site.register(PlayerMedicalLeave)
admin.site.register(PlayerTeam)
admin.site.register(Position)
admin.site.register(StatsMatchPlayer)