#coding=utf-8

#导入pygame库,并初始化
import pygame
from pygame.locals import *
pygame.init()

#创建一个大小为480*890的窗口，第二个参数为窗口模式，第三个参数为色深
#screen保存返回的Surface对象
bg_size = 480,852
screen = pygame.display.set_mode((bg_size),0,32)

#设置窗口标题
pygame.display.set_caption("PlaneFight")

from sys import exit #创建退出程序功能
from random import randint #导入随机数库
from settings import * #导入设置
from player import PlayerPlane #导入玩家飞机
from bullet import Bullet
from enemy import SmallEnemy #导入小型敌机
from enemy import MiddleEnemy #导入中型敌机
from enemy import BigEnemy #导入大型敌机



#设置背景图像文件名称并加载
background_image_filename = './image/background.png'
background = pygame.image.load(background_image_filename).convert()

#敌机生成函数
def add_small_enemies(group1,group2,num):
	for i in range(num):
		e1 = SmallEnemy()
		group1.add(e1)
		group2.add(e1)

def add_middle_enemies(group1,group2,num):
	for i in range(num):
		e2 = MiddleEnemy()
		group1.add(e2)
		group2.add(e2)

def add_big_enemies(group1,group2,num):
	for i in range(num):
		e3 = BigEnemy()
		group1.add(e3)
		group2.add(e3)

def enemy_speed_up(enemy,value):
	for e in enemy:
		e.speed += value


def main():
	pygame.mixer.music.play(loops = -1) #loops为-1背景音无限循环播放
	score = 0
	score_font = pygame.font.SysFont("arial", 20)

	player = PlayerPlane() #初始化玩家飞机
	switch_image = False
	player_destroy_index = 0 #玩家飞机爆炸图片切换标志

	bullets = [] #创建子弹类列表
	for i in range(6):
		bullets.append(Bullet(player.rect.left,player.rect.top))
	bullet_index = 0 #子弹标记序号

	#-----初始化敌机-----#
	enemies = pygame.sprite.Group() 
	small_enemies = pygame.sprite.Group()
	middle_enemies = pygame.sprite.Group()
	big_enemies = pygame.sprite.Group()
	add_small_enemies(small_enemies,enemies,1)	
	add_middle_enemies(middle_enemies,enemies,1)
	add_big_enemies(big_enemies,enemies,1)
	small_enemy_destroy_index = 0 #小敌机爆炸图片切换标志
	middle_enemy_destroy_index = 0 #中敌机爆炸图片切换标志
	big_enemy_destroy_index = 0 #大敌机爆炸图片切换标志
	delay = 60
	wait = 60 #等待1秒再随鼠标移动，防止游戏开始时无法获取鼠标位置而出生在左上角
	level = 1 #游戏难度


	while True:
		screen.blit(background,(0,0))
		score_text = score_font.render("score : %s" % str(score), True, (255,255,255))
		screen.blit(score_text, (10, 5))

		#接收到退出事件后退出程序
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
		
		clock = pygame.time.Clock() #定义时钟
		#定义所设置帧数，即每秒运行多少次循环，但是视性能而定
		clock.tick(60)
		#默认为毫秒，转化为秒
		#time_passed_second = time_passed / 1000.0


		if level == 1 and score > 6000:
			level = 2
			level_up_sound.play()
			add_small_enemies(small_enemies,enemies,3)	
			add_middle_enemies(middle_enemies,enemies,2)
			add_big_enemies(big_enemies,enemies,1)
			enemy_speed_up(small_enemies,2)
		elif level == 2 and score > 15000:
			level = 3
			level_up_sound.play()
			add_small_enemies(small_enemies,enemies,3)	
			add_middle_enemies(middle_enemies,enemies,2)
			add_big_enemies(big_enemies,enemies,1)
			enemy_speed_up(small_enemies,2)
			enemy_speed_up(middle_enemies,2)
		elif level == 3 and score > 30000:
			level = 4
			level_up_sound.play()
			add_small_enemies(small_enemies,enemies,3)	
			add_middle_enemies(middle_enemies,enemies,2)
			add_big_enemies(big_enemies,enemies,1)
			enemy_speed_up(small_enemies,2)
			enemy_speed_up(middle_enemies,2)
			enemy_speed_up(big_enemies,2)

		#玩家飞机碰撞检测
		player_down = pygame.sprite.spritecollide(player,enemies,False,pygame.sprite.collide_mask)
		if player_down:
			player.active = False
			for e in player_down:
				e.active = False

		#判断玩家飞机的存活状态
		if player.active:
			if wait <= 0:
				player.move()
			if switch_image:
				screen.blit(player.image1,player.rect)
			else:
				screen.blit(player.image2,player.rect)
			if not (delay % 3):
				switch_image = not switch_image
		else:
			if player_destroy_index == 0:
				player_down_sound.play()
			screen.blit(player.destroy_images[player_destroy_index],player.rect)
			if player_destroy_index == 3:
				player.reset()
			player_destroy_index = (player_destroy_index + 1) % 4

		if not (delay % 10):
			#重置子弹
			bullets[bullet_index].reset(player.rect.left,player.rect.top)
			#子弹序号循环递增
			bullet_index = (bullet_index + 1) % 6
		for b in bullets:
			if b.active:
				#移动并显示子弹
				b.move()
				bullet_sound.play()			
				screen.blit(b.image,b.rect)
				hit_enemy = pygame.sprite.spritecollide(b,enemies,False,pygame.sprite.collide_mask)
				if hit_enemy:
					b.active = False
					for e in hit_enemy:
						e.HP -= 1
						e.hit = True
						if e.HP ==0:
							e.active = False

		for se in small_enemies:
			if se.active:
				se.move()
				screen.blit(se.image,se.rect)
			else:
				if small_enemy_destroy_index == 0:
					enemy1_down_sound.play()
				if not (delay % 3):
					screen.blit(se.destroy_images[small_enemy_destroy_index],se.rect)
					small_enemy_destroy_index = (small_enemy_destroy_index + 1) % 4
					if small_enemy_destroy_index == 0:
						score += 100
						se.reset()

		for me in middle_enemies:
			if me.active:
				me.move()
				if me.hit:
					if not (delay % 3):
						screen.blit(me.hit_image,me.rect)
						me.hit = False
				else:
					screen.blit(me.image,me.rect)
			else:
				if middle_enemy_destroy_index == 0:
					enemy2_down_sound.play()
				if not (delay % 3):
					screen.blit(me.destroy_images[middle_enemy_destroy_index],me.rect)
					middle_enemy_destroy_index = (middle_enemy_destroy_index + 1) % 4
					if middle_enemy_destroy_index == 0:
						score += 500
						me.reset()

		for be in big_enemies:
			if be.active:
				be.move()
				if be.hit:
					if not (delay % 3):
						screen.blit(be.hit_image,be.rect)
						be.hit = False
				else:
					if switch_image:
						screen.blit(be.image1,be.rect)
					else:
						screen.blit(be.image2,be.rect)
				if be.rect.bottom == -50:
					enemy3_approach_sound.play(-1)
			else:
				if big_enemy_destroy_index == 0:
					enemy3_down_sound.play()
				if not (delay % 3):
					screen.blit(be.destroy_images[big_enemy_destroy_index],be.rect)
					big_enemy_destroy_index = (big_enemy_destroy_index + 1) % 5
					if big_enemy_destroy_index == 0:
						score += 1500
						be.reset()
		
		#隐藏鼠标光标
		#pygame.mouse.set_visible(False)
		pygame.display.update() #刷新显示
		if delay == 0:
			delay = 60
		delay -= 1
		wait -= 1
main()
