from ampel.pipeline.t0.filters.AbstractTransientsFilter import AbstractTransientsFilter
from ampel.pipeline.common.flags.TransientFlags import TransientFlags
from random import randint

class RandFilter(AbstractTransientsFilter):

	def __init__(self):
		self.threshold = None

	def set_filter_parameters(self, d):
		self.threshold = d['threshold']

	def apply(self, ztfdict):
		if randint(0, 99) > self.threshold:
			return self.on_match_default_flags
		else:
			return None
