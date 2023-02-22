import pygame, sys
from model import Model
from controller import Controller
from view import View

v = View()
c = Controller(v)
c.startGame()
