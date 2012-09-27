# -*- coding: utf-8 -*-

from django.contrib import admin
from notifications.models import Notification

class NotificationAdmin(admin.ModelAdmin):
  list_display = ('recipient', 'actor', 'verb', 'description', 'target', 'action_object', 'timestamp', 'readed', 'public')
  list_filter = ('recipient', 'actor', 'verb')

  def actor(self, obj):
    return obj.actor

  def target(self, obj):
    return obj.target

  def action_object(self, obj):
    return obj.action_object
admin.site.register(Notification, NotificationAdmin)
