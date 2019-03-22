import random
import math
import logging

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)

# logging.debug('This message should appear on the console')
# logging.info('So should this')
# logging.warning('And this, too')

# https://www.youtube.com/watch?v=DntEoGG7RyY&t=302s

def best_score(scores):
	best_score = math.fabs(scores[0] - 21)
	for score in scores:
		score = math.fabs(score - 21)
		if score <= best_score:
			best_score = score
	return best_score

def calculate_score(cards):
	scores = [0]
	for card in cards:
		scores[-1] += card
		if card == 1:
			scores.append(scores[-1] - card)
			scores[-1] += 10
	return best_score(scores)

# init 1 to 10 for each color
deck = (list(range(1,10)) * 4)
# add Jack,Queen and King == 10
deck.extend([10] * 12)
# shuffle the cards
random.shuffle(deck)
logging.info('Deck initialised...')


player_cards = []
dealer_cards = []
last_score = float("inf")

while(True):
	# take the first card in the deck
	player_cards.append(deck.pop())
	# shuffle the cards
	random.shuffle(deck)
	score = calculate_score(player_cards)
	# stop taking cards if score is greater than 18
	if score <= 3 or score >= last_score:
		break
	last_score = calculate_score(player_cards)
logging.info('Player done playing...')

last_score = float("inf")

while(True):
	# take the first card in the deck
	dealer_cards.append(deck.pop())
	# shuffle the cards
	random.shuffle(deck)
	score = calculate_score(dealer_cards)
	# stop taking cards if score is greater than 18
	if score <= 3 or score >= last_score:
		break
	last_score = calculate_score(dealer_cards)
logging.info('Dealer done playing...')

print("(Cards)    Player: {} Dealer: {}".format(player_cards,dealer_cards))
print("(Scores)   Player: {} Dealer: {}".format(calculate_score(player_cards),calculate_score(dealer_cards)))
