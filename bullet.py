#coding=utf-8

import pygame
pygame.init()
from random import randint


class Bullet(pygame.sprite.Sprite):
	
	def __init__ (self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image_filename = './image/bullet1.png'
		self.image = pygame.image.load(self.image_filename).convert_alpha()
		self.rect = self.image.get_rect()
		self.reset(x,y)
		self.active = False
		self.speed = 15
		self.mask = pygame.mask.from_surface(self.image)

	def move(self):
		if self.rect.top < 0:
			#若超出，子弹重置
			self.active = False			
		else:
			#未超出则向前移动，移动距离为一次循环所需时间乘以速度，保持不同性能机器运行效果一致
			self.rect.top -= self.speed		
		
	def reset(self,x,y):
		self.rect.left = x + 47
		self.rect.top = y
		self.active = True