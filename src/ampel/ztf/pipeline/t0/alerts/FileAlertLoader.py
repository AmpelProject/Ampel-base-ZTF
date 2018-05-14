#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : ampel/pipeline/t0/alerts/FileAlertLoader.py
# License           : BSD-3-Clause
# Author            : vb <vbrinnel@physik.hu-berlin.de>
# Date              : 30.04.2018
# Last Modified Date: 14.05.2018
# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>


from ampel.abstract.AbsAlertLoader import AbsAlertLoader
from ampel.pipeline.logging.LoggingUtils import LoggingUtils
import logging, io


class FileAlertLoader(AbsAlertLoader):


	def __init__(self, files=None, logger=None):
		""" 
		"""
		self.logger = LoggingUtils.get_logger() if logger is None else logger
		self.iter_files = None
		self.files = []

		if files is not None:
			self.add_files(files)


	def add_files(self, arg):
		"""
		"""
		if type(arg) is str:
			arg = [arg]

		for fp in arg:
			self.files.append(fp)
			self.logger.debug("Adding " + str(len(fp)) + " files to the list")

		self.iter_files = iter(self.files)


	def get_files(self):
		"""
		"""
		for fpath in self.iter_files:
			alert_file = open(fpath, "rb")
			yield alert_file
			alert_file.close()