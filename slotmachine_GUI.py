import kivy
import time
import threading
from random import randint
from kivy.app import App
from kivy.base import Builder
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty
from kivy.properties import BooleanProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock, mainthread
from kivy.config import Config
from win32api import GetSystemMetrics
from slotmachine import Slotmachine_engine
import locale
import sys

locale.setlocale(locale.LC_ALL, 'de_DE.utf-8')
if sys.platform == 'win32':
	Config.set('graphics', 'width', GetSystemMetrics(0)-100)
	Config.set('graphics', 'height', GetSystemMetrics(1)-100)
else:
	Config.set('graphics', 'width', '1200')
	Config.set('graphics', 'height', '800')


Game = Slotmachine_engine(1,50)

class MyTextInput(TextInput):
	max_characters = NumericProperty(0)
	def insert_text(self, substring, from_undo=False):
		if len(self.text) > 3 and 3 > 0:
			substring = ''
		TextInput.insert_text(self, substring, from_undo)


class MyGrid(Widget):	

	def start_game(self):	
		self.color_winning_lines(0)
		self.get_number_of_symbols()
		self.get_payout()
		self.shuffle_numbers()
		Game.start_round()
		self.credits.text = str(Game.get_credits())
		self.get_rows()


	def get_rows(self):
		dic_name_to_picsource = {'10': 'icons/cherry.png',
								'Jack': 'icons/strawberry.png',
								'Queen': 'icons/citrone.png',
								'King': 'icons/banana.png',
								'Ace': 'icons/grape.png',
								'SEVEN': 'icons/SEVEN.png'}			
		self.wheel_1_0.source = dic_name_to_picsource[Game.get_rows()[0][0]]
		self.wheel_2_0.source = dic_name_to_picsource[Game.get_rows()[0][1]]		
		self.wheel_3_0.source = dic_name_to_picsource[Game.get_rows()[0][2]]
		self.wheel_4_0.source = dic_name_to_picsource[Game.get_rows()[0][3]]
		self.wheel_5_0.source = dic_name_to_picsource[Game.get_rows()[0][4]]
		
		self.wheel_1_1.source = dic_name_to_picsource[Game.get_rows()[1][0]]
		self.wheel_2_1.source = dic_name_to_picsource[Game.get_rows()[1][1]]		
		self.wheel_3_1.source = dic_name_to_picsource[Game.get_rows()[1][2]]
		self.wheel_4_1.source = dic_name_to_picsource[Game.get_rows()[1][3]]		
		self.wheel_5_1.source = dic_name_to_picsource[Game.get_rows()[1][4]]
		
		self.wheel_1_2.source = dic_name_to_picsource[Game.get_rows()[2][0]]
		self.wheel_2_2.source = dic_name_to_picsource[Game.get_rows()[2][1]]		
		self.wheel_3_2.source = dic_name_to_picsource[Game.get_rows()[2][2]]
		self.wheel_4_2.source = dic_name_to_picsource[Game.get_rows()[2][3]]		
		self.wheel_5_2.source = dic_name_to_picsource[Game.get_rows()[2][4]]


	def shuffle_numbers(self):
		threading.Thread(target=self.shuffle_numbers_thread).start()

	
	def shuffle_numbers_thread(self):
		dic_name_to_picsource = {'10': 'icons/cherry.png',
								'Jack': 'icons/strawberry.png',
								'Queen': 'icons/citrone.png',
								'King': 'icons/banana.png',
								'Ace': 'icons/grape.png',
								'SEVEN': 'icons/SEVEN.png'}		
		shuffle_pictures = ['10']*5 + ['Jack'] * 5 + ['Queen'] * 5 + ['King'] * 5 + ['Ace'] * 5 + ['SEVEN'] * 5
		for i in range(10):
			if i < 5:
				self.wheel_1_0.source = dic_name_to_picsource[str(shuffle_pictures[randint(0,len(shuffle_pictures)-2)])]
				self.wheel_1_1.source = dic_name_to_picsource[str(shuffle_pictures[randint(0,len(shuffle_pictures)-2)])]			
				self.wheel_1_2.source = dic_name_to_picsource[str(shuffle_pictures[randint(0,len(shuffle_pictures)-2)])]	
			else: 
				self.wheel_1_0.source = dic_name_to_picsource[Game.get_rows()[0][0]]	
				self.wheel_1_1.source = dic_name_to_picsource[Game.get_rows()[1][0]]
				self.wheel_1_2.source = dic_name_to_picsource[Game.get_rows()[2][0]]
			if i < 6:	
				self.wheel_2_0.source = dic_name_to_picsource[str(shuffle_pictures[randint(0,len(shuffle_pictures)-2)])]					
				self.wheel_2_1.source = dic_name_to_picsource[str(shuffle_pictures[randint(0,len(shuffle_pictures)-2)])]				
				self.wheel_2_2.source = dic_name_to_picsource[str(shuffle_pictures[randint(0,len(shuffle_pictures)-2)])]	
			else:
				self.wheel_2_0.source = dic_name_to_picsource[Game.get_rows()[0][1]]	
				self.wheel_2_1.source = dic_name_to_picsource[Game.get_rows()[1][1]]
				self.wheel_2_2.source = dic_name_to_picsource[Game.get_rows()[2][1]]			
			if i < 7:				
				self.wheel_3_0.source = dic_name_to_picsource[str(shuffle_pictures[randint(0,len(shuffle_pictures)-2)])]
				self.wheel_3_1.source = dic_name_to_picsource[str(shuffle_pictures[randint(0,len(shuffle_pictures)-2)])]			
				self.wheel_3_2.source = dic_name_to_picsource[str(shuffle_pictures[randint(0,len(shuffle_pictures)-2)])]		
			else:
				self.wheel_3_0.source = dic_name_to_picsource[Game.get_rows()[0][2]]	
				self.wheel_3_1.source = dic_name_to_picsource[Game.get_rows()[1][2]]
				self.wheel_3_2.source = dic_name_to_picsource[Game.get_rows()[2][2]]	
			if i < 8:				
				self.wheel_4_0.source = dic_name_to_picsource[str(shuffle_pictures[randint(0,len(shuffle_pictures)-2)])]
				self.wheel_4_1.source = dic_name_to_picsource[str(shuffle_pictures[randint(0,len(shuffle_pictures)-2)])]			
				self.wheel_4_2.source = dic_name_to_picsource[str(shuffle_pictures[randint(0,len(shuffle_pictures)-2)])]		
			else:
				self.wheel_4_0.source = dic_name_to_picsource[Game.get_rows()[0][3]]	
				self.wheel_4_1.source = dic_name_to_picsource[Game.get_rows()[1][3]]
				self.wheel_4_2.source = dic_name_to_picsource[Game.get_rows()[2][3]]	
			if i < 9:				
				self.wheel_5_0.source = dic_name_to_picsource[str(shuffle_pictures[randint(0,len(shuffle_pictures)-2)])]									   
				self.wheel_5_1.source = dic_name_to_picsource[str(shuffle_pictures[randint(0,len(shuffle_pictures)-2)])]									   
				self.wheel_5_2.source = dic_name_to_picsource[str(shuffle_pictures[randint(0,len(shuffle_pictures)-2)])]
			else:
				self.wheel_5_0.source = dic_name_to_picsource[Game.get_rows()[0][4]]	
				self.wheel_5_1.source = dic_name_to_picsource[Game.get_rows()[1][4]]
				self.wheel_5_2.source = dic_name_to_picsource[Game.get_rows()[2][4]]	
			time.sleep(0.035)
	
		self.color_winning_lines(1)
		if Game.get_win() > 0:
			self.win.text = str(Game.get_win())
	
	
	def color_winning_lines(self, i):
		self.ow = i
		Clock.schedule_once(self.color_winning_lines_thread, 0)
	
	
	def check_input_size(self):
		for i in [self.gui_w1_nS1,
			self.gui_w2_nS1,
			self.gui_w3_nS1,
			self.gui_w4_nS1,
			self.gui_w5_nS1,
			self.gui_w1_nS2,
			self.gui_w2_nS2,
			self.gui_w3_nS2,
			self.gui_w4_nS2,
			self.gui_w5_nS2,
			self.gui_w1_nS3,
			self.gui_w2_nS3,
			self.gui_w3_nS3,
			self.gui_w4_nS3,
			self.gui_w5_nS3,
			self.gui_w1_nS4,
			self.gui_w2_nS4,
			self.gui_w3_nS4,
			self.gui_w4_nS4,
			self.gui_w5_nS4,
			self.gui_w1_nS5,
			self.gui_w2_nS5,
			self.gui_w3_nS5,
			self.gui_w4_nS5,
			self.gui_w5_nS5,
			self.gui_w1_nS6,
			self.gui_w2_nS6,
			self.gui_w3_nS6,
			self.gui_w4_nS6,
			self.gui_w5_nS6]: 
			if int(i.text.replace('.','')) > 99:
				i.text = '99'
	
	
	def get_number_of_symbols(self):
		self.gui_w1_nS1.text = str(locale.format_string('%d', Game.w1_nS1, 1))
		self.gui_w2_nS1.text = str(locale.format_string('%d', Game.w2_nS1, 1))
		self.gui_w3_nS1.text = str(locale.format_string('%d', Game.w3_nS1, 1))
		self.gui_w4_nS1.text = str(locale.format_string('%d', Game.w4_nS1, 1))
		self.gui_w5_nS1.text = str(locale.format_string('%d', Game.w5_nS1, 1))	
		self.gui_w1_nS2.text = str(locale.format_string('%d', Game.w1_nS2, 1))
		self.gui_w2_nS2.text = str(locale.format_string('%d', Game.w2_nS2, 1))
		self.gui_w3_nS2.text = str(locale.format_string('%d', Game.w3_nS2, 1))
		self.gui_w4_nS2.text = str(locale.format_string('%d', Game.w4_nS2, 1))
		self.gui_w5_nS2.text = str(locale.format_string('%d', Game.w5_nS2, 1))	
		self.gui_w1_nS3.text = str(locale.format_string('%d', Game.w1_nS3, 1))
		self.gui_w2_nS3.text = str(locale.format_string('%d', Game.w2_nS3, 1))
		self.gui_w3_nS3.text = str(locale.format_string('%d', Game.w3_nS3, 1))
		self.gui_w4_nS3.text = str(locale.format_string('%d', Game.w4_nS3, 1))
		self.gui_w5_nS3.text = str(locale.format_string('%d', Game.w5_nS3, 1))	
		self.gui_w1_nS4.text = str(locale.format_string('%d', Game.w1_nS4, 1))
		self.gui_w2_nS4.text = str(locale.format_string('%d', Game.w2_nS4, 1))
		self.gui_w3_nS4.text = str(locale.format_string('%d', Game.w3_nS4, 1))
		self.gui_w4_nS4.text = str(locale.format_string('%d', Game.w4_nS4, 1))
		self.gui_w5_nS4.text = str(locale.format_string('%d', Game.w5_nS4, 1))	
		self.gui_w1_nS5.text = str(locale.format_string('%d', Game.w1_nS5, 1))
		self.gui_w2_nS5.text = str(locale.format_string('%d', Game.w2_nS5, 1))
		self.gui_w3_nS5.text = str(locale.format_string('%d', Game.w3_nS5, 1))
		self.gui_w4_nS5.text = str(locale.format_string('%d', Game.w4_nS5, 1))
		self.gui_w5_nS5.text = str(locale.format_string('%d', Game.w5_nS5, 1))	
		self.gui_w1_nS6.text = str(locale.format_string('%d', Game.w1_nS6, 1))
		self.gui_w2_nS6.text = str(locale.format_string('%d', Game.w2_nS6, 1))
		self.gui_w3_nS6.text = str(locale.format_string('%d', Game.w3_nS6, 1))
		self.gui_w4_nS6.text = str(locale.format_string('%d', Game.w4_nS6, 1))
		self.gui_w5_nS6.text = str(locale.format_string('%d', Game.w5_nS6, 1))	

		
	def change_number_of_symbols(self):
		if int(self.gui_w1_nS1.text) + int(self.gui_w1_nS2.text) + int(self.gui_w1_nS3.text) + int(self.gui_w1_nS4.text) + int(self.gui_w1_nS5.text) + int(self.gui_w1_nS6.text) < 6:
			Game.w1_nS1 = 1		
			Game.w1_nS2 = 1
			Game.w1_nS3 = 1
			Game.w1_nS4 = 1
			Game.w1_nS5 = 1
			Game.w1_nS6 = 1
		else:
			Game.w1_nS1 = int(self.gui_w1_nS1.text)
			Game.w1_nS2 = int(self.gui_w1_nS2.text)
			Game.w1_nS3 = int(self.gui_w1_nS3.text)
			Game.w1_nS4 = int(self.gui_w1_nS4.text)
			Game.w1_nS5 = int(self.gui_w1_nS5.text)
			Game.w1_nS6 = int(self.gui_w1_nS6.text)
		if int(self.gui_w2_nS1.text) + int(self.gui_w2_nS2.text) + int(self.gui_w2_nS3.text) + int(self.gui_w2_nS4.text) + int(self.gui_w2_nS5.text) + int(self.gui_w2_nS6.text) < 6:
			Game.w2_nS1 = 1		
			Game.w2_nS2 = 1
			Game.w2_nS3 = 1
			Game.w2_nS4 = 1
			Game.w2_nS5 = 1
			Game.w2_nS6 = 1
		else:
			Game.w2_nS1 = int(self.gui_w2_nS1.text)
			Game.w2_nS2 = int(self.gui_w2_nS2.text)
			Game.w2_nS3 = int(self.gui_w2_nS3.text)
			Game.w2_nS4 = int(self.gui_w2_nS4.text)
			Game.w2_nS5 = int(self.gui_w2_nS5.text)
			Game.w2_nS6 = int(self.gui_w2_nS6.text)
		if int(self.gui_w3_nS1.text) + int(self.gui_w3_nS2.text) + int(self.gui_w3_nS3.text) + int(self.gui_w3_nS4.text) + int(self.gui_w3_nS5.text) + int(self.gui_w3_nS6.text) < 6:
			Game.w3_nS1 = 1		
			Game.w3_nS2 = 1
			Game.w3_nS3 = 1
			Game.w3_nS4 = 1
			Game.w3_nS5 = 1
			Game.w3_nS6 = 1
		else:
			Game.w3_nS1 = int(self.gui_w3_nS1.text)
			Game.w3_nS2 = int(self.gui_w3_nS2.text)
			Game.w3_nS3 = int(self.gui_w3_nS3.text)
			Game.w3_nS4 = int(self.gui_w3_nS4.text)
			Game.w3_nS5 = int(self.gui_w3_nS5.text)
			Game.w3_nS6 = int(self.gui_w3_nS6.text)		
		if int(self.gui_w4_nS1.text) + int(self.gui_w4_nS2.text) + int(self.gui_w4_nS3.text) + int(self.gui_w4_nS4.text) + int(self.gui_w4_nS5.text) + int(self.gui_w4_nS6.text) < 6:
			Game.w4_nS1 = 1		
			Game.w4_nS2 = 1
			Game.w4_nS3 = 1
			Game.w4_nS4 = 1
			Game.w4_nS5 = 1
			Game.w4_nS6 = 1
		else:
			Game.w4_nS1 = int(self.gui_w4_nS1.text)
			Game.w4_nS2 = int(self.gui_w4_nS2.text)
			Game.w4_nS3 = int(self.gui_w4_nS3.text)
			Game.w4_nS4 = int(self.gui_w4_nS4.text)
			Game.w4_nS5 = int(self.gui_w4_nS5.text)
			Game.w4_nS6 = int(self.gui_w4_nS6.text)			
		if int(self.gui_w5_nS1.text) + int(self.gui_w5_nS2.text) + int(self.gui_w5_nS3.text) + int(self.gui_w5_nS4.text) + int(self.gui_w5_nS5.text) + int(self.gui_w5_nS6.text) < 6:
			Game.w5_nS1 = 1		
			Game.w5_nS2 = 1
			Game.w5_nS3 = 1
			Game.w5_nS4 = 1
			Game.w5_nS5 = 1
			Game.w5_nS6 = 1
		else:
			Game.w5_nS1 = int(self.gui_w5_nS1.text)
			Game.w5_nS2 = int(self.gui_w5_nS2.text)
			Game.w5_nS3 = int(self.gui_w5_nS3.text)
			Game.w5_nS4 = int(self.gui_w5_nS4.text)
			Game.w5_nS5 = int(self.gui_w5_nS5.text)
			Game.w5_nS6 = int(self.gui_w5_nS6.text)		

	
	def get_payout(self):
		self.gui_s1_5times.text = str(locale.format_string('%d', Game.s1_5times, 1))
		self.gui_s2_5times.text = str(locale.format_string('%d', Game.s2_5times, 1))
		self.gui_s3_5times.text = str(locale.format_string('%d', Game.s3_5times, 1))
		self.gui_s4_5times.text = str(locale.format_string('%d', Game.s4_5times, 1))
		self.gui_s5_5times.text = str(locale.format_string('%d', Game.s5_5times, 1))
		self.gui_s1_4times.text = str(locale.format_string('%d', Game.s1_4times, 1))
		self.gui_s2_4times.text = str(locale.format_string('%d', Game.s2_4times, 1))
		self.gui_s3_4times.text = str(locale.format_string('%d', Game.s3_4times, 1))
		self.gui_s4_4times.text = str(locale.format_string('%d', Game.s4_4times, 1))
		self.gui_s5_4times.text = str(locale.format_string('%d', Game.s5_4times, 1))
		self.gui_s1_3times.text = str(locale.format_string('%d', Game.s1_3times, 1))
		self.gui_s2_3times.text = str(locale.format_string('%d', Game.s2_3times, 1))
		self.gui_s3_3times.text = str(locale.format_string('%d', Game.s3_3times, 1))
		self.gui_s4_3times.text = str(locale.format_string('%d', Game.s4_3times, 1))
		self.gui_s5_3times.text = str(locale.format_string('%d', Game.s5_3times, 1))	
	
	
	def change_payout(self):
		for i in [self.gui_s1_5times,
		          self.gui_s2_5times,
		          self.gui_s3_5times,
		          self.gui_s4_5times,
		          self.gui_s5_5times,
		          self.gui_s1_4times,
		          self.gui_s2_4times,
		          self.gui_s3_4times,
		          self.gui_s4_4times,
		          self.gui_s5_4times,
		          self.gui_s1_3times,
		          self.gui_s2_3times,
		          self.gui_s3_3times,
		          self.gui_s4_3times,
		          self.gui_s5_3times]:
			if int(i.text) >	999999:
				i.text = '999999'	
		Game.s1_5times = int(self.gui_s1_5times.text)
		Game.s2_5times = int(self.gui_s2_5times.text)
		Game.s3_5times = int(self.gui_s3_5times.text)
		Game.s4_5times = int(self.gui_s4_5times.text)
		Game.s5_5times = int(self.gui_s5_5times.text)	
		Game.s1_4times = int(self.gui_s1_4times.text)
		Game.s2_4times = int(self.gui_s2_4times.text)
		Game.s3_4times = int(self.gui_s3_4times.text)
		Game.s4_4times = int(self.gui_s4_4times.text)
		Game.s5_4times = int(self.gui_s5_4times.text)	
		Game.s1_3times = int(self.gui_s1_3times.text)
		Game.s2_3times = int(self.gui_s2_3times.text)
		Game.s3_3times = int(self.gui_s3_3times.text)
		Game.s4_3times = int(self.gui_s4_3times.text)
		Game.s5_3times = int(self.gui_s5_3times.text)

	def update_number_of_possible_ways(self):
		self.gui_npw_s1_5times.text = str(locale.format_string('%d', (Game.w1_nS1 * Game.w2_nS1 * Game.w3_nS1 * Game.w4_nS1 * Game.w5_nS1 * 5), 1))
		self.gui_npw_s2_5times.text = str(locale.format_string('%d', (Game.w1_nS2 * Game.w2_nS2 * Game.w3_nS2 * Game.w4_nS2 * Game.w5_nS2 * 5), 1))
		self.gui_npw_s3_5times.text = str(locale.format_string('%d', (Game.w1_nS3 * Game.w2_nS3 * Game.w3_nS3 * Game.w4_nS3 * Game.w5_nS3 * 5), 1))
		self.gui_npw_s4_5times.text = str(locale.format_string('%d', (Game.w1_nS4 * Game.w2_nS4 * Game.w3_nS4 * Game.w4_nS4 * Game.w5_nS4 * 5), 1))
		self.gui_npw_s5_5times.text = str(locale.format_string('%d', (Game.w1_nS5 * Game.w2_nS5 * Game.w3_nS5 * Game.w4_nS5 * Game.w5_nS5 * 5), 1))
		self.gui_npw_s6_5times.text = str(locale.format_string('%d', (Game.w1_nS6 * Game.w2_nS6 * Game.w3_nS6 * Game.w4_nS6 * Game.w5_nS6 * 5), 1))
		
		self.gui_npw_s1_4times.text = str(locale.format_string('%d', Game.w1_nS1 * Game.w2_nS1 * Game.w3_nS1 * Game.w4_nS1 * (sum([Game.w5_nS1, Game.w5_nS2, Game.w5_nS3, Game.w5_nS4, Game.w5_nS5, Game.w5_nS6]) - Game.w5_nS1) * 5, 1))
		self.gui_npw_s2_4times.text = str(locale.format_string('%d', Game.w1_nS2 * Game.w2_nS2 * Game.w3_nS2 * Game.w4_nS2 * (sum([Game.w5_nS1, Game.w5_nS2, Game.w5_nS3, Game.w5_nS4, Game.w5_nS5, Game.w5_nS6]) - Game.w5_nS2) * 5, 1))
		self.gui_npw_s3_4times.text = str(locale.format_string('%d', Game.w1_nS3 * Game.w2_nS3 * Game.w3_nS3 * Game.w4_nS3 * (sum([Game.w5_nS1, Game.w5_nS2, Game.w5_nS3, Game.w5_nS4, Game.w5_nS5, Game.w5_nS6]) - Game.w5_nS3) * 5, 1))
		self.gui_npw_s4_4times.text = str(locale.format_string('%d', Game.w1_nS4 * Game.w2_nS4 * Game.w3_nS4 * Game.w4_nS4 * (sum([Game.w5_nS1, Game.w5_nS2, Game.w5_nS3, Game.w5_nS4, Game.w5_nS5, Game.w5_nS6]) - Game.w5_nS4) * 5, 1))
		self.gui_npw_s5_4times.text = str(locale.format_string('%d', Game.w1_nS5 * Game.w2_nS5 * Game.w3_nS5 * Game.w4_nS5 * (sum([Game.w5_nS1, Game.w5_nS2, Game.w5_nS3, Game.w5_nS4, Game.w5_nS5, Game.w5_nS6]) - Game.w5_nS5) * 5, 1))
		self.gui_npw_s6_4times.text = str(locale.format_string('%d', Game.w1_nS6 * Game.w2_nS6 * Game.w3_nS6 * Game.w4_nS6 * (sum([Game.w5_nS1, Game.w5_nS2, Game.w5_nS3, Game.w5_nS4, Game.w5_nS5, Game.w5_nS6]) - Game.w5_nS6) * 5, 1))

		self.gui_npw_s1_3times.text = str(locale.format_string('%d',Game.w1_nS1 * Game.w2_nS1 * Game.w3_nS1 * (sum([Game.w4_nS1, Game.w4_nS2, Game.w4_nS3, Game.w4_nS4, Game.w4_nS5, Game.w4_nS6]) - Game.w4_nS1) * sum([Game.w5_nS1, Game.w5_nS2, Game.w5_nS3, Game.w5_nS4, Game.w5_nS5, Game.w5_nS6]) * 5, 1))
		self.gui_npw_s2_3times.text = str(locale.format_string('%d',Game.w1_nS2 * Game.w2_nS2 * Game.w3_nS2 * (sum([Game.w4_nS1, Game.w4_nS2, Game.w4_nS3, Game.w4_nS4, Game.w4_nS5, Game.w4_nS6]) - Game.w4_nS2) * sum([Game.w5_nS1, Game.w5_nS2, Game.w5_nS3, Game.w5_nS4, Game.w5_nS5, Game.w5_nS6]) * 5, 1))
		self.gui_npw_s3_3times.text = str(locale.format_string('%d',Game.w1_nS3 * Game.w2_nS3 * Game.w3_nS3 * (sum([Game.w4_nS1, Game.w4_nS2, Game.w4_nS3, Game.w4_nS4, Game.w4_nS5, Game.w4_nS6]) - Game.w4_nS3) * sum([Game.w5_nS1, Game.w5_nS2, Game.w5_nS3, Game.w5_nS4, Game.w5_nS5, Game.w5_nS6]) * 5, 1))
		self.gui_npw_s4_3times.text = str(locale.format_string('%d',Game.w1_nS4 * Game.w2_nS4 * Game.w3_nS4 * (sum([Game.w4_nS1, Game.w4_nS2, Game.w4_nS3, Game.w4_nS4, Game.w4_nS5, Game.w4_nS6]) - Game.w4_nS4) * sum([Game.w5_nS1, Game.w5_nS2, Game.w5_nS3, Game.w5_nS4, Game.w5_nS5, Game.w5_nS6]) * 5, 1))
		self.gui_npw_s5_3times.text = str(locale.format_string('%d',Game.w1_nS5 * Game.w2_nS5 * Game.w3_nS5 * (sum([Game.w4_nS1, Game.w4_nS2, Game.w4_nS3, Game.w4_nS4, Game.w4_nS5, Game.w4_nS6]) - Game.w4_nS5) * sum([Game.w5_nS1, Game.w5_nS2, Game.w5_nS3, Game.w5_nS4, Game.w5_nS5, Game.w5_nS6]) * 5, 1))
		self.gui_npw_s6_3times.text = str(locale.format_string('%d',Game.w1_nS6 * Game.w2_nS6 * Game.w3_nS6 * (sum([Game.w4_nS1, Game.w4_nS2, Game.w4_nS3, Game.w4_nS4, Game.w4_nS5, Game.w4_nS6]) - Game.w4_nS6) * sum([Game.w5_nS1, Game.w5_nS2, Game.w5_nS3, Game.w5_nS4, Game.w5_nS5, Game.w5_nS6]) * 5, 1))		
	
	def update_return(self):
		self.gui_return_s1_5times.text =  str(locale.format_string('%d', int(self.gui_npw_s1_5times.text.replace('.','')) * Game.s1_5times, 1))
		self.gui_return_s2_5times.text =  str(locale.format_string('%d', int(self.gui_npw_s2_5times.text.replace('.','')) * Game.s2_5times, 1))
		self.gui_return_s3_5times.text =  str(locale.format_string('%d', int(self.gui_npw_s3_5times.text.replace('.','')) * Game.s3_5times, 1))
		self.gui_return_s4_5times.text =  str(locale.format_string('%d', int(self.gui_npw_s4_5times.text.replace('.','')) * Game.s4_5times, 1))
		self.gui_return_s5_5times.text =  str(locale.format_string('%d', int(self.gui_npw_s5_5times.text.replace('.','')) * Game.s5_5times, 1))
		self.gui_return_s6_5times.text =  str(locale.format_string('%d', int(self.gui_npw_s6_5times.text.replace('.','')) * Game.s6_5times, 1))
		
		self.gui_return_s1_4times.text = str(locale.format_string('%d', int(self.gui_npw_s1_4times.text.replace('.','')) * Game.s1_4times, 1))
		self.gui_return_s2_4times.text = str(locale.format_string('%d', int(self.gui_npw_s2_4times.text.replace('.','')) * Game.s2_4times, 1))
		self.gui_return_s3_4times.text = str(locale.format_string('%d', int(self.gui_npw_s3_4times.text.replace('.','')) * Game.s3_4times, 1))
		self.gui_return_s4_4times.text = str(locale.format_string('%d', int(self.gui_npw_s4_4times.text.replace('.','')) * Game.s4_4times, 1))
		self.gui_return_s5_4times.text = str(locale.format_string('%d', int(self.gui_npw_s5_4times.text.replace('.','')) * Game.s5_4times, 1))
		self.gui_return_s6_4times.text = str(locale.format_string('%d', int(self.gui_npw_s6_4times.text.replace('.','')) * Game.s6_4times, 1))
		
		self.gui_return_s1_3times.text = str(locale.format_string('%d', int(self.gui_npw_s1_3times.text.replace('.','')) * Game.s1_3times, 1))
		self.gui_return_s2_3times.text = str(locale.format_string('%d', int(self.gui_npw_s2_3times.text.replace('.','')) * Game.s2_3times, 1))
		self.gui_return_s3_3times.text = str(locale.format_string('%d', int(self.gui_npw_s3_3times.text.replace('.','')) * Game.s3_3times, 1))
		self.gui_return_s4_3times.text = str(locale.format_string('%d', int(self.gui_npw_s4_3times.text.replace('.','')) * Game.s4_3times, 1))
		self.gui_return_s5_3times.text = str(locale.format_string('%d', int(self.gui_npw_s5_3times.text.replace('.','')) * Game.s5_3times, 1))
		self.gui_return_s6_3times.text = str(locale.format_string('%d', int(self.gui_npw_s6_3times.text.replace('.','')) * Game.s6_3times, 1))


	
	def color_winning_lines_thread(self, ow):
		ow = self.ow
		winning_lines = Game.get_winnig_lines()
		if ow == 1 and winning_lines != []:
			for i in winning_lines:
				if i[0] == 0:
					self.wheel_1_0.source = self.wheel_1_0.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_1_0.source else self.wheel_1_0.source
					self.wheel_2_0.source = self.wheel_2_0.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_2_0.source else self.wheel_2_0.source
					self.wheel_3_0.source = self.wheel_3_0.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_3_0.source else self.wheel_3_0.source
				if i[0] == 0 and i[1] == 4:	
					self.wheel_4_0.source = self.wheel_4_0.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_4_0.source else self.wheel_4_0.source
				if i[0] == 0 and i[1] == 5:	
					self.wheel_4_0.source = self.wheel_4_0.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_4_0.source else self.wheel_4_0.source
					self.wheel_5_0.source = self.wheel_5_0.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_5_0.source else self.wheel_5_0.source

				if i[0] == 1:
					self.wheel_1_1.source = self.wheel_1_1.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_1_1.source else self.wheel_1_1.source
					self.wheel_2_1.source = self.wheel_2_1.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_2_1.source else self.wheel_2_1.source
					self.wheel_3_1.source = self.wheel_3_1.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_3_1.source else self.wheel_3_1.source
				if i[0] == 1 and i[1] == 4:	                                                 
					self.wheel_4_1.source = self.wheel_4_1.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_4_1.source else self.wheel_4_1.source
				if i[0] == 1 and i[1] == 5:	 
					self.wheel_4_1.source = self.wheel_4_1.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_4_1.source else self.wheel_4_1.source
					self.wheel_5_1.source = self.wheel_5_1.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_5_1.source else self.wheel_5_1.source		
			
				if i[0] == 2:
					self.wheel_1_2.source = self.wheel_1_2.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_1_2.source else self.wheel_1_2.source
					self.wheel_2_2.source = self.wheel_2_2.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_2_2.source else self.wheel_2_2.source
					self.wheel_3_2.source = self.wheel_3_2.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_3_2.source else self.wheel_3_2.source
				if i[0] == 2 and i[1] == 4:	                                                 
					self.wheel_4_2.source = self.wheel_4_2.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_4_2.source else self.wheel_4_2.source
				if i[0] == 2 and i[1] == 5:	  
					self.wheel_4_2.source = self.wheel_4_2.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_4_2.source else self.wheel_4_2.source
					self.wheel_5_2.source = self.wheel_5_2.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_5_2.source else self.wheel_5_2.source		

				if i[0] == 3:
					self.wheel_1_0.source = self.wheel_1_0.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_1_0.source else self.wheel_1_0.source
					self.wheel_2_1.source = self.wheel_2_1.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_2_1.source else self.wheel_2_1.source
					self.wheel_3_2.source = self.wheel_3_2.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_3_2.source else self.wheel_3_2.source
				if i[0] == 3 and i[1] == 4:	                                                 
					self.wheel_4_1.source = self.wheel_4_1.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_4_1.source else self.wheel_4_1.source
				if i[0] == 3 and i[1] == 5:	    
					self.wheel_4_1.source = self.wheel_4_1.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_4_1.source else self.wheel_4_1.source
					self.wheel_5_0.source = self.wheel_5_0.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_5_0.source else self.wheel_5_0.source	

				if i[0] == 4:
					self.wheel_1_2.source = self.wheel_1_2.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_1_2.source else self.wheel_1_2.source
					self.wheel_2_1.source = self.wheel_2_1.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_2_1.source else self.wheel_2_1.source
					self.wheel_3_0.source = self.wheel_3_0.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_3_0.source else self.wheel_3_0.source
				if i[0] == 4 and i[1] == 4:	                                                 
					self.wheel_4_1.source = self.wheel_4_1.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_4_1.source else self.wheel_4_1.source
				if i[0] == 4 and i[1] == 5:
					self.wheel_4_1.source = self.wheel_4_1.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_4_1.source else self.wheel_4_1.source
					self.wheel_5_2.source = self.wheel_5_2.source.split('.')[0] + '_win.png' if 'win' not in self.wheel_5_2.source else self.wheel_5_2.source					
		elif ow == 0:
					self.wheel_1_0.source = self.wheel_1_0.source.split('_')[0] + '.png' if '_' in self.wheel_1_0.source else self.wheel_1_0.source
					self.wheel_2_0.source = self.wheel_2_0.source.split('_')[0] + '.png' if '_' in self.wheel_2_0.source else self.wheel_2_0.source
					self.wheel_3_0.source = self.wheel_3_0.source.split('_')[0] + '.png' if '_' in self.wheel_3_0.source else self.wheel_3_0.source
					self.wheel_4_0.source = self.wheel_4_0.source.split('_')[0] + '.png' if '_' in self.wheel_4_0.source else self.wheel_4_0.source
					self.wheel_5_0.source = self.wheel_5_0.source.split('_')[0] + '.png' if '_' in self.wheel_5_0.source else self.wheel_5_0.source		
					self.wheel_1_1.source = self.wheel_1_1.source.split('_')[0] + '.png' if '_' in self.wheel_1_1.source else self.wheel_1_1.source
					self.wheel_2_1.source = self.wheel_2_1.source.split('_')[0] + '.png' if '_' in self.wheel_2_1.source else self.wheel_2_1.source
					self.wheel_3_1.source = self.wheel_3_1.source.split('_')[0] + '.png' if '_' in self.wheel_3_1.source else self.wheel_3_1.source
					self.wheel_4_1.source = self.wheel_4_1.source.split('_')[0] + '.png' if '_' in self.wheel_4_1.source else self.wheel_4_1.source
					self.wheel_5_1.source = self.wheel_5_1.source.split('_')[0] + '.png' if '_' in self.wheel_5_1.source else self.wheel_5_1.source		
					self.wheel_1_2.source = self.wheel_1_2.source.split('_')[0] + '.png' if '_' in self.wheel_1_2.source else self.wheel_1_2.source
					self.wheel_2_2.source = self.wheel_2_2.source.split('_')[0] + '.png' if '_' in self.wheel_2_2.source else self.wheel_2_2.source
					self.wheel_3_2.source = self.wheel_3_2.source.split('_')[0] + '.png' if '_' in self.wheel_3_2.source else self.wheel_3_2.source
					self.wheel_4_2.source = self.wheel_4_2.source.split('_')[0] + '.png' if '_' in self.wheel_4_2.source else self.wheel_4_2.source
					self.wheel_5_2.source = self.wheel_5_2.source.split('_')[0] + '.png' if '_' in self.wheel_5_2.source else self.wheel_5_2.source		

	def update_statistics(self):
		self.check_input_size()
		self.change_number_of_symbols()	
		self.get_number_of_symbols()	
		self.change_payout()
		self.update_number_of_possible_ways()
		self.update_return()		

		sum_w1 = Game.w1_nS1 + Game.w1_nS2 +  Game.w1_nS3 +  Game.w1_nS4 +  Game.w1_nS5 +  Game.w1_nS6
		sum_w2 = Game.w2_nS1 + Game.w2_nS2 +  Game.w2_nS3 +  Game.w2_nS4 +  Game.w2_nS5 +  Game.w2_nS6
		sum_w3 = Game.w3_nS1 + Game.w3_nS2 +  Game.w3_nS3 +  Game.w3_nS4 +  Game.w3_nS5 +  Game.w3_nS6
		sum_w4 = Game.w4_nS1 + Game.w4_nS2 +  Game.w4_nS3 +  Game.w4_nS4 +  Game.w4_nS5 +  Game.w4_nS6
		sum_w5 = Game.w5_nS1 + Game.w5_nS2 +  Game.w5_nS3 +  Game.w5_nS4 +  Game.w5_nS5 +  Game.w5_nS6
		 
		self.gui_sum_n_possible_ways_5_times.text = str(locale.format_string('%d', int(self.gui_npw_s1_5times.text.replace('.','')) + int(self.gui_npw_s2_5times.text.replace('.','')) + int(self.gui_npw_s3_5times.text.replace('.','')) + int(self.gui_npw_s4_5times.text.replace('.','')) + int(self.gui_npw_s5_5times.text.replace('.','')) + int(self.gui_npw_s6_5times.text.replace('.','')), 1))
		self.gui_sum_n_possible_ways_4_times.text = str(locale.format_string('%d', int(self.gui_npw_s1_4times.text.replace('.','')) + int(self.gui_npw_s2_4times.text.replace('.','')) + int(self.gui_npw_s3_4times.text.replace('.','')) + int(self.gui_npw_s4_4times.text.replace('.','')) + int(self.gui_npw_s5_4times.text.replace('.','')) + int(self.gui_npw_s6_4times.text.replace('.','')), 1))
		self.gui_sum_n_possible_ways_3_times.text = str(locale.format_string('%d', int(self.gui_npw_s1_3times.text.replace('.','')) + int(self.gui_npw_s2_3times.text.replace('.','')) + int(self.gui_npw_s3_3times.text.replace('.','')) + int(self.gui_npw_s4_3times.text.replace('.','')) + int(self.gui_npw_s5_3times.text.replace('.','')) + int(self.gui_npw_s6_3times.text.replace('.','')), 1))
		
		self.gui_sum_return_5_times.text = str(locale.format_string('%d', int(self.gui_return_s1_5times.text.replace('.','')) + int(self.gui_return_s2_5times.text.replace('.','')) + int(self.gui_return_s3_5times.text.replace('.','')) + int(self.gui_return_s4_5times.text.replace('.','')) + int(self.gui_return_s5_5times.text.replace('.','')) + int(self.gui_return_s6_5times.text.replace('.','')), 1))
		self.gui_sum_return_4_times.text = str(locale.format_string('%d', int(self.gui_return_s1_4times.text.replace('.','')) + int(self.gui_return_s2_4times.text.replace('.','')) + int(self.gui_return_s3_4times.text.replace('.','')) + int(self.gui_return_s4_4times.text.replace('.','')) + int(self.gui_return_s5_4times.text.replace('.','')) + int(self.gui_return_s6_4times.text.replace('.','')), 1))
		self.gui_sum_return_3_times.text = str(locale.format_string('%d', int(self.gui_return_s1_3times.text.replace('.','')) + int(self.gui_return_s2_3times.text.replace('.','')) + int(self.gui_return_s3_3times.text.replace('.','')) + int(self.gui_return_s4_3times.text.replace('.','')) + int(self.gui_return_s5_3times.text.replace('.','')) + int(self.gui_return_s6_3times.text.replace('.','')), 1))
		

		self.gui_w1_nS6_sum.text = str(sum([Game.w1_nS1, Game.w1_nS2, Game.w1_nS3, Game.w1_nS4, Game.w1_nS5, Game.w1_nS6]))
		self.gui_w2_nS6_sum.text = str(sum([Game.w2_nS1, Game.w2_nS2, Game.w2_nS3, Game.w2_nS4, Game.w2_nS5, Game.w2_nS6]))
		self.gui_w3_nS6_sum.text = str(sum([Game.w3_nS1, Game.w3_nS2, Game.w3_nS3, Game.w3_nS4, Game.w3_nS5, Game.w3_nS6]))
		self.gui_w4_nS6_sum.text = str(sum([Game.w4_nS1, Game.w4_nS2, Game.w4_nS3, Game.w4_nS4, Game.w4_nS5, Game.w4_nS6]))
		self.gui_w5_nS6_sum.text = str(sum([Game.w5_nS1, Game.w5_nS2, Game.w5_nS3, Game.w5_nS4, Game.w5_nS5, Game.w5_nS6]))
		
		self.gui_nr_total_coms.text = f'{sum_w1} * {sum_w2} * {sum_w3} * {sum_w4} * {sum_w5}'
		self.gui_nr_total_coms_sum.text = str(locale.format_string('%d', sum_w1*sum_w2*sum_w3*sum_w4*sum_w5, 1))
		
		self.gui_likelihood_getting_line.text = f'({self.gui_sum_n_possible_ways_5_times.text} + {self.gui_sum_n_possible_ways_4_times.text} + {self.gui_sum_n_possible_ways_3_times.text})\n------------------------------------------------\n                  {self.gui_nr_total_coms_sum.text}'
		self.gui_gui_likelihood_getting_line_percent.text = str(round((int(self.gui_sum_n_possible_ways_5_times.text.replace('.','')) + int(self.gui_sum_n_possible_ways_4_times.text.replace('.','')) + int(self.gui_sum_n_possible_ways_3_times.text.replace('.',''))) / int(self.gui_nr_total_coms_sum.text.replace('.',''))*100,2)) + '%'
		
		self.gui_expected_return.text = f'({self.gui_sum_return_5_times.text} + {self.gui_sum_return_4_times.text} + {self.gui_sum_return_3_times.text})\n------------------------------------------------------\n                        {self.gui_nr_total_coms_sum.text}'
		self.gui_expected_return_percent.text = str(round((int(self.gui_sum_return_5_times.text.replace('.','')) + int(self.gui_sum_return_4_times.text.replace('.','')) + int(self.gui_sum_return_3_times.text.replace('.','')))/int(self.gui_nr_total_coms_sum.text.replace('.',''))*100,2)) + '%'
		
	def refill_credits(self):
		if int(self.refilled_credits.text) > 999999:
			self.refilled_credits.text = '999999'
			
		credits = int(self.refilled_credits.text)			
		Game.credits = credits	
		self.credits.text = str(Game.get_credits())
		
	def test_run(self):
		threading.Thread(target=self.test_run_thread).start()	
	
	def test_run_thread(self):
		run_count = int(self.gui_test_run.text)
		Game.credits = run_count
		for i in range(run_count):
			Game.start_round()
			self.credits.text = str(Game.get_credits())	
			self.get_rows()
			self.color_winning_lines(0)
		self.color_winning_lines(1)


class SlotmachineGUI(App):
	def build(self):
		return MyGrid()
	
if __name__ == '__main__':
	SlotmachineGUI().run()