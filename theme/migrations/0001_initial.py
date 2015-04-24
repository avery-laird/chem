# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ("pages", "0001_initial"),
    )

    def forwards(self, orm):
        # Adding model 'HomePage'
        db.create_table(u'theme_homepage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('header', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('subheader', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('splash', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'theme', ['HomePage'])

        # Adding model 'Slide'
        db.create_table(u'theme_slide', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('homepage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='slides', to=orm['theme.HomePage'])),
            ('image', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'theme', ['Slide'])

        # Adding model 'ExtendedBlog'
        db.create_table(u'theme_extendedblog', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('splash', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'theme', ['ExtendedBlog'])


    def backwards(self, orm):
        # Deleting model 'HomePage'
        db.delete_table(u'theme_homepage')

        # Deleting model 'Slide'
        db.delete_table(u'theme_slide')

        # Deleting model 'ExtendedBlog'
        db.delete_table(u'theme_extendedblog')


    models = {
        u'pages.page': {
            'Meta': {'ordering': "(u'titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2, 3)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'theme.extendedblog': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'ExtendedBlog', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'splash': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'theme.homepage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'HomePage', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'splash': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'subheader': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'theme.slide': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Slide'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'slides'", 'to': u"orm['theme.HomePage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['theme']
