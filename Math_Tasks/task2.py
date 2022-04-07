# You have an unbiased deck of cards (deck size = 52).
# The probability of finding an ACE will decrease with each successful draw.
# Let's say you got lucky & had a 100% success rate in drawing a specific card from the deck.
# Find the average rate of decrease of probability of finding an ACE.
# In how many tries will your probability go to 0?
# Write code to find the above.

cards = 52
aces = 4
diff = []
Sum = 0

print('Probability will be 0 in {} tries'.format(aces+1))

while aces != 1:
    prob1 = aces/cards
    prob2 = (aces-1)/(cards-1)
    change = prob1 - prob2
    diff.append(change)
    Sum += change
    aces -= 1
    cards -= 1
    
print('List of Difference in probabilities:', diff)
print('Avg. Rate of Decrease: {} %'.format(Sum/len(diff)*100))