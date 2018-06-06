#coding=utf-8

import pygame
pygame.init()
pygame.mixer.init()

#游戏背景音
pygame.mixer.music.load("./sound/game_music.wav")
pygame.mixer.music.set_volume(0.3)

#子弹发射音
bullet_sound = pygame.mixer.Sound("./sound/bullet.wav")
bullet_sound.set_volume(0.1)

#玩家飞机爆炸音
player_down_sound = pygame.mixer.Sound("./sound/game_over.wav")
player_down_sound.set_volume(0.3)

#小敌机爆炸音
enemy1_down_sound = pygame.mixer.Sound("./sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.3)

#中敌机爆炸音
enemy2_down_sound = pygame.mixer.Sound("./sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.3)

#大敌机临近音
enemy3_approach_sound = pygame.mixer.Sound("./sound/big_spaceship_flying.wav")
enemy3_approach_sound.set_volume(0.3)
#大敌机爆炸音
enemy3_down_sound = pygame.mixer.Sound("./sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.3)

#难度升级音
level_up_sound = pygame.mixer.Sound("./sound/achievement.wav")
level_up_sound.set_volume(0.4)

def level_up(level,score):
	if level == 1 and score > 6000:
		level = 2
		level_up_sound.play()
		add_small_enemies(small_enemies,enemies,3)	
		add_middle_enemies(middle_enemies,enemies,2)
		add_big_enemies(big_enemies,enemies,1)
		enemy_speed_up(small_enemies,2)
	elif level == 2 and score > 10000:
		level = 3
		level_up_sound.play()
		add_small_enemies(small_enemies,enemies,3)	
		add_middle_enemies(middle_enemies,enemies,2)
		add_big_enemies(big_enemies,enemies,1)
		enemy_speed_up(small_enemies,2)
		enemy_speed_up(middle_enemies,2)
	elif level == 3 and score > 20000:
		level = 4
		level_up_sound.play()
		add_small_enemies(small_enemies,enemies,3)	
		add_middle_enemies(middle_enemies,enemies,2)
		add_big_enemies(big_enemies,enemies,1)
		enemy_speed_up(small_enemies,2)
		enemy_speed_up(middle_enemies,2)
		enemy_speed_up(big_enemies,2)