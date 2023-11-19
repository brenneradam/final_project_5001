import random
import time

MINIMUM_BET = 25

MIN_BET_MSG = f'Place your bet (min. ${MINIMUM_BET}): '
BLACKJACK_DEALER_MSG = 'Blackjack - Dealer Wins :('
BLACKJACK_PLAYER_MSG = 'Blackjack - You Win!'
BLACKJACK_PUSH_MSG = 'Push - blackjack for everyone'
BLACKJACK_NOBODY_HOME_MSG = "Dealer checked for Blackjack ... Nobody's Home!"
INSURANCE_QUESTION_MSG = 'Would you like insurance on your hand (Y / N)?: '
INVALID_INPUT_MSG = 'Invalid Input: Please Try Again!'
INSUFFICIENT_FUNDS_MSG = 'Insufficent Funds: Please visit menu to deposit funds.'
MIN_BET_ERROR_MSG = 'Minimum bet not satisifed: Please place a bet equal or greater than the table minimum.'

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
    
    bet_amount = input(MIN_BET_MSG)  # prompt the user to enter their bet

    if bet_amount.isdigit() == False:  # if the bet is not an integer
        print(INVALID_INPUT_MSG)  # reprompt
        return place_bet(wallet_value)
    
    bet_amount = int(bet_amount)  # convert the str to int

    if (wallet_value - bet_amount) < 0:  # if the bet can't be covered by the wallet amount
        print(INSUFFICIENT_FUNDS_MSG)  # reprompt
        return place_bet(wallet_value)
    
    elif bet_amount < MINIMUM_BET:  # if the bet does not meet the minimum
        print(MIN_BET_ERROR_MSG)  # re-prompt
        return place_bet(wallet_value)
    
    return bet_amount

def hand_calculator(hand:list) -> int:
    '''
    Takes a hand of cards and calculates the value of the hand; 
    Aces will default as high (11) until the hand value exceeds 21, in which case the ace value(s) will revert to low (1) automatically.

    Arguments:
        hand: list of card that make up the blackjack hand - can be either player or dealer

    Returns:
        hand_value: the value of the blackjack hand 
    '''

    hand_value = 0
    ace_cnt = 0

    for card in hand:  # iterating through hand
        
        if card[:-1] == 'A':  # if the card is an ace
            ace_cnt += 1  # count it and move on (will handle in the end)
        
        else:
            hand_value += doc_values[card[:-1]]  # all non-ace cards, add the card value to the hand value
    
    for ace in range(ace_cnt):  # for the number of aces counted

        if hand_value + 11 > 21:  # if the ace will send the hand over the top, count it as a hard ace (1)
            hand_value += 1
        else:  # otherwise, count it as a soft ace (11)
            hand_value += 11

    return hand_value

def dealer_play(hand:object) -> None:
    '''
    Automatic hitting for the dealer, based on soft 17 gameplay.

    Arguments:
        hand: a hand of blackjack
    '''
        
    while hand.value() < 17:  # soft 17 - dealer will stand on soft 17 or higher
        
        hit_card = hand.hit()  # hand hit

        print(f"Dealer was dealt the {card_to_text(hit_card)} ... their hand value is now {hand.value()}")

def card_to_text(card:str) -> str:
    '''
    Takes a card from the deck and represents in a phrase

    Arguments:
        card: the card from a deck of cards, with value and suit
    
    Returns:
        return_str: the phrase representation of a card (i.e., 10H = 10 of Hearts)
    '''

    return_str = ''

    return_str += (card[:-1] + ' of ' + suit_values[card[-1]])

    return return_str

def client_option_reader(input_msg:str, options:tuple) -> str:
    '''
    Prompts the user with a message, and checks for valid, inputted commands

    Arguments:
        input_msg: what the user sees at the console
        options: the valid strings that the user can enter
    
    Returns:
        client: the valid option entered, from options
    '''

    client = input(input_msg)  # prompts the user with a message at the console

    client = client.strip()  # stripping any whitespace

    if client in options:  # if the stripped input exists within the options

        return client  # return that input

    else:

        print(INVALID_INPUT_MSG)  # prompt the user that their input is not within the the set of expected options

        return client_option_reader(input_msg, options)  # reprompt them with the client_option_reader()

