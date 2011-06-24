# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Category.url'
        db.add_column('riddles_category', 'url', self.gf('django.db.models.fields.CharField')(default='', max_length=128), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Category.url'
        db.delete_column('riddles_category', 'url')


    models = {
        'riddles.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'})
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
