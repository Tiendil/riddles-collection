# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('riddles_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('riddles', ['Category'])

        # Adding model 'Riddle'
        db.create_table('riddles_riddle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=1024)),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['riddles.Category'], null=True)),
        ))
        db.send_create_signal('riddles', ['Riddle'])


    def backwards(self, orm):
        
        # Deleting model 'Category'
        db.delete_table('riddles_category')

        # Deleting model 'Riddle'
        db.delete_table('riddles_riddle')


    models = {
        'riddles.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'riddles.riddle': {
            'Meta': {'object_name': 'Riddle'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['riddles.Category']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['riddles']
