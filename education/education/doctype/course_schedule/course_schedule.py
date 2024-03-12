# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt


from datetime import datetime

import frappe
from frappe import _
from frappe.model.document import Document
import calendar
from datetime import timedelta
from dateutil import relativedelta


class CourseSchedule(Document):
	def validate(self):
		self.instructor_name = frappe.db.get_value(
			"Instructor", self.instructor1
		)
		
		self.validate_time()
	
	
	def validate_time(self):
		"""Validates if from_time is greater than to_time"""
		if self.from_time > self.to_time:
			frappe.throw(_("From Time cannot be greater than To Time."))

	@frappe.whitelist()
	def get_meeting_dates(self):
		meeting_dates = []
		"""Returns a list of meeting dates and also creates a child document for each meeting date with meeting time"""     
		days_of_week = [self.monday, self.tuesday, self.wednesday, self.thursday, self.friday, self.saturday, self.sunday]
		current_date = datetime.strptime(self.c_datestart, "%Y-%m-%d")
		while current_date <= self.c_dateend:
			if days_of_week[current_date.weekday()]:
				meeting_dates.append(current_date)
				current_date += timedelta(days=1)
		return meeting_dates
	@frappe.whitelist()
	def on_update(self):
		"""Create child documents for each meeting date"""
		meeting_dates = self.get_meeting_dates()
		for meeting_date in meeting_dates:
			meeting = frappe.get_doc('course_schedule_meeting_dates')
			meeting.append ("course_schedule_meeting_dates", {
   			"cs_meetdate": meeting_date,
			"cs_from_time": self.from_time,
			"cs_to_time": self.to_time})
			meeting.save()