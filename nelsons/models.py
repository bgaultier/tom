from __future__ import unicode_literals

from django.db import models

class Nelson(models.Model):
	name = models.SlugField(_(u"Name"), help_text=_(u"Enter a valid Nelson name consisting of letters, numbers, underscores or hyphens."), primary_key=True, max_length=24)
	edx_user = models.SlugField(_(u"edX User"), help_text=_(u"Enter a valid edx User ID consisting of letters, numbers, underscores or hyphens."), max_length=32)

	latitude = models.DecimalField(_(u"Latitude"), max_digits = 10, decimal_places = 6, help_text=_(u"Enter a valid latitude like 48.120094"), null = True, blank = True, default = 48.120094)
	longitude = models.DecimalField(_(u"Longitude"), max_digits = 10, decimal_places = 6, help_text=_(u"Enter a valid longitude like -1.629206"), null = True, blank = True, default = -1.629206)

	created_date = models.DateTimeField(_(u"Created date"), auto_now_add=True)
	last_activity = models.DateTimeField(_(u"Last activity"), auto_now = True)

	def __unicode__(self):
		return self.name

	def clean(self):
		self.name = self.name.lower()

	def belongs_to(self, user):
		return user == self.edx_user

	def was_active_recently(self):
		return self.last_activity >= timezone.now() - timedelta(minutes=90)

	was_active_recently.admin_order_field = 'last_activity'
	was_active_recently.boolean = True
	was_active_recently.short_description = _(u"Active recently ?")
