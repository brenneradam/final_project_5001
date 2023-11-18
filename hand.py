import random
MINIMUM_BET = 25

BLACKJACK_DEALER_MSG = 'Blackjack - Dealer Wins :('
BLACKJACK_PLAYER_MSG = 'Blackjack - You Win!'
BLACKJACK_PUSH_MSG = 'Push - blackjack for everyone'
BLACKJACK_NOBODY_HOME = "Dealer checked for Blackjack ... Nobody's Home!"
INSURANCE_QUESTION = 'Would you like insurance on your hand (Y / N)?: '
INVALID_INPUT = 'Invalid Input: Please Try Again!'

doc = ('AH','AD','AC','AS',
       'KH','KD','KC','KS',
       'QH','QD','QC','QS',
       'JH','JD','JC','JS',
       '10H','10D','10C','10S',
       '9H','9D','9C','9S',
       '8H','8D','8C','8S',
       '7H','7D','7C','7S',
       '6H','6D','6C','6S',
       '5H','5D','5C','5S',
       '4H','4D','4C','4S',
       '3H','3D','3C','3S',
       '2H','2D','2C','2S')

doc_values = {'A' : None,
              'K' : 10,
              'Q' : 10,
              'J' : 10,
              '10': 10,
              '9' : 9,
              '8' : 8,
              '7' : 7,
              '6' : 6, 
              '5' : 5, 
              '4' : 4,
              '3' : 3,
              '2' : 2}

suit_values = {'H':'Hearts','D':'Diamonds','C':'Clubs','S':'Spades'}

class BlackjackHand:
    '''
    Represents a hand of blackjack
    '''

    def __init__(self):

        self.hand = [random.choice(doc),random.choice(doc)]

    def hit(self):

        self.hand.append(random.choice(doc))

        return self.hand[-1]
    
    def value(self):

        return hand_calculator(self.hand)
    
    def split(self):

        split_card = self.hand[1]

        split_1 = BlackjackHand()
        split_1.hand[0] = split_card

        split_2 = BlackjackHand()
        split_2.hand[0] = split_card

        return split_1, split_2

def place_bet(wallet_value:int) -> int:
    '''
    Prompts the user to place a bet; required to be equal or greater than minimum bet

    Arguments:
        wallet_value: the amount of money available in the user's account
    
    Returns:
        bet_amount: the amount of the money the user is wagering from their wallet
    '''
    
    bet_amount = input(f'Place your bet (min. ${MINIMUM_BET}): ')

    if bet_amount.isdigit() == False:
        print(f'Invalid Input: Please re-enter a valid bet amount.')
        return place_bet(wallet_value)
    
    bet_amount = int(bet_amount)

    if (wallet_value - bet_amount) < 0:
        print('Insufficent Funds: Please visit menu to deposit funds.')
        return place_bet(wallet_value)
    
    elif bet_amount < 25:
        print(f'Minimum bet not satisifed: Please place a bet equal or greater than the table minimum.')
        return place_bet(wallet_value)
    
    return bet_amount

def hand_calculator(hand:list) -> int:
    '''
    Takes a hand of cards (list) and calculates the value of the hand; 
    Aces will default as high (11) until the hand value exceeds 21, in which case the ace value(s) will revert to low (1) automatically.

    Arguments:
        hand: list of card (codes) that make up blackjack hand - can be either player or dealer

    Returns:
        hand_value: the value of the blackjack hand 
    
    '''

    hand_value = 0
    ace_cnt = 0

    for card in hand:
        
        if card[:-1] == 'A':
            ace_cnt += 1
        
        else:
            hand_value += doc_values[card[:-1]]
    
    for ace in range(ace_cnt):

        if hand_value + 11 > 21:
            hand_value += 1
        else:
            hand_value += 11

    return hand_value

def dealer_play(hand:object) -> None:

    # soft 17 - dealer will stand on soft 17 or higher
        
    while hand.value() < 17:

        hit_card = hand.hit()

        print(f"Dealer was dealt the {card_to_text(hit_card)} ... their hand value is now {hand.value()}")

def card_to_text(card:str) -> str:

    return_str = ''

    return_str += (card[:-1] + ' of ' + suit_values[card[-1]])

    return return_str

def client_option_reader(input_msg:str, options:tuple) -> str:

    client = input(input_msg)

    client = client.strip()

    if client in options:

        return client

    else:

        print(INVALID_INPUT)

        return client_option_reader(input_msg, options)
    