def play_game(wallet:int=100) -> int:

    bet = place_bet(wallet)  # place your inital bet

    wallet -= bet  # subtracting the initial bet from wallet value

    insurance = 0  # initializing insurance amount of zero

    player = BlackjackHand()  # creating a random hand for the player
    dealer = BlackjackHand()  # creating a random hand for the dealer

    print(f'Your hand is the {card_to_text(player.hand[0])}' + ' & ' + f'{card_to_text(player.hand[1])}, with a value of {str(player.value())}')

    print(f'Dealer showing {card_to_text(dealer.hand[0])}')

    if doc_values[dealer.hand[0][:-1]] == 10 or dealer.hand[0][:-1] == 'A':  # if the dealer shows a card worthy of checking for blackjack

        if (wallet - (bet / 2)) >= 0:  # if you can still affort the insurance price, we will ask if you would like insurance

            question = client_option_reader(INSURANCE_QUESTION_MSG, ('Y','N'))  # asking about insurance

            if question == 'Y':  # if the user prompts yes, they will be charged 50% of their initial bet
                insurance += (.5 * bet)  # funds applied to insurance
                wallet -= insurance  # insurance taken out of wallet
    
        if dealer.value() == 21 and player.value() != 21:  # if the dealer has blackjack and the user does NOT

            print(BLACKJACK_DEALER_MSG)  # informing user of loss

            wallet += (insurance * 3)  # wallet gets 3x their insurance bet; this includes inital insurance bet (1x) + 2:1 winnings (2x)

            return wallet
        
        elif dealer.value() == 21 and player.value() == 21:  # if both dealer and player have 21

            print(BLACKJACK_PUSH_MSG)  # informing user of push

            wallet += (bet + (insurance * 3))  # user gets their original bet back + 3x insurance (if any)

            return wallet
        
        else:  # if there is no scenario where the dealer has blackjack

            print(BLACKJACK_NOBODY_HOME_MSG)  # nobody is home!

    if player.value() == 21:  # if the player has blackjack

        print(BLACKJACK_PLAYER_MSG)  # winner winner !
        wallet += (2.5 * bet) - insurance  # return the original bet and 1.5x that amount

        return wallet

    stay = False
    double_down = False

    while player.value() < 21 and stay == False and double_down == False:

        if len(player.hand) == 2 and (wallet - bet) >= 0:  # if you still have your initally dealt hand and can afford another bet, you are presented with 
                                                            # a double down opportunity

            move = client_option_reader('Would you like to Stay [S] / Hit [H] / Double Down [D]?: ', ('S','H','D'))

        else:

            move = client_option_reader('Would you like to Stay [S] / Hit [H]?: ',('S','H'))

        if move == 'H':  # if you are opting to hit
            hit_card = player.hit()  # the player's hand get hit
            print(f"You were dealt the {card_to_text(hit_card)} ... your hand value is now {player.value()}")
        
        elif move == 'S':  # if you are staying, set the stay variable to True to break while loop
            stay = True
        
        elif move == 'D':  # if you are doubling down
            wallet -= bet  # subtract an additional bet from the user's wallet
            hit_card = player.hit()  # take a hit
            print(f"Doubled Down! You were dealt the {card_to_text(hit_card)} ... your hand value is now {player.value()}")
            double_down = True  # set the double down variable to True to break the loop

    if player.value() > 21:  # if the player has over 21 (busted)
        print(f'You busted with {str(player.value())}')
        return wallet  # current value of wallet, with losses already reflected
    
    print(f'Dealer flips ... their hidden card is a {card_to_text(dealer.hand[1])}, yielding a dealer hand value of {dealer.value()}')
    dealer_play(dealer)  # dealer automatically hits until they hit hard 17+ or bust

    if dealer.value() > 21:  # if the dealer busts
        print('Dealer Busted - You Win!')
        wallet += (bet * 2)  # player gets original bet plus 1x in winnings
        return wallet
    elif dealer.value() > player.value():  # if the dealer beats the player's hand
        print('Dealer wins!')
        return wallet  # current value of wallet, with losses already reflected
    elif dealer.value() < player.value():  # if the player beats the dealer's hand,
        print('Player wins!')
        wallet += (bet * 2)  # player gets original bet plus 1x in winnings
        return wallet
    else:  # both player and dealer have hands of equal value
        print('Push - nobody wins!')
        wallet += bet  # player gets original bet back
        return wallet
    
# user tracking functionality

def user_credentials() -> (str, str):

    username = input('Please enter your username: ')  # user inputs their username
    password = input('Please enter your password (case sensitive): ')  # user inputs their password

    username = username.strip()
    password = password.strip()

    return username, password

def user_login(username:str, password:str) -> list:

    try:
        
        with open('blackjack_account_log.txt', 'r') as file:  # trying to open the account log
            
            for line in file:  # for each line in the file

                account = line.split(',')  # split all the account information (comma seperated)

                if account[0] == username:  # if the username (in account line) matches the provided username

                    if account[1].strip() == password:  # if the user name and password match

                        return account  # return all the account information
                
                    elif account[1].strip() != password:  # if the username matches but the password does not

                        print('Invalid password - please try again')

                        return None
                
                else:

                    pass
                    
        print(f"We can't find an account under the provided username: {username} - please create an account to get started!")  # inidicate if there is no username

        return None
    
    except FileNotFoundError:

        print('No users found - please create a user account to get started!')

        return None

def user_already_exists(user:str) -> bool:

    with open('blackjack_account_log.txt', 'r') as file:  # open the file

        for line in file:  # iterate through each line

            x = line.split(',')  # split up the account information (comma seperated)

            if x[0] == user:  # if the username exists, return True

                return True
            
def new_user():

    user, pwd = user_credentials()  # get credentials

    try:  # if the file exists

        exists = False

        with open('blackjack_account_log.txt', 'r') as file:  # read the file
            
            if user_already_exists(user) == True:  # if the username already exists
                print('Username already in use - please specify a unique username!')
                exists = True

        if exists != True:

            with open('blackjack_account_log.txt', 'a') as file: 

                file.write(f'{user},{pwd},0\n')
                print(f'Username: {user}')
                print(f'Password: {pwd}')
                print(f'Wallet: $0')

    except FileNotFoundError:

        with open('blackjack_account_log.txt', 'w') as file:

            file.write(f'{user},{pwd},0\n')
            print(f'Username: {user}')
            print(f'Password: {pwd}')
            print(f'Wallet: $0')

def main():

    ## menu
    ## wallet loading

    pass

# wallet = 100

# while wallet > 0:
#     inital_wallet = wallet
#     print(f'Wallet Amount: ${str(wallet)}')
#     wallet = play_game(wallet)
#     if inital_wallet > wallet:
#         print(f'You Lost: ${str(abs(inital_wallet - wallet))}')
#     elif inital_wallet < wallet:
#         print(f'You Won: ${str(abs(inital_wallet - wallet))}')
    
print(user_login('adambrenner2','abc'))