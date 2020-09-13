import pytest

# How to neable logs for tests
from python.python.classes.todo_sample_app.Meta import Project, InMemoryNotification
import logging

LOGGER = logging.getLogger(__name__)

def test_create_project():
	project = Project('Learn to sell stock')
	assert project, "Project should exist"
	assert project.creation_date

def test_in_memory_notifications():
	notif = InMemoryNotification()
	notif.notify("Hello world!")

	# Properties:
	#	assert notif.goku() # you can't call it like this
	assert notif.goku # but you can call it like this i.e. no () at the end


	# FIXME: this is failing # Fixed! Don't call events with the trailing ()! because its decorated as a property
	events = notif.events
	assert events is not None
	assert len(events) == 1

