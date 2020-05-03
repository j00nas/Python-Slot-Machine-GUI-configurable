from random import randint
from numpy import mean
import sys
import time

class Slotmachine_engine():

	def __init__(self, bet, credits, 
			##Number of symbols on each wheel
			w1_nS1 = 6, w1_nS2 = 5, w1_nS3 = 5, w1_nS4 = 5, w1_nS5 = 2, w1_nS6 = 1, 
			w2_nS1 = 6, w2_nS2 = 5, w2_nS3 = 4, w2_nS4 = 3, w2_nS5 = 5, w2_nS6 = 1, 
			w3_nS1 = 8, w3_nS2 = 5, w3_nS3 = 4, w3_nS4 = 4, w3_nS5 = 2, w3_nS6 = 1, 
			w4_nS1 = 6, w4_nS2 = 5, w4_nS3 = 4, w4_nS4 = 3, w4_nS5 = 5, w4_nS6 = 1, 
			w5_nS1 = 8, w5_nS2 = 5, w5_nS3 = 4, w5_nS4 = 4, w5_nS5 = 2, w5_nS6 = 1, 
			##Payout per symbol per number of hits from left to right
			s1_5times = 20, s1_4times = 6, s1_3times = 1, 
			s2_5times = 24, s2_4times = 10, s2_3times = 3, 
			s3_5times = 28, s3_4times = 14, s3_3times = 3, 
			s4_5times = 32, s4_4times = 18, s4_3times = 3, 
			s5_5times = 40, s5_4times = 30, s5_3times = 4, 
			s6_5times = 2000, s6_4times = 1000, s6_3times = 20):
		self.bet = bet
		self.credits = credits
		self.win_total = 0
		self.rows = []
		self.win_round = 0
		self.winning_lines = []
		self.w1_nS1 = w1_nS1
		self.w1_nS2 = w1_nS2
		self.w1_nS3 = w1_nS3
		self.w1_nS4 = w1_nS4
		self.w1_nS5 = w1_nS5
		self.w1_nS6 = w1_nS6		
		self.w2_nS1 = w2_nS1
		self.w2_nS2 = w2_nS2
		self.w2_nS3 = w2_nS3
		self.w2_nS4 = w2_nS4
		self.w2_nS5 = w2_nS5
		self.w2_nS6 = w2_nS6
		self.w3_nS1 = w3_nS1
		self.w3_nS2 = w3_nS2
		self.w3_nS3 = w3_nS3
		self.w3_nS4 = w3_nS4
		self.w3_nS5 = w3_nS5
		self.w3_nS6 = w3_nS6
		self.w4_nS1 = w4_nS1
		self.w4_nS2 = w4_nS2
		self.w4_nS3 = w4_nS3
		self.w4_nS4 = w4_nS4
		self.w4_nS5 = w4_nS5
		self.w4_nS6 = w4_nS6
		self.w5_nS1 = w5_nS1
		self.w5_nS2 = w5_nS2
		self.w5_nS3 = w5_nS3
		self.w5_nS4 = w5_nS4
		self.w5_nS5 = w5_nS5
		self.w5_nS6 = w5_nS6
		self.s1_3times = s1_3times
		self.s1_4times = s1_4times
		self.s1_5times = s1_5times
		self.s2_3times = s2_3times
		self.s2_4times = s2_4times
		self.s2_5times = s2_5times		
		self.s3_3times = s3_3times
		self.s3_4times = s3_4times
		self.s3_5times = s3_5times			
		self.s4_3times = s4_3times
		self.s4_4times = s4_4times
		self.s4_5times = s4_5times			
		self.s5_3times = s5_3times
		self.s5_4times = s5_4times
		self.s5_5times = s5_5times		
		self.s6_3times = s6_3times
		self.s6_4times = s6_4times
		self.s6_5times = s6_5times	
		self.w1 = ''
		self.w2 = ''
		self.w3 = ''
		self.w4 = ''
		self.w5 = ''
		#self.main()
		
		
	def start_round(self):
		if self.credits != 0:
			#print(f'Your credits is: {self.credits}')
			#print(f'Your bet is: {self.bet}')
			#input('Press Enter to start a round\n')
			self.credits -= self.bet
			self.roll_wheels()
		#else:
			#print('no more money')
	
	
	def roll_wheels(self):
		self.w1 = ['10']*self.w1_nS1 + ['Jack']*self.w1_nS2 + ['Queen']*self.w1_nS3 + ['King']*self.w1_nS4 + ['Ace']*self.w1_nS5 + ['SEVEN']*self.w1_nS6
		self.w2 = ['10']*self.w2_nS1 + ['Jack']*self.w2_nS2 + ['Queen']*self.w2_nS3 + ['King']*self.w2_nS4 + ['Ace']*self.w2_nS5 + ['SEVEN']*self.w2_nS6
		self.w3 = ['10']*self.w3_nS1 + ['Jack']*self.w3_nS2 + ['Queen']*self.w3_nS3 + ['King']*self.w3_nS4 + ['Ace']*self.w3_nS5 + ['SEVEN']*self.w3_nS6
		self.w4 = ['10']*self.w4_nS1 + ['Jack']*self.w4_nS2 + ['Queen']*self.w4_nS3 + ['King']*self.w4_nS4 + ['Ace']*self.w4_nS5 + ['SEVEN']*self.w4_nS6
		self.w5 = ['10']*self.w5_nS1 + ['Jack']*self.w5_nS2 + ['Queen']*self.w5_nS3 + ['King']*self.w5_nS4 + ['Ace']*self.w5_nS5 + ['SEVEN']*self.w5_nS6
		wheels = [self.w1, self.w2, self.w3, self.w4, self.w5]

		output_all_wheels = []
		for i in wheels:
			output_one_wheel = []
			for j in range(5):
				random_number = randint(0,len(i)-1)
				n1 = i[random_number]
				output_one_wheel.append(n1)
				i.remove(n1)
			output_all_wheels.append(tuple(output_one_wheel))
		
		##possible winning_rows - 5 winning lines
		first_winning_line = (output_all_wheels[0][0], output_all_wheels[1][0], output_all_wheels[2][0], output_all_wheels[3][0], output_all_wheels[4][0])
		second_winning_line = (output_all_wheels[0][1], output_all_wheels[1][1], output_all_wheels[2][1],  output_all_wheels[3][1],  output_all_wheels[4][1])
		third_winning_line = (output_all_wheels[0][2], output_all_wheels[1][2], output_all_wheels[2][2], output_all_wheels[3][2], output_all_wheels[4][2])
		fourth_winning_line = (output_all_wheels[0][0], output_all_wheels[1][1], output_all_wheels[2][2], output_all_wheels[3][1], output_all_wheels[4][0])
		fifth_winning_line = (output_all_wheels[0][2], output_all_wheels[1][1], output_all_wheels[2][0], output_all_wheels[3][1], output_all_wheels[4][2])
		
		self.check_win(first_winning_line, second_winning_line, third_winning_line, fourth_winning_line, fifth_winning_line)
	
	
	def check_win(self, first_winning_line, second_winning_line, third_winning_line, fourth_winning_line, fifth_winning_line):
		winning_lines = [first_winning_line, second_winning_line, third_winning_line, fourth_winning_line, fifth_winning_line]
		
		visible_rows = [first_winning_line, second_winning_line, third_winning_line]
		self.rows = visible_rows
		#for i in visible_rows:
			#print(f'{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t')
	
		
		winning_table = {
						('10','10','10') : self.s1_3times, 
						('Jack', 'Jack', 'Jack') : self.s2_3times,
						('Queen', 'Queen', 'Queen') : self.s3_3times,
						('King', 'King', 'King') : self.s4_3times,
						('Ace', 'Ace', 'Ace') : self.s5_3times,
						('SEVEN', 'SEVEN', 'SEVEN'): self.s6_3times,
						('10','10','10', '10') : self.s1_4times, 
						('Jack', 'Jack', 'Jack','Jack') : self.s2_4times,
						('Queen', 'Queen', 'Queen', 'Queen') : self.s3_4times,
						('King', 'King', 'King', 'King') : self.s4_4times,
						('Ace', 'Ace', 'Ace', 'Ace') : self.s5_4times,
						('SEVEN', 'SEVEN', 'SEVEN', 'SEVEN'): self.s6_4times,	
						('10','10','10', '10', '10') : self.s1_5times, 
						('Jack', 'Jack', 'Jack','Jack', 'Jack') : self.s2_5times,
						('Queen', 'Queen', 'Queen', 'Queen', 'Queen') : self.s3_5times,
						('King', 'King', 'King', 'King', 'King') : self.s4_5times,
						('Ace', 'Ace', 'Ace', 'Ace', 'Ace') : self.s5_5times,
						('SEVEN', 'SEVEN', 'SEVEN', 'SEVEN', 'SEVEN'): self.s6_5times							
						}
		
		self.win_round = 0
		counter = 0
		self.winning_lines = []
		for i in winning_lines:
			if i[0] == i[1] and i[0] == i[2] and i[0] != i[3]:
				self.win_round += winning_table[i[:3]]
				self.winning_lines.append([counter,3])
			if i[0] == i[1] and i[0] == i[2] and i[0] == i[3] and i[0] != i[4]:
				self.win_round += winning_table[i[:4]]	
				self.winning_lines.append([counter,4])
			if i in winning_table:
				self.win_round += winning_table[i]
				self.winning_lines.append([counter,5])
			counter += 1
		#print(f'\nYou won: {self.win_round}')
		self.credits += self.win_round	
		#print(self.winning_lines)
		
		
	def main(self):
		while self.credits != 0:
			#print('\n')
			self.start_round()
		#print(f'Your credits is: {self.credits}')
		#print(f'Your bet is: {self.bet}')		
	
	def get_credits(self):
		if self.credits > 0:
			return str(self.credits)
		else:
			return str('Game Over')
			
	def get_rows(self):
		if self.rows == []:
			return [('W1-0', 'W2-0', 'W3-0', 'W4-0', 'W5-0'), ('W1-1', 'W2-1', 'W3-1', 'W4-1', 'W5-1'), ('W1-2', 'W2-2', 'W3-2', 'W4-2', 'W5-2')]
		else:
			return self.rows
	
	def get_win(self):
		return self.win_round
	
	def get_winnig_lines(self):
		return self.winning_lines
		
	
#Slotmachine_engine(1, 50)
		
#test_outcome = []
#for i in range(99):
#	x = Slotmachine(1, 100)
#	test_outcome.append(x.credits)
#print('\n' + str(test_outcome))
#print('\n' + str(mean(test_outcome)))
				
			
			
		
		
		