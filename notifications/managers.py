from django.contrib.contenttypes.models import ContentType
from django.db import models


class NotificationManager(models.Manager):
    def unread_count(self, user):
        return self.filter(recipient=user, readed=False).count()

    def mark_all_as_read(self, recipient):
        return self.filter(recipient=recipient, readed=False).update(readed=True)

    def withdraw(self, sender, recipient, verb, action_object, target):
      actor_type = ContentType.objects.get_for_model(sender)
      action_object_type = ContentType.objects.get_for_model(action_object)
      target_type = ContentType.objects.get_for_model(target)
      return self.filter(
        #readed = False,
        actor_content_type = actor_type,
        actor_object_id = sender.id,
        recipient = recipient,
        verb = verb,
        action_object_content_type = action_object_type,
        action_object_object_id = action_object.id,
        target_content_type = target_type,
        target_object_id = target.id
      ).delete()