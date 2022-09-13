from . import __version__ as app_version

app_name = "visa_management"
app_title = "Visa Management"
app_publisher = "Solufy"
app_description = "This module is developed for visa management of employees. It provides details information about Visa Applications, Visa Approvals, Reports for Visa Information, Visa Availability and Visa Usage Details"
app_email = "contact@solufy.in"
app_license = "MIT"

fixtures = [{
    "doctype": "Workflow",
        "filters": {
            "name": [ "in", ["Visa Management"] ]
            }
        },
        {
    "doctype": "Workflow State"
    }
    ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/visa_management/css/visa_management.css"
# app_include_js = "/assets/visa_management/js/visa_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/visa_management/css/visa_management.css"
# web_include_js = "/assets/visa_management/js/visa_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "visa_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "visa_management.utils.jinja_methods",
#	"filters": "visa_management.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "visa_management.install.before_install"
# after_install = "visa_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "visa_management.uninstall.before_uninstall"
# after_uninstall = "visa_management.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "visa_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }


doc_events = {
    'Visa Application': {
        'validate': [
            'visa_management.visa_management.doctype.visa_application.visa_application.validate'
        ],
  },
}
# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"visa_management.tasks.all"
#	],
#	"daily": [
#		"visa_management.tasks.daily"
#	],
#	"hourly": [
#		"visa_management.tasks.hourly"
#	],
#	"weekly": [
#		"visa_management.tasks.weekly"
#	],
#	"monthly": [
#		"visa_management.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "visa_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "visa_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "visa_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"visa_management.auth.validate"
# ]
