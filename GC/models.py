# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import six
from django.utils.translation import gettext_lazy as _

# Dónde ibamos a colocar el tipo de competición (liga o copa)

@python_2_unicode_compatible
class Season (models.Model):
    """
        Season. All season must be associated with a category.
        A season includes a year of competition.
        Ex: 2010/2011 or 2012/2013. feb_season_id it will be the first part,
        in this case, 2010 and 2012 respectively.
    """
    name = models.CharField(_('name'), unique=True, max_length=64)
    feb_season_id = models.IntegerField(_('feb id'), unique=True)
    feb_season_name = models.CharField(_('feb name'), max_length=64)
    start_date = models.DateField(_('start date'), null=True)
    end_date = models.DateField(_('end date'), null=True)
    """
    class Meta:
        verbose_name = _('season')
        verbose_name_plural = _('seasons')
    """
    def __str__(self):
        return self.name
# End Class Season     
    

@python_2_unicode_compatible
class Genre (models.Model):
    """
        Genre. It is used to characterize a category.
        The types are male or female.
    """
    name = models.CharField(_('name'), unique=True, max_length=64)
    description = models.CharField(_('description'), max_length=64, null=True)
    """
    class Meta:
        verbose_name = _('genre')
        verbose_name_plural = _('genres')
    """
    def __str__(self):
        return self.name
# End Class Genre


@python_2_unicode_compatible
class Modality (models.Model):
    """
        Modality. It is used to characterize a category.
        The types are. (Ligue or Cup) (normal o wheelchair?)
    """
    name = models.CharField(_('name'), unique=True, max_length=64)
    description = models.CharField(_('description'), max_length=64, null=True)
    
    class Meta:
        verbose_name = _('modality')
        verbose_name_plural = _('modalities')

    def __str__(self):
        return self.name
# End Class Modality


@python_2_unicode_compatible
class Scope (models.Model):
    """
        Scope. It is used to characterize a category.
        The types are national, continental and worldwide.
    """
    name = models.CharField(_('name'), unique=True, max_length=64)
    description = models.CharField(_('description'), max_length=64, null=True)
    
    class Meta:
        verbose_name = _('scope')
        verbose_name_plural = _('scopes')

    def __str__(self):
        return self.name
# End Class Scope


@python_2_unicode_compatible
class Category (models.Model):
    """
        Category. Any competition is completely defined by Category, Genre, Modality, Scope and its phases.
        A category includes a number of teams inside it.
        2013 FEB the categories are:
        - Male: LIGA ENDESA, ORO,  PLATA, LEB BRONCE, EBA, C.Cadete Masc.Sel.Aut.
        - Female: L.F., L.F.-2, EUROLEAGUE WOMEN, EUROCUP WOMEN, 
    """
    name = models.CharField(_('name'), unique=True, max_length=128)
    feb_category_id = models.IntegerField(_('feb id'), unique=True)
    feb_category_name = models.CharField(_('feb name'), unique=True, max_length=128)
    genre = models.ForeignKey(Genre, null=True,default=None, verbose_name=_('genre'))
    modality = models.ForeignKey(Modality, null=True, default= None, verbose_name=_('modality'))
    seasons = models.ManyToManyField(Season, verbose_name=_('seasons'))
    
    
    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name
# End Class Category


@python_2_unicode_compatible
class Team (models.Model):
    """
        Team. A set of players. Can be registered in one or more seasons. Any register have different id. 
    """
    name = models.CharField(_('name'), max_length=128)
    feb_team_name = models.CharField(_('feb name'), max_length=128)
    feb_team_alias = models.CharField(_('feb alias'), max_length=128)
    registrations = models.ManyToManyField(Season, through='TeamRegistrations', verbose_name=_('registrations'))
    
    class Meta:
        verbose_name = _('team')
        verbose_name_plural = _('teams')

    def __str__(self):
        return self.name
# End Class Team


