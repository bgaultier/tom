from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

class Hit(models.Model):
	created_date = models.DateTimeField(_(u"Hit date"), auto_now_add=True)
