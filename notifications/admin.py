# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from notifications.models import Notification

class NotificationAdmin(admin.ModelAdmin):
  list_display = ('recipient', 'actor', 'verb', 'description', 'target', 'action_object', 'timestamp', 'readed', 'public')
  list_filter = ('recipient', 'verb')

  def actor(self, obj):
    return obj.actor
  actor.short_description = '来源'

  def target(self, obj):
    return obj.target
  target.short_description = '目标'

  def action_object(self, obj):
    return obj.action_object
  action_object.description = '动作对象'

admin.site.register(Notification, NotificationAdmin)
