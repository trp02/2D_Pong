import pygame, sys
from model import Model
from controller import Controller
from view import View

m = Model
v = View(m)
c = Controller(v)
c.startGame()