def insurance_play(dealer:object, player:object, wallet:int, bet:int) -> (bool, int, str):

    insurance = 0

    if (wallet - (bet * 1.5)) >= 0:

        question = client_option_reader(INSURANCE_QUESTION, ('Y','N'))

        if question == 'Y':
            insurance += (.5 * bet)

    if dealer.value() == 21 and player.value() != 21:

        return True, (-1 * bet) + (insurance * 2), BLACKJACK_DEALER_MSG
    
    elif dealer.value() == 21 and player.value() == 21:

        return True, 0 + (insurance * 2), BLACKJACK_PUSH_MSG
    
    else:

        return False, insurance, BLACKJACK_NOBODY_HOME

def play_game(wallet:int=100):

    bet = place_bet(wallet)

    total_risk = bet
    insurance = 0

    player = BlackjackHand()
    dealer = BlackjackHand()

    print(f'Your hand is the {card_to_text(player.hand[0])}' + ' & ' + f'{card_to_text(player.hand[1])}, with a value of {str(player.value())}')
    print(f'Dealer showing {card_to_text(dealer.hand[0])}')

    # if doc_values[dealer_show_card[:-1]] == 10 or dealer_show_card[:-1] == 'A':

    #     if (wallet - (bet * 1.5)) >= 0:

    #         insurance_question = client_option_reader('Would you like insurance on your hand (Y / N)?: ', ('Y','N'))

    #         if insurance_question == 'Y':
    #             insurance += (.5 * bet)
    #             total_risk += insurance
    
    #     if dealer.value() == 21 and dealer.value() != 21:

    #         print(BLACKJACK_DEALER_MSG)

    #         return (-1 * bet) + (insurance * 2)  
        
    #     elif dealer.value() == 21 and player.value() == 21:
    #         print(BLACKJACK_PUSH_MSG)
    #         return 0 + (insurance * 2)
        
    #     else:
    #         print(BLACKJACK_NOBODY_HOME)

    if doc_values[dealer.hand[0][:-1]] == 10 or dealer.hand[0][:-1] == 'A':

        stop, value, msg = insurance_play(dealer, player, wallet, bet)

        if stop == True:

            print(msg)
            return value
        
        elif stop == False:

            print(msg)
            insurance += value
            total_risk += insurance

    ## this is where split comes into play .. think there needs to be recursion

    if player.value() == 21:
        print(BLACKJACK_PLAYER_MSG)
        return (1.5 * bet) - insurance

    stay = False
    double_down = False

    while player.value() < 21 and stay == False and double_down == False:

        if len(player.hand) == 2 and (wallet - total_risk - bet) >= 0:

            if player.hand[0][:-1] == player.hand[1][:-1]:

                move = client_option_reader('Would you like to Stay [S] / Hit [H] / Double Down [D] / Split [SS]?: ', ('S','H','D','SS'))

            else:

                move = client_option_reader('Would you like to Stay [S] / Hit [H] / Double Down [D]?: ', ('S','H','D'))

        else:

            move = client_option_reader('Would you like to Stay [S] / Hit [H]?: ',('S','H'))

        if move == 'H':
            hit_card = player.hit()
            print(f"You were dealt the {card_to_text(hit_card)} ... your hand value is now {player.value()}")
        
        elif move == 'S':
            stay = True
        
        elif move == 'D':
            bet = bet * 2
            total_risk += bet
            hit_card = player.hit()
            print(f"Doubled Down! You were dealt the {card_to_text(hit_card)} ... your hand value is now {player.value()}")
            double_down = True

        elif move == 'SS':

            continue

    if player.value() > 21:
        print(f'You busted with {str(player.value())}')
        return (-1 * bet) - insurance
    
    print(f'Dealer flips ... their hidden card is a {card_to_text(dealer.hand[1])}, yielding a dealer hand value of {dealer.value()}')
    
    dealer_play(dealer)

    if dealer.value() > 21:
        print('Dealer Busted - You Win!')
        return bet - insurance
    elif dealer.value() > player.value():
        print('Dealer wins!')
        return (-1 * bet) - insurance
    elif dealer.value() < player.value():
        print('Player wins!')
        return bet - insurance
    else:
        print('Push - nobody wins!')
        return 0 - insurance
    
def main():

    ## menu
    ## wallet loading

    pass

while True:
    play_game()