@python_2_unicode_compatible
class TeamRegistrations (models.Model):
    """
        TeamRegistrations. Entity to represent the manytomany relationship between a Team and a Season. 
        Register number must be unique. 
    """
    team = models.ForeignKey(Team, verbose_name=_('team')) 
    season = models.ForeignKey(Season,to_field='name', verbose_name=_('season'))
    feb_registration_id = models.IntegerField(_('feb id'), unique=True)
    category = models.ForeignKey(Category, to_field='name', verbose_name=_('category'))
    
    class Meta:
        verbose_name = _('team registration')
        verbose_name_plural = _('teams registration')
        unique_together = (('team', 'season', 'feb_registration_id'),)

    def __str__(self):
        return "%s | %s | %s" % (
            six.text_type(self.team),
            six.text_type(self.season),
            six.text_type(self.feb_registration_id))
# End Class TeamRegistrations


@python_2_unicode_compatible
class Phase (models.Model):
    """
        Phase. Any category(competition) plays different phases(one or more).
        An example of this, 2013 FEB Oro phases are:
        - Liga Regular, P-O Clasif., Copa Ppe.Asturias, P-O Desc.
    """
    name = models.CharField(_('name'), unique=True, max_length=128)
    feb_phase_id = models.IntegerField(_('feb id'), unique=True)
    feb_phase_name = models.CharField(_('feb name'), unique=True, max_length=128)
    feb_phase_alias = models.CharField(_('feb alias'), max_length=128, null=True)
    category = models.ForeignKey(Category, verbose_name=_('category'))
    season = models.ForeignKey(Season, verbose_name=_('season'))
    
    class Meta:
        verbose_name = _('phase')
        verbose_name_plural = _('phases')

    def __str__(self):
        return self.name
# End Class Phase


@python_2_unicode_compatible
class Group (models.Model):
    """
        Group. Any phase have groups(one or more).
        An example of this, 2013 FEB Oro Liga Regular phase have one group
        and 2013 FEB Oro Copa have 4 groups: octavos, cuartos, semifinales and final.
    """
    name = models.CharField(_('name'), max_length=128)
    feb_group_id = models.IntegerField(_('feb id'), unique=True)
    feb_group_name = models.CharField(_('feb name'), max_length=128)
    phase = models.ForeignKey(Phase, verbose_name=_('phase'))
    
    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')
#         unique_together = (('name', 'feb_group_id', 'feb_group_name'),)

    def __str__(self):
        return self.name
# End Class Group


@python_2_unicode_compatible
class Fixture (models.Model):
    """
        Fixture. A group have a variable number of fixtures (one or more).
    """
    feb_fixture_id = models.IntegerField(_('feb id'), unique=True)
    date = models.DateField(_('date'))
    number = models.IntegerField(_('number'))
    group = models.ForeignKey(Group, verbose_name=_('group'))
    
    class Meta:
        verbose_name = _('fixture')
        verbose_name_plural = _('fixtures')

    def __str__(self):
        return str(self.number) + ' ' + str(self.date)
# End Class Fixture


@python_2_unicode_compatible
class Match (models.Model):
    """
        Match. A fixture have a variable number of matches (one or more).
    """
    feb_match_id = models.IntegerField(_('feb id'), unique=True)
    local_team = models.ForeignKey(Team, related_name='local_team+', verbose_name=_('local team')) # To avoid not to create a backwards relation, +
    visitor_team = models.ForeignKey(Team, related_name='visitor_team+', verbose_name=_('visitor team'))
    date = models.DateField(_('date'), null=True)
    main_refree = models.CharField(_('main refree'), max_length=128, null=True)
    auxiliar_refree = models.CharField(_('auxiliar refree'), max_length=128, null=True)
    place = models.CharField(_('place'), max_length=128, null=True)
    fixture = models.ForeignKey(Fixture, verbose_name=_('fixture'), null=True)
    
#    local_score = models.IntegerField(_('local score'))
#    visitor_score = models.IntegerField(_('visitor score'))
    
    class Meta:
        verbose_name = _('match')
        verbose_name_plural = _('matches')

    def __str__(self):
        return "%s | %s | %s" % (
            six.text_type(self.local_team),
            ' - ',
            six.text_type(self.visitor_team))
