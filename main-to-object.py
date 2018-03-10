#coding=utf-8

#导入pygame库,并初始化
import pygame
pygame.init()

#创建一个大小为480*890的窗口，第二个参数为窗口模式，第三个参数为色深
#screen保存返回的Surface对象
screen = pygame.display.set_mode((480,852),0,32)

#设置窗口标题
pygame.display.set_caption("PlaneFight")

#创建退出程序功能
from sys import exit
#导入随机数库
from random import randint

#设置图像文件名称
background_image_filename = './image/background.png' 
mouse_image_filename = './image/hero1.png'

#定义一个子弹类
class Bullet(object):
	
	def __init__(self):
		#玩家飞机发射的子弹
		self.player_image_filename = './image/bullet1.png'
		self.player_image = pygame.image.load(self.player_image_filename).convert_alpha()
		#初始化子弹坐标
		self.player_x = 0
		self.player_y = -1
		#初始化子弹速度
		self.player_speed = 2000

	def Move(self,time_passed_second):
		#获取鼠标位置
		#判断子弹是否超出屏幕
		if self.player_y < 0:
			#若超出，重新发射
			mouse_x,mouse_y = pygame.mouse.get_pos()
			self.player_x = mouse_x - self.player_image.get_width()/2
			self.player_y = mouse_y - self.player_image.get_width()/2
		else:
			#未超出则向前移动，移动距离为一次循环所需时间乘以速度，保持不同性能机器运行效果一致
			self.player_y -= time_passed_second * self.player_speed

#定义一个敌机类
class Enemy(object):

	def __init__(self):
		self.enemy_image_filename = './image/enemy0.png'
		self.image = pygame.image.load(self.enemy_image_filename).convert_alpha()
		#定义敌机初始坐标
		self.x = randint(-25,455)
		self.y = 0
		#定义敌机速度
		self.speed = randint(100,400)
	def Move(self,time_passed_second):
		if self.y > 852:
			self.x = randint(-25,430)
			self.y = 0
		else:
			self.y += self.speed * time_passed_second

#加载并转换图像,convert_alpha()能保留alpha通道信息，实现透明
#窗口背景
background = pygame.image.load(background_image_filename).convert()
#鼠标控制的图片，即玩家飞机
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

bullet = Bullet()
enemy = Enemy()
#定义时钟
clock = pygame.time.Clock()

#游戏的主循环
while True:
	#event接收get()方法中保存的所有程序中发生的事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
		#接收到退出事件后退出程序
			pygame.quit()
			exit()
	
	#定义所设置帧数，即每秒运行多少次循环，但是视性能而定
	time_passed = clock.tick(30)
	#默认为毫秒，转化为秒
	time_passed_second = time_passed / 1000.0
	
	#移动子弹
	bullet.Move(time_passed_second)
	#移动敌机
	enemy.Move(time_passed_second)
	
	#显示背景，左上角位置为0,0
	screen.blit((background),(0,0))

	#获取鼠标位置，鼠标移动玩家飞机随之移动
	x,y = pygame.mouse.get_pos()
	
	#调整玩家飞机中心位置与鼠标位置一致
	x -= mouse_cursor.get_width() / 2
	y -= mouse_cursor.get_height() / 2
	#隐藏鼠标光标
	pygame.mouse.set_visible(False)
	
	#显示敌机
	screen.blit(enemy.image,(enemy.x,enemy.y))
	#显示玩家飞机发射的子弹
	screen.blit(bullet.player_image,(bullet.player_x,bullet.player_y))
	#显示鼠标光标控制的玩家飞机
	screen.blit((mouse_cursor),(x,y))

	#刷新显示
	pygame.display.update()