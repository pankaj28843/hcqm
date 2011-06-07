# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'HealthCenterType'
        db.create_table('main_healthcentertype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('main', ['HealthCenterType'])

        # Adding model 'HealthCenter'
        db.create_table('main_healthcenter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.HealthCenterType'])),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('main', ['HealthCenter'])

        # Adding model 'RatingCriteria'
        db.create_table('main_ratingcriteria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('max_value', self.gf('django.db.models.fields.FloatField')()),
            ('min_value', self.gf('django.db.models.fields.FloatField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('main', ['RatingCriteria'])

        # Adding model 'Rating'
        db.create_table('main_rating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('health_center', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.HealthCenter'])),
            ('criteria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.RatingCriteria'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('main', ['Rating'])


    def backwards(self, orm):
        
        # Deleting model 'HealthCenterType'
        db.delete_table('main_healthcentertype')

        # Deleting model 'HealthCenter'
        db.delete_table('main_healthcenter')

        # Deleting model 'RatingCriteria'
        db.delete_table('main_ratingcriteria')

        # Deleting model 'Rating'
        db.delete_table('main_rating')


    models = {
        'main.healthcenter': {
            'Meta': {'object_name': 'HealthCenter'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.HealthCenterType']"})
        },
        'main.healthcentertype': {
            'Meta': {'object_name': 'HealthCenterType'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.rating': {
            'Meta': {'object_name': 'Rating'},
            'criteria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.RatingCriteria']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'health_center': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.HealthCenter']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'main.ratingcriteria': {
            'Meta': {'object_name': 'RatingCriteria'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_value': ('django.db.models.fields.FloatField', [], {}),
            'min_value': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['main']
