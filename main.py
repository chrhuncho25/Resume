#Chris Cooper
#04/26/2024
#Blackjack Simulator




import random


#Function that draws a random card for you, this is the beginning of the game
def draw_card():
   cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
   return random.choice(cards)
#Function that calculates the value of the current hand that you have
def calculate_total_card(hand):
   total = 0
   num_aces = 0
   for card in hand:
       if card.isdigit():
           total += int(card)
       elif card in ['J', 'Q', 'K']:
           total += 10
       elif card == 'A':
           total += 11
           num_aces += 1
   while total > 21 and num_aces:
       total -= 10
       num_aces -= 1
   return total
#This function creates the round of blackjack
def play_blackjack():
   player_total_hand = [draw_card(), draw_card()]
   dealer_total_hand = [draw_card(), draw_card()]


   while True:
       print("Your current hand is :", player_total_hand, "Total:", calculate_total_card(player_total_hand))
       print("The Dealer's current hand is:", [dealer_total_hand[0], '*'])


       if calculate_total_card(player_total_hand) == 21:
           print("Blackjack! You win!")
           return 'win'
       elif calculate_total_card(player_total_hand) > 21:
           print("Busted! You lose.")
           return 'lose'


       action = input("Do you want to Hit (press H) or Stand? (press S) ").lower()
       if action == 'h':
           player_total_hand.append(draw_card())
       elif action == 's':
           break


   while calculate_total_card(dealer_total_hand) <= 16:
       dealer_total_hand.append(draw_card())


   print("Your hand is : ", player_total_hand, "Total:", calculate_total_card(player_total_hand))
   print("The Dealer's hand is : ", dealer_total_hand, "Total:", calculate_total_card(dealer_total_hand))


   player_total = calculate_total_card(player_total_hand)
   dealer_total = calculate_total_card(dealer_total_hand)


   if dealer_total > 21 or player_total > dealer_total:
       print("You win this round!")
       return 'win'
   elif player_total == dealer_total:
       print("It's a draw!")
       return 'draw'
   else:
       print("You have lost this round.")
       return 'lose'
#This function simulates multiple rounds of blackjack
def simulate_blackjack(num_hands):
   results_hit = {'win': 0, 'lose': 0, 'draw': 0}
   results_stand = {'win': 0, 'lose': 0, 'draw': 0}


   for _ in range(num_hands):
       starting_value = random.randint(4, 22)


       # This simulates the hitting
       result_hit = play_blackjack()
       results_hit[result_hit] += 1


       # THis simulates the standing
       player_hand = [str(starting_value)]
       result_stand = play_blackjack()
       results_stand[result_stand] += 1


   return results_hit, results_stand


if __name__ == "__main__":
   num_hands = 100000
   hit_results, stand_results = simulate_blackjack(num_hands)


   print("Results for hitting:")
   print("Win:", hit_results['win'])
   print("Lose:", hit_results['lose'])
   print("Draw:", hit_results['draw'])


   print("\nResults for standing:")
   print("Win:", stand_results['win'])
   print("Lose:", stand_results['lose'])
   print("Draw:", stand_results['draw'])
