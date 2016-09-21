# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Phase.season'
        db.add_column(u'GC_phase', 'season',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=177, to=orm['GC.Season']),
                      keep_default=False)


        # Changing field 'StatsMatchPlayer.player'
        db.alter_column(u'GC_statsmatchplayer', 'player_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['GC.Player']))
        # Adding unique constraint on 'StatsMatchPlayer', fields ['match', 'player']
        db.create_unique(u'GC_statsmatchplayer', ['match_id', 'player_id'])


        # Changing field 'StatsMatchTeam.extended_time'
        db.alter_column(u'GC_statsmatchteam', 'extended_time', self.gf('django.db.models.fields.CharField')(max_length=128, null=True))

        # Changing field 'StatsMatchTeam.partial_scores'
        db.alter_column(u'GC_statsmatchteam', 'partial_scores', self.gf('django.db.models.fields.CharField')(max_length=128, null=True))

        # Changing field 'StatsMatchTeam.third_partial'
        db.alter_column(u'GC_statsmatchteam', 'third_partial', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'StatsMatchTeam.first_partial'
        db.alter_column(u'GC_statsmatchteam', 'first_partial', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'StatsMatchTeam.score'
        db.alter_column(u'GC_statsmatchteam', 'score', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'StatsMatchTeam.second_partial'
        db.alter_column(u'GC_statsmatchteam', 'second_partial', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'StatsMatchTeam.four_partial'
        db.alter_column(u'GC_statsmatchteam', 'four_partial', self.gf('django.db.models.fields.IntegerField')(null=True))
        # Adding unique constraint on 'StatsMatchTeam', fields ['team', 'match']
        db.create_unique(u'GC_statsmatchteam', ['team_id', 'match_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'StatsMatchTeam', fields ['team', 'match']
        db.delete_unique(u'GC_statsmatchteam', ['team_id', 'match_id'])

        # Removing unique constraint on 'StatsMatchPlayer', fields ['match', 'player']
        db.delete_unique(u'GC_statsmatchplayer', ['match_id', 'player_id'])

        # Deleting field 'Phase.season'
        db.delete_column(u'GC_phase', 'season_id')


        # Changing field 'StatsMatchPlayer.player'
        db.alter_column(u'GC_statsmatchplayer', 'player_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['GC.Team']))

        # Changing field 'StatsMatchTeam.extended_time'
        db.alter_column(u'GC_statsmatchteam', 'extended_time', self.gf('django.db.models.fields.CharField')(default=None, max_length=128))

        # Changing field 'StatsMatchTeam.partial_scores'
        db.alter_column(u'GC_statsmatchteam', 'partial_scores', self.gf('django.db.models.fields.CharField')(default=None, max_length=128))

        # Changing field 'StatsMatchTeam.third_partial'
        db.alter_column(u'GC_statsmatchteam', 'third_partial', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'StatsMatchTeam.first_partial'
        db.alter_column(u'GC_statsmatchteam', 'first_partial', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'StatsMatchTeam.score'
        db.alter_column(u'GC_statsmatchteam', 'score', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'StatsMatchTeam.second_partial'
        db.alter_column(u'GC_statsmatchteam', 'second_partial', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'StatsMatchTeam.four_partial'
        db.alter_column(u'GC_statsmatchteam', 'four_partial', self.gf('django.db.models.fields.IntegerField')(default=0))

    models = {
        u'GC.category': {
            'Meta': {'object_name': 'Category'},
            'feb_category_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'feb_category_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['GC.Genre']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modality': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['GC.Modality']", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'seasons': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['GC.Season']", 'symmetrical': 'False'})
        },
        u'GC.fixture': {
            'Meta': {'object_name': 'Fixture'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'feb_fixture_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['GC.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {})
        },
        u'GC.genre': {
            'Meta': {'object_name': 'Genre'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        u'GC.group': {
            'Meta': {'object_name': 'Group'},
            'feb_group_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'feb_group_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['GC.Phase']"})
        },
        u'GC.match': {
            'Meta': {'object_name': 'Match'},
            'auxiliar_refree': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'feb_match_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'fixture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['GC.Fixture']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'local_team+'", 'to': u"orm['GC.Team']"}),
            'main_refree': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'visitor_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'visitor_team+'", 'to': u"orm['GC.Team']"})
        },
        u'GC.modality': {
            'Meta': {'object_name': 'Modality'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        u'GC.person': {
            'Meta': {'object_name': 'Person'},
            'born_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['GC.Genre']", 'null': 'True'}),
            'height': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'photo': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'surname_1': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'surname_2': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2'})
        },
        u'GC.phase': {
            'Meta': {'object_name': 'Phase'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['GC.Category']"}),
            'feb_phase_alias': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'feb_phase_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'feb_phase_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['GC.Season']"})
        },
        u'GC.player': {
            'Meta': {'object_name': 'Player', '_ormbases': [u'GC.Person']},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'dorsal': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'feb_id': ('django.db.models.fields.IntegerField', [], {}),
            u'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['GC.Person']", 'unique': 'True', 'primary_key': 'True'}),
            'teams': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['GC.Team']", 'through': u"orm['GC.PlayerTeam']", 'symmetrical': 'False'})
        },
        u'GC.playermedicalleave': {
            'Meta': {'object_name': 'PlayerMedicalLeave'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'diagnostic': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'estimated_leave': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['GC.Player']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'GC.playerteam': {
            'Meta': {'unique_together': "((u'player', u'team', u'start_date'),)", 'object_name': 'PlayerTeam'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['GC.Player']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['GC.Team']"})
        },
        u'GC.position': {
            'Meta': {'object_name': 'Position'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'GC.scope': {
            'Meta': {'object_name': 'Scope'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        u'GC.season': {
            'Meta': {'object_name': 'Season'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'feb_season_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'feb_season_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True'})
        },
        u'GC.statsmatchplayer': {
            'Meta': {'unique_together': "((u'match', u'player'),)", 'object_name': 'StatsMatchPlayer'},
            'assists': ('django.db.models.fields.IntegerField', [], {}),
            'block_against': ('django.db.models.fields.IntegerField', [], {}),
            'blocks_pro': ('django.db.models.fields.IntegerField', [], {}),
            'bm_val': ('django.db.models.fields.IntegerField', [], {}),
            'def_rebounds': ('django.db.models.fields.IntegerField', [], {}),
            'faults_made': ('django.db.models.fields.IntegerField', [], {}),
            'faults_received': ('django.db.models.fields.IntegerField', [], {}),
            'feb_val': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['GC.Match']"}),
            'mate': ('django.db.models.fields.IntegerField', [], {}),
            'off_rebounds': ('django.db.models.fields.IntegerField', [], {}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['GC.Player']"}),
            'point_goals_1': ('django.db.models.fields.IntegerField', [], {}),
            'point_goals_1_attempted': ('django.db.models.fields.IntegerField', [], {}),
            'point_goals_2': ('django.db.models.fields.IntegerField', [], {}),
            'point_goals_2_attempted': ('django.db.models.fields.IntegerField', [], {}),
            'point_goals_3': ('django.db.models.fields.IntegerField', [], {}),
            'point_goals_3_attempted': ('django.db.models.fields.IntegerField', [], {}),
            'points': ('django.db.models.fields.IntegerField', [], {}),
            'seconds': ('django.db.models.fields.IntegerField', [], {}),
            'starter_player': ('django.db.models.fields.BooleanField', [], {}),
            'steals': ('django.db.models.fields.IntegerField', [], {}),
            'turnovers': ('django.db.models.fields.IntegerField', [], {})
        },
        u'GC.statsmatchteam': {
            'Meta': {'unique_together': "((u'team', u'match'),)", 'object_name': 'StatsMatchTeam'},
            'extended_time': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'first_partial': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'four_partial': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['GC.Match']"}),
            'number_extended_times': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'partial_scores': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'second_partial': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['GC.Team']"}),
            'third_partial': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'GC.team': {
            'Meta': {'object_name': 'Team'},
            'feb_team_alias': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'feb_team_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'registrations': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['GC.Season']", 'through': u"orm['GC.TeamRegistrations']", 'symmetrical': 'False'})
        },
        u'GC.teamregistrations': {
            'Meta': {'unique_together': "((u'team', u'season', u'feb_registration_id'),)", 'object_name': 'TeamRegistrations'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['GC.Category']", 'to_field': "u'name'"}),
            'feb_registration_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['GC.Season']", 'to_field': "u'name'"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['GC.Team']"})
        }
    }

    complete_apps = ['GC']