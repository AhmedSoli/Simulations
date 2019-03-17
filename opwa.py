# every participant is sent a letter explaining the following rules:
# there are n number of people who received the same letter as his
# there is an address listed in the letter
# if only one participant replies with another letter to the listed address
# then this participant will win 1Billion Dollars.
# if more than one participant replied or no one replied then no one wins the money

# the simulation forces all participants to act superrationaly
# participants are not allowed to communite with each other at any points
# they can use all the information mentioned in the letter

# the superrational solution is explained in this video: 
# https://www.youtube.com/watch?v=NkYCWqzBc7M&t=440s

from Participant import Participant

repetitions = 100
num_participants = int(10000000 * 0.999999)
limit = 1
results = []
participants = []

for ID in range(num_participants):
	participants.append(Participant(ID))

for repetition in range(repetitions):
	num_respones = 0
	for participant in participants:
		if participant.decide(num_participants):
			if num_respones >= limit:
				results.append(0)
				break
			else:
				num_respones += 1
	else:
		if num_respones == limit:
			results.append(1)
		else:
			results.append(0)

print(sum(results)/len(results))