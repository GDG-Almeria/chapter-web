# -*- coding: utf-8 -*-

# Project: "GDG Almería"
# Script: main.py - App handler mapping
# App identifier: gdg-almeria
# URL: www.---.com
# Author: Marcos Manuel Ortega - Indavelopers
# Version: v1.0 - 02/2016


# -- Imports --
import webapp2

from scripts.handlers import *


# -- App --
app = webapp2.WSGIApplication([('/', StaticPage),
                               ('/webmap', Webmap)],
                              debug=True)

# todo Error default html