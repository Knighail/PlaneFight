#coding=utf-8

import pygame
pygame.init()
from random import randint

#小敌机
class SmallEnemy(pygame.sprite.Sprite):
	HP = 1
	def __init__ (self):
		pygame.sprite.Sprite.__init__(self)
		self.image_filename = './image/enemy0.png'
		self.image = pygame.image.load(self.image_filename).convert_alpha()
		self.destroy_images = []
		self.destroy_images.extend([\
				pygame.image.load('./image/enemy0_down1.png').convert_alpha(),\
				pygame.image.load('./image/enemy0_down2.png').convert_alpha(),\
				pygame.image.load('./image/enemy0_down3.png').convert_alpha(),\
				pygame.image.load('./image/enemy0_down4.png').convert_alpha()\
			])
		self.rect = self.image.get_rect()
		self.reset()
		self.HP = SmallEnemy.HP
		self.speed = 2
		self.mask = pygame.mask.from_surface(self.image)

	def move(self):
		if self.rect.top > 852:
			self.reset()
		else:
			self.rect.top += self.speed		
		
	def reset(self):
		self.rect.left = randint(0,430)
		self.rect.top = randint(-5 * self.rect.height,-5)
		self.active = True 
		self.HP = SmallEnemy.HP

#中敌机
class MiddleEnemy(pygame.sprite.Sprite):
	HP = 5
	def __init__ (self):
		pygame.sprite.Sprite.__init__(self)
		self.image_filename = './image/enemy1.png'
		self.hit_image_filename = './image/enemy1_hit.png'
		self.image = pygame.image.load(self.image_filename).convert_alpha()
		self.hit_image = pygame.image.load(self.hit_image_filename).convert_alpha()
		self.destroy_images = []
		self.destroy_images.extend([\
				pygame.image.load('./image/enemy1_down1.png').convert_alpha(),\
				pygame.image.load('./image/enemy1_down2.png').convert_alpha(),\
				pygame.image.load('./image/enemy1_down3.png').convert_alpha(),\
				pygame.image.load('./image/enemy1_down4.png').convert_alpha()\
			])
		self.rect = self.image.get_rect()
		self.reset()
		self.HP = MiddleEnemy.HP
		self.speed = 1
		self.mask = pygame.mask.from_surface(self.image)

	def move(self):
		if self.rect.top > 852:
			self.reset()
		else:
			self.rect.top += self.speed		
		
	def reset(self):
		self.rect.left = randint(0,430)
		self.rect.top = randint(-10 * self.rect.height,-self.rect.height)
		self.hit = False
		self.active = True
		self.HP = MiddleEnemy.HP

#大敌机
class BigEnemy(pygame.sprite.Sprite):
	HP = 15
	def __init__ (self):
		pygame.sprite.Sprite.__init__(self)
		self.image_filename1 = './image/enemy2.png'
		self.image_filename2 = './image/enemy2_n2.png'
		self.hit_image_filename = './image/enemy2_hit.png'
		self.image1 = pygame.image.load(self.image_filename1).convert_alpha()
		self.image2 = pygame.image.load(self.image_filename2).convert_alpha()
		self.hit_image = pygame.image.load(self.hit_image_filename).convert_alpha()
		self.destroy_images = []
		self.destroy_images.extend([\
				pygame.image.load('./image/enemy2_down1.png').convert_alpha(),\
				pygame.image.load('./image/enemy2_down2.png').convert_alpha(),\
				pygame.image.load('./image/enemy2_down3.png').convert_alpha(),\
				pygame.image.load('./image/enemy2_down4.png').convert_alpha(),\
				pygame.image.load('./image/enemy2_down5.png').convert_alpha()\
			])
		self.rect = self.image1.get_rect()
		self.reset()
		self.HP = BigEnemy.HP
		self.speed = 1
		self.mask = pygame.mask.from_surface(self.image1)

	def move(self):
		if self.rect.top > 852:
			self.reset()
		else:
			self.rect.top += self.speed		
		
	def reset(self):
		self.rect.left = randint(0,430)
		self.rect.top = randint(-15 * self.rect.height,-self.rect.height)
		self.hit = False
		self.active = True
		self.HP = BigEnemy.HP