# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Season'
        db.create_table(u'GC_season', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('feb_season_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('feb_season_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True)),
        ))
        db.send_create_signal(u'GC', ['Season'])

        # Adding model 'Genre'
        db.create_table(u'GC_genre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=64, null=True)),
        ))
        db.send_create_signal(u'GC', ['Genre'])

        # Adding model 'Modality'
        db.create_table(u'GC_modality', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=64, null=True)),
        ))
        db.send_create_signal(u'GC', ['Modality'])

        # Adding model 'Scope'
        db.create_table(u'GC_scope', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=64, null=True)),
        ))
        db.send_create_signal(u'GC', ['Scope'])

        # Adding model 'Category'
        db.create_table(u'GC_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('feb_category_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('feb_category_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('genre', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['GC.Genre'], null=True)),
            ('modality', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['GC.Modality'], null=True)),
        ))
        db.send_create_signal(u'GC', ['Category'])

        # Adding M2M table for field seasons on 'Category'
        m2m_table_name = db.shorten_name(u'GC_category_seasons')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('category', models.ForeignKey(orm[u'GC.category'], null=False)),
            ('season', models.ForeignKey(orm[u'GC.season'], null=False))
        ))
        db.create_unique(m2m_table_name, ['category_id', 'season_id'])

        # Adding model 'Team'
        db.create_table(u'GC_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('feb_team_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('feb_team_alias', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'GC', ['Team'])

        # Adding model 'TeamRegistrations'
        db.create_table(u'GC_teamregistrations', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['GC.Team'])),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['GC.Season'], to_field=u'name')),
            ('feb_registration_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['GC.Category'], to_field=u'name')),
        ))
        db.send_create_signal(u'GC', ['TeamRegistrations'])

        # Adding unique constraint on 'TeamRegistrations', fields ['team', 'season', 'feb_registration_id']
        db.create_unique(u'GC_teamregistrations', ['team_id', 'season_id', 'feb_registration_id'])

        # Adding model 'Phase'
        db.create_table(u'GC_phase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('feb_phase_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('feb_phase_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('feb_phase_alias', self.gf('django.db.models.fields.CharField')(max_length=128, null=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['GC.Category'])),
        ))
        db.send_create_signal(u'GC', ['Phase'])

        # Adding model 'Group'
        db.create_table(u'GC_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('feb_group_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('feb_group_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('phase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['GC.Phase'])),
        ))
        db.send_create_signal(u'GC', ['Group'])

        # Adding model 'Fixture'
        db.create_table(u'GC_fixture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feb_fixture_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['GC.Group'])),
        ))
        db.send_create_signal(u'GC', ['Fixture'])

        # Adding model 'Match'
        db.create_table(u'GC_match', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feb_match_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('local_team', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'local_team+', to=orm['GC.Team'])),
            ('visitor_team', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'visitor_team+', to=orm['GC.Team'])),
            ('date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('main_refree', self.gf('django.db.models.fields.CharField')(max_length=128, null=True)),
            ('auxiliar_refree', self.gf('django.db.models.fields.CharField')(max_length=128, null=True)),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=128, null=True)),
            ('fixture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['GC.Fixture'], null=True)),
        ))
        db.send_create_signal(u'GC', ['Match'])

        # Adding model 'StatsMatchTeam'
        db.create_table(u'GC_statsmatchteam', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['GC.Team'])),
            ('match', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['GC.Match'])),
            ('score', self.gf('django.db.models.fields.IntegerField')()),
            ('partial_scores', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('first_partial', self.gf('django.db.models.fields.IntegerField')()),
            ('second_partial', self.gf('django.db.models.fields.IntegerField')()),
            ('third_partial', self.gf('django.db.models.fields.IntegerField')()),
            ('four_partial', self.gf('django.db.models.fields.IntegerField')()),
            ('extended_time', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('number_extended_times', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'GC', ['StatsMatchTeam'])

        # Adding model 'Person'
        db.create_table(u'GC_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=128, null=True)),
            ('surname_1', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('surname_2', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('born_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('genre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['GC.Genre'], null=True)),
            ('photo', self.gf('django.db.models.fields.CharField')(max_length=128, null=True)),
            ('height', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2)),
            ('weight', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal(u'GC', ['Person'])

        # Adding model 'Player'
        db.create_table(u'GC_player', (
            (u'person_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['GC.Person'], unique=True, primary_key=True)),
            ('feb_id', self.gf('django.db.models.fields.IntegerField')()),
            ('dorsal', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'GC', ['Player'])

        # Adding model 'PlayerMedicalLeave'
        db.create_table(u'GC_playermedicalleave', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['GC.Player'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('diagnostic', self.gf('django.db.models.fields.CharField')(max_length=128, null=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=128, null=True)),
            ('estimated_leave', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'GC', ['PlayerMedicalLeave'])

        # Adding model 'PlayerTeam'
        db.create_table(u'GC_playerteam', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['GC.Player'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['GC.Team'])),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True)),
        ))
        db.send_create_signal(u'GC', ['PlayerTeam'])

        # Adding unique constraint on 'PlayerTeam', fields ['player', 'team', 'start_date']
        db.create_unique(u'GC_playerteam', ['player_id', 'team_id', 'start_date'])

        # Adding model 'Position'
        db.create_table(u'GC_position', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=128, null=True)),
        ))
        db.send_create_signal(u'GC', ['Position'])

        # Adding model 'StatsMatchPlayer'
        db.create_table(u'GC_statsmatchplayer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('match', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['GC.Match'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['GC.Team'])),
            ('seconds', self.gf('django.db.models.fields.IntegerField')()),
            ('points', self.gf('django.db.models.fields.IntegerField')()),
            ('point_goals_2', self.gf('django.db.models.fields.IntegerField')()),
            ('point_goals_2_attempted', self.gf('django.db.models.fields.IntegerField')()),
            ('point_goals_3', self.gf('django.db.models.fields.IntegerField')()),
            ('point_goals_3_attempted', self.gf('django.db.models.fields.IntegerField')()),
            ('point_goals_1', self.gf('django.db.models.fields.IntegerField')()),
            ('point_goals_1_attempted', self.gf('django.db.models.fields.IntegerField')()),
            ('off_rebounds', self.gf('django.db.models.fields.IntegerField')()),
            ('def_rebounds', self.gf('django.db.models.fields.IntegerField')()),
            ('assists', self.gf('django.db.models.fields.IntegerField')()),
            ('turnovers', self.gf('django.db.models.fields.IntegerField')()),
            ('steals', self.gf('django.db.models.fields.IntegerField')()),
            ('blocks_pro', self.gf('django.db.models.fields.IntegerField')()),
            ('block_against', self.gf('django.db.models.fields.IntegerField')()),
            ('mate', self.gf('django.db.models.fields.IntegerField')()),
            ('faults_made', self.gf('django.db.models.fields.IntegerField')()),
            ('faults_received', self.gf('django.db.models.fields.IntegerField')()),
            ('feb_val', self.gf('django.db.models.fields.IntegerField')()),
            ('bm_val', self.gf('django.db.models.fields.IntegerField')()),
            ('starter_player', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'GC', ['StatsMatchPlayer'])


    def backwards(self, orm):
        # Removing unique constraint on 'PlayerTeam', fields ['player', 'team', 'start_date']
        db.delete_unique(u'GC_playerteam', ['player_id', 'team_id', 'start_date'])

        # Removing unique constraint on 'TeamRegistrations', fields ['team', 'season', 'feb_registration_id']
        db.delete_unique(u'GC_teamregistrations', ['team_id', 'season_id', 'feb_registration_id'])

        # Deleting model 'Season'
        db.delete_table(u'GC_season')

        # Deleting model 'Genre'
        db.delete_table(u'GC_genre')

        # Deleting model 'Modality'
        db.delete_table(u'GC_modality')

        # Deleting model 'Scope'
        db.delete_table(u'GC_scope')

        # Deleting model 'Category'
        db.delete_table(u'GC_category')

        # Removing M2M table for field seasons on 'Category'
        db.delete_table(db.shorten_name(u'GC_category_seasons'))

        # Deleting model 'Team'
        db.delete_table(u'GC_team')

        # Deleting model 'TeamRegistrations'
        db.delete_table(u'GC_teamregistrations')

        # Deleting model 'Phase'
        db.delete_table(u'GC_phase')

        # Deleting model 'Group'
        db.delete_table(u'GC_group')

        # Deleting model 'Fixture'
        db.delete_table(u'GC_fixture')

        # Deleting model 'Match'
        db.delete_table(u'GC_match')

        # Deleting model 'StatsMatchTeam'
        db.delete_table(u'GC_statsmatchteam')

        # Deleting model 'Person'
        db.delete_table(u'GC_person')

        # Deleting model 'Player'
        db.delete_table(u'GC_player')

        # Deleting model 'PlayerMedicalLeave'
        db.delete_table(u'GC_playermedicalleave')

        # Deleting model 'PlayerTeam'
        db.delete_table(u'GC_playerteam')

        # Deleting model 'Position'
        db.delete_table(u'GC_position')

        # Deleting model 'StatsMatchPlayer'
        db.delete_table(u'GC_statsmatchplayer')


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
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
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
            'Meta': {'object_name': 'StatsMatchPlayer'},
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
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['GC.Team']"}),
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
            'Meta': {'object_name': 'StatsMatchTeam'},
            'extended_time': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'first_partial': ('django.db.models.fields.IntegerField', [], {}),
            'four_partial': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['GC.Match']"}),
            'number_extended_times': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'partial_scores': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'second_partial': ('django.db.models.fields.IntegerField', [], {}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['GC.Team']"}),
            'third_partial': ('django.db.models.fields.IntegerField', [], {})
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