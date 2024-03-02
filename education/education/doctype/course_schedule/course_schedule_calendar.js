frappe.views.calendar["Course Schedule"] = {
	field_map: {
		"start": "from_time",
		"end": "to_time",
		"id": "name",
		"title": "course",
		"allDay": "allDay",
	},
	gantt: false,
	order_by: "c.datestart",
	filters: [
		{
			"fieldtype": "Link",
			"fieldname": "course",
			"options": "Course",
			"label": __("Course")
		},
		{
			"fieldtype": "Link",
			"fieldname": "instructor",
			"options": "Instructor",
			"label": __("Instructor")
		},
		{
			"fieldtype": "Link",
			"fieldname": "room",
			"options": "Room",
			"label": __("Room")
		}
	],
	get_events_method: "education.education.api.get_course_schedule_events"
}
