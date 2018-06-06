#coding=utf-8

import pygame
#pygame.init()

#创建玩家飞机类

class PlayerPlane(pygame.sprite.Sprite):
	
	def __init__ (self):
		#super(PlayerPlane,self).__init__()
		#设置两张飞机图片轮流切换,形成动态效果
		self.image_filename1 = './image/hero1.png'
		self.image_filename2 = './image/hero2.png'
		self.image1 = pygame.image.load(self.image_filename1).convert_alpha()
		self.image2 = pygame.image.load(self.image_filename2).convert_alpha()
		#设置飞机爆炸图片,添加动态效果
		self.destroy_images = []
		self.destroy_images.extend([\
				pygame.image.load('./image/hero_blowup_n1.png').convert_alpha(),\
				pygame.image.load('./image/hero_blowup_n2.png').convert_alpha(),\
				pygame.image.load('./image/hero_blowup_n3.png').convert_alpha(),\
				pygame.image.load('./image/hero_blowup_n4.png').convert_alpha()\
			])		
		self.rect = self.image1.get_rect()
		#设置飞机轮廓便于检查碰撞
		self.mask = pygame.mask.from_surface(self.image1)
		self.reset()

	def move(self): #因飞机随鼠标移动，暂不考虑移动到屏幕外
		mouse_x, mouse_y = pygame.mouse.get_pos()
		self.rect.left = mouse_x - self.image1.get_width()/2
		self.rect.top = mouse_y - self.image1.get_height()/2
		
	def reset(self):
		self.rect.left = 200
		self.rect.top = 700
		self.active = True