# End Class Match


@python_2_unicode_compatible
class StatsMatchTeam (models.Model):
    """
        StatsMatchTeam. Stats for a team in a match.
    """
    team = models.ForeignKey(Team, verbose_name=_('team'))
    match = models.ForeignKey(Match, verbose_name=_('match'))
    score = models.IntegerField(_('score'), null=True)
    partial_scores = models.CharField(_('partial scores'), max_length=128, null=True)
    first_partial = models.IntegerField(_('first partial'), null=True)
    second_partial = models.IntegerField(_('second partial'), null=True)
    third_partial = models.IntegerField(_('third partial'), null=True)
    four_partial = models.IntegerField(_('four partial'), null=True)
    extended_time = models.CharField(_('extended time'), max_length=128, null=True)
    number_extended_times = models.IntegerField(_('number extended times'), null=True)
    
    class Meta:
        verbose_name = _('match stats')
        verbose_name_plural = _('match stats')
        unique_together = (('team', 'match'),)

    def __str__(self):
        return "%s  | %s | %s |%s" % (
            six.text_type(self.team),
            six.text_type(self.partial_scores),
            six.text_type(self.extended_time),
            six.text_type(self.score))
#End Class StatsMatchTeam


@python_2_unicode_compatible
class Person (models.Model):
    """
        Person.
    """
    name = models.CharField(_('name'), max_length=128)
    surname = models.CharField(_('surname'), max_length=128, null=True)
    surname_1 = models.CharField(_('surname 1'), max_length=128)
    surname_2 = models.CharField(_('surname 2'), max_length=128)
    born_date = models.DateField(_('born date'), null=True)
    genre = models.ForeignKey(Genre, verbose_name=_('genre'), null=True)
    photo = models.CharField(_('photo'), max_length=128, null=True)
    height = models.DecimalField(_('height'), max_digits=5, decimal_places=2, null=True) 
    weight = models.DecimalField(_('height'), max_digits=5, decimal_places=2, null=True)
    
    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('persons')

    def __str__(self):
        return "%s  %s  %s" % (
            six.text_type(self.name),
            six.text_type(self.surname_1),
            six.text_type(self.surname_2))
#End Class Person


@python_2_unicode_compatible
class Player (Person):
    """
        Player. The representation of a player.
    """
    feb_id = models.IntegerField(_('feb id'))
    dorsal = models.IntegerField(_('dorsal'), null=True)
    active = models.BooleanField(_('active'))
    teams = models.ManyToManyField(Team, through='PlayerTeam', verbose_name=_('teams') )
    
    class Meta:
        verbose_name = _('player')
        verbose_name_plural = _('players')

    def __str__(self):
        return "%s  | %s | %s |%s" % (
            six.text_type(self.name),
            six.text_type(self.surname_1),
            six.text_type(self.surname_2),
            six.text_type(self.active))
#End Class Player


@python_2_unicode_compatible
class PlayerMedicalLeave (models.Model):
    """
        PlayerMedicalLeave. Player medical leaves.
    """
    player = models.ForeignKey(Player, verbose_name=_('player'))
    start_date = models.DateField(_('start date'))
    end_date = models.DateField(_('end date'), null=True)
    diagnostic = models.CharField(_('diagnostic'), max_length=128, null=True)
    comments = models.CharField(_('comments'), max_length=128, null=True)
    estimated_leave = models.IntegerField(_('estimated leave'), null=True)
    
    class Meta:
        verbose_name = _('player medical leave')
        verbose_name_plural = _('player medical leaves')

    def __str__(self):
        return "%s  | %s | %s |%s" % (
            six.text_type(self.name),
            six.text_type(self.surname_1),
            six.text_type(self.surname_2),
            six.text_type(self.active))
#End Class PlayerMedicalLeave


@python_2_unicode_compatible
class PlayerTeam (models.Model):
    """
        Player. To keep the information about teams in which the player played.
        Entity to represent the manytomany relationship between a Team and Player. 
        Register number must be unique. Date ranges are correlatives.
    """
    player = models.ForeignKey(Player, verbose_name=_('player'))
    team = models.ForeignKey(Team, verbose_name=_('team'))
    start_date = models.DateField(_('start date'), null=True)
    end_date = models.DateField(_('end date'), null=True)
    
    class Meta:
        verbose_name = _('player team')
        verbose_name_plural = _('player teams')
        unique_together = (('player', 'team', 'start_date'),)

    def __str__(self):
        return "%s | %s | %s | %s" % (
            six.text_type(self.player),
            six.text_type(self.team),
            six.text_type(self.start_date),
            six.text_type(self.end_date))
#End Class Player


@python_2_unicode_compatible
class Position (models.Model):
    """
        Position. Position which play the player.
    """
    name = models.CharField(_('description'), unique=True, max_length=128)
    description = models.CharField(_('description'), max_length=128, null=True)
    
    class Meta:
        verbose_name = _('position')
        verbose_name_plural = _('positions')

    def __str__(self):
        return "%s" % (
            six.text_type(self.name))
#End Class Position


@python_2_unicode_compatible
class StatsMatchPlayer (models.Model):
    """
        StatsMatchPlayer. Stats for a player in a match.
    """
    match = models.ForeignKey(Match, verbose_name=_('match'))
    player = models.ForeignKey(Player, verbose_name=_('player'))
    seconds = models.IntegerField(_('seconds'))
    points = models.IntegerField(_('points'))
    point_goals_2 = models.IntegerField(_('2 points goals made'))
    point_goals_2_attempted = models.IntegerField(_('2 points goals attempted'))
    point_goals_3 = models.IntegerField(_('3 points goals made'))
    point_goals_3_attempted = models.IntegerField(_('3 points goals attempted'))
    point_goals_1 = models.IntegerField(_('free throws made'))
    point_goals_1_attempted = models.IntegerField(_('free throws attempted'))
    off_rebounds = models.IntegerField(_('offensive rebounds'))
    def_rebounds = models.IntegerField(_('defensive rebounds'))
    assists = models.IntegerField(_('assists'))
    turnovers = models.IntegerField(_('turnovers'))
    steals = models.IntegerField(_('steals'))
    blocks_pro = models.IntegerField(_('block pro'))
    block_against = models.IntegerField(_('block against'))
    mate = models.IntegerField(_('mate'))
    faults_made = models.IntegerField(_('faults made'))
    faults_received = models.IntegerField(_('faults received'))
    feb_val = models.IntegerField(_('feb val'))
    bm_val = models.IntegerField(_('bm val'))
    starter_player = models.BooleanField(_('starter player'));
    
    class Meta:
        verbose_name = _('match stats')
        verbose_name_plural = _('match stats')
        unique_together = (('match', 'player'),)

    def __str__(self):
        return "%s  | %s | %s |%s" % (
            six.text_type(self.match),
            six.text_type(self.player),
            six.text_type(self.feb_val),
            six.text_type(self.starter_player))
    
    def minutes(self):
        """
            Get the minutes played by a player in a match.
            Format: MM:SS.
        """
        
        # TODO
        
        return 0;
    
    def points_2_percent(self):
        """
            Get the percent for 2 points goals.
        """
        
        # TODO
        
        return 0;
    
    def points_3_percent(self):
        """
            Get the percent for 3 points goals.
        """
        
        # TODO
        
        return 0;
    
    def points_1_percent(self):
        """
            Get the percent for 2 points goals.
        """
        
        # TODO
        
        return 0;
    
    def rebounds_total (self):
        """
            Get the total of rebounds (defensive rebounds + offensive rebounds)
        """
        return self.def_rebounds + self.off_rebounds;
    

def save_player():
    """
    """
    
#End save player

        
#End Class StatsMatchPlayer

