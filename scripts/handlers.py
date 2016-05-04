# -*- coding: utf-8 -*-

# Project: "GDG Almería"
# Script: handlers.py - Page handlers
# App identifier: gdg-almeria
# URL: gdg-almeria.appspot.com
# Author: Marcos Manuel Ortega - Indavelopers
# Version: v1-0 - 05/2016


# -- Imports --
import os
import webapp2
import jinja2

from google.appengine.api import users


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
		if event_url:
			self.render('event.html')

		else:
			self.error(404)

			self.render('error-404.html')


class AdminHandler(MainHandler):
	@staticmethod
	def get_logout_url():
		user = users.get_current_user()

		if user:
			return users.create_logout_url('/')

		else:
			return None

	def render(self, template, params=None):
		if not params:
			params = {}

		params['logout_url'] = self.get_logout_url()

		super(AdminHandler, self).render(self, template, params)


class AdminPanel(AdminHandler):
	def get(self):
		self.render('admin-home.html')


class AdminEventos(AdminHandler):
	def get(self):
		self.render('admin-eventos.html')


class AdminOrganizadores(AdminHandler):
	def get(self):
		self.render('admin-organizadores.html')


class AdminBlog(AdminHandler):
	def get(self):
		self.render('admin-blog.html')


class Webmap(MainHandler):
	def get(self):
		pages = []

		webmap = '<br>'.join(pages)

		self.response.out.write(webmap)


class Error404(MainHandler):
	def get(self):
		self.error(404)

		self.render('error-404.html')
