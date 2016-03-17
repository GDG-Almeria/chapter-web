# -*- coding: utf-8 -*-

# Project: "GDG Almería"
# Script: handlers.py - Web handlers
# App identifier: gdg-almeria
# URL: www.---.com
# Author: Marcos Manuel Ortega - Indavelopers
# Version: v1.0 - 02/2016


# -- Imports --
import os
import webapp2
import jinja2


# Initialize Jinja2 environment
template_dir = os.path.join(os.path.dirname(__file__), '../templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


# -- Handlers --
class MainHandler(webapp2.RequestHandler):
	def render(self, template, params=None):
		if not params:
			params = {}

		t = jinja_env.get_template(template)

		self.response.out.write(t.render(params))


class StaticPage(MainHandler):
	def get(self):
		templates = {'': 'home.html'}

		page = self.request.path.split('/')[-1]

		try:
			template = templates[page]

		except KeyError:
			template = 'error-404.html'

		self.render(template)


class EventsPage(MainHandler):
	def get(self):
		self.render('events.html')


class EventPage(MainHandler):
	def get(self, event_url):
		if event_url == 'i-women-techmakers-almeria':
			self.render('event.html')

		else:
			self.error(404)

			self.render('error-404.html')


class Webmap(MainHandler):
	def get(self):
		webmap = []     # todo

		webmap = '<br>'.join(webmap)

		self.response.out.write(webmap)


class Error404(MainHandler):
	def get(self):
		self.error(404)

		self.render('error-404.html')
