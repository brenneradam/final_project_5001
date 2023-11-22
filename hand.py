"""
Blackack 1.0

A program that allows users to create an account, load their wallet, and play blackjack.

NAME: ADAM BRENNER
SEMESTER: FALL 2023
"""

import random

MINIMUM_BET = 25

MIN_BET_MSG = f'Place your bet (min. ${MINIMUM_BET}): '
BLACKJACK_DEALER_MSG = 'Blackjack - Dealer Wins :('
BLACKJACK_PLAYER_MSG = 'Blackjack - You Win!'
BLACKJACK_PUSH_MSG = 'Push - blackjack for everyone'
BLACKJACK_NOBODY_HOME_MSG = "Dealer checked for Blackjack ... Nobody's Home!"
INSURANCE_QUESTION_MSG = 'Would you like insurance on your hand (Y / N)?: '
INVALID_INPUT_MSG = 'Invalid Input: Please Try Again!'
INSUFFICIENT_FUNDS_MSG = 'Insufficent Funds: Please visit menu to deposit more funds.'
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
        '''

        '''

        self.hand = [random.choice(doc),random.choice(doc)]

    def hit(self):
        '''

        '''

        self.hand.append(random.choice(doc))

        return self.hand[-1]
    
    def value(self):
        '''
        '''

        return hand_calculator(self.hand)

def place_bet(wallet_value:int) -> int:
    '''
    Prompts the user to place a bet; required to be equal or greater than minimum bet

    Arguments:
        wallet_value: the amount of money available in the user's account
    
    Returns:
        bet_amount: the amount of the money the user is wagering from their wallet
    '''
    
    bet_amount = input(MIN_BET_MSG)  # prompt the user to enter their bet

    if bet_amount.isdigit() == False:  # if the bet is not a whole number ... does not support cents on the dollar
        print(INVALID_INPUT_MSG)  # reprompt
        return place_bet(wallet_value)
    
    bet_amount = float(bet_amount)  # convert the str to float

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
        hand: list of cards that make up the blackjack hand - can be either player or dealer

    Returns:
        hand_value: the counted value of the blackjack hand 
    '''

    hand_value = 0
    ace_cnt = 0

    for card in hand:  # iterating through each card in hand
        
        if card[:-1] == 'A':  # if the card is an ace
            ace_cnt += 1  # count it and move on (will handle in the end)
        
        else:
            hand_value += doc_values[card[:-1]]  # for all non-ace cards, add the card value to the hand value
    
    for ace in range(ace_cnt):  # for the number of aces counted

        if hand_value + 11 > 21:  # if the ace will put the hand over 21, count it as a hard ace (1)
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
    Takes a card from the deck and represents it in a phrase

    Arguments:
        card: the card from a deck of cards, with value and suit
    
    Returns:
        return_str: the phrase representation of a card (i.e., 10H = 10 of Hearts)
    '''

    return_str = (card[:-1] + ' of ' + suit_values[card[-1]])  # phrase creation

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
    '''
    Replicates the player experience in a single game of blackjack.

    Arguments:
        wallet: the amount of funds a user has to spend at the blackjack table
    
    Returns:
        wallet: the user's updated wallet value, reflecting the winnings / losses from the single game of blackjack
    '''

    bet = place_bet(wallet)  # place your inital bet

    wallet -= bet  # subtracting the initial bet from the user's wallet value

    insurance = 0  # initializing insurance amount of zero

    player = BlackjackHand()  # creating a random hand for the player
    dealer = BlackjackHand()  # creating a random hand for the dealer

    print(f'Your hand is the {card_to_text(player.hand[0])}' + ' & ' + f'{card_to_text(player.hand[1])}, with a value of {str(player.value())}')

    print(f'Dealer showing {card_to_text(dealer.hand[0])}')

    if doc_values[dealer.hand[0][:-1]] == 10 or dealer.hand[0][:-1] == 'A':  # if the dealer shows a card worthy of checking for blackjack

        if (wallet - (bet / 2)) >= 0:  # if you can still afford the insurance price, we will ask if you would like insurance

            question = client_option_reader(INSURANCE_QUESTION_MSG, ('Y','N'))  # asking about insurance

            if question == 'Y':  # if the user prompts yes, they will be charged 50% of their initial bet
                insurance += (.5 * bet)  # funds applied to insurance
                wallet -= insurance  # insurance taken out of wallet
    
        if dealer.value() == 21 and player.value() != 21:  # if the dealer has blackjack and the user does NOT
            
            print(f'Dealer flips ... their hidden card is a {card_to_text(dealer.hand[1])}, yielding a dealer hand value of {dealer.value()}')
            print(BLACKJACK_DEALER_MSG)  # informing user of loss

            wallet += (insurance * 3)  # wallet gets 3x their insurance bet; this includes inital insurance bet (1x) + 2:1 winnings (2x)

            return wallet
        
        elif dealer.value() == 21 and player.value() == 21:  # if both dealer and player have 21

            print(f'Dealer flips ... their hidden card is a {card_to_text(dealer.hand[1])}, yielding a dealer hand value of {dealer.value()}')
            print(BLACKJACK_PUSH_MSG)  # informing user of push

            wallet += (bet + (insurance * 3))  # user gets their original bet back + 3x insurance (if any)

            return wallet
        
        else:  # if there is no scenario where the dealer has blackjack

            print(BLACKJACK_NOBODY_HOME_MSG)  # nobody is home!

    if player.value() == 21:  # if the player has blackjack

        print(BLACKJACK_PLAYER_MSG)  # winner winner !
        wallet += (2.5 * bet)  # return the original bet and 1.5x that amount

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
        
        elif move == 'D':  # if you are doubling down - no need to check if you can afford (done above)
            wallet -= bet  # subtract an additional bet from the user's wallet
            hit_card = player.hit()  # take a hit
            print(f"Doubled Down! You were dealt the {card_to_text(hit_card)} ... your hand value is now {player.value()}")
            double_down = True  # set the double down variable to True to break the loop

    if player.value() > 21:  # if the player has over 21 (busted)
        print(f'You busted with {str(player.value())}')
        return wallet  # current value of wallet, with losses already reflected
    
    print(f'Dealer flips ... their hidden card is a {card_to_text(dealer.hand[1])}, yielding a dealer hand value of {dealer.value()}')
    dealer_play(dealer)  # dealer automatically hits until they hit soft/hard 17+ or bust

    if dealer.value() > 21:  # if the dealer busts
        print('Dealer Busted - You Win!')
        if double_down == True:
            wallet += (bet * 4)  # player gets 2x original and 2x in winnings
            return wallet
        else:
            wallet += (bet * 2)  # player gets original bet plus 1x in winnings
            return wallet
    elif dealer.value() > player.value():  # if the dealer beats the player's hand
        print('Dealer wins!')
        return wallet  # current value of wallet, with losses already reflected
    elif dealer.value() < player.value():  # if the player beats the dealer's hand,
        print('Player wins!')
        if double_down == True:
            wallet += (bet * 4)  # player gets 2x original bet plus 2x in winnings
            return wallet
        else:
            wallet += (bet * 2)  # player gets original bet plus 1x in winnings
            return wallet
    else:  # both player and dealer have hands of equal value
        print('Push - nobody wins!')
        if double_down == True:
            wallet += (bet * 2)  # player gets 2x original bet
            return wallet
        else:
            wallet += bet  # player gets original bet
            return wallet

def user_credentials() -> (str, str):
    '''
    Prompts user with message to input their username and password.

    Returns:
        username: a stripped version of the provided username
        password: a stripped version of the provided password
    '''

    username = input('Please enter your username: ')  # user inputs their username
    password = input('Please enter your password (case sensitive): ')  # user inputs their password

    username = username.strip()
    password = password.strip()

    return username, password

def user_login(username:str, password:str) -> list:
    '''
    References a provided username and password to access the user's account information, required to play Blackjack

    Arguments:
        username: the provided username
        password: the provided password
    
    Returns:
        account: the user's account information if username is found and password is correct
    '''

    try:
        
        with open('blackjack_account_log.txt', 'r') as file:  # trying to open the account log
            
            for line in file:  # for each line in the file

                account = line.split(',')  # split all the account information (comma seperated)

                if account[0] == username:  # if the username (in account line) matches the provided username

                    if account[1].strip() == password:  # if the user name and password match

                        return account  # return all the account information as a list
                
                    elif account[1].strip() != password:  # if the username matches but the password does not

                        print('Invalid password!')

                        return None
                
                else:

                    pass  # continue to the next account (line) in the file
                    
        print(f"We can't find an account under the provided username: {username} - please create an account to get started!")  # inidicate if there is no username found

        return None
    
    except FileNotFoundError:  # if the file can't be found, there is no user base

        print('No users found - please create a user account to get started!')

        return None

def user_already_exists(user:str) -> bool:
    '''
    Check's to see whether a username is already in existence.

    Arguments:
        user: a username
    
    Returns:
        True / False
    '''

    with open('blackjack_account_log.txt', 'r') as file:  # open the file

        for line in file:  # iterate through each line

            x = line.split(',')  # split up the account information (comma seperated)

            if x[0] == user:  # if the username exists, return True

                return True
            
def new_user():
    '''
    Creates a new user account. Requires unique username.
    '''

    user, pwd = user_credentials()  # get credentials

    try:  # if the file exists

        exists = False

        with open('blackjack_account_log.txt', 'r') as file:  # read the file
            
            if user_already_exists(user) == True:  # if the username already exists
                print('Username already in use - please specify a unique username!')
                exists = True

        if exists == False:  # if the username does not exist

            with open('blackjack_account_log.txt', 'a') as file: 

                file.write(f'{user},{pwd},0.00\n')  # append a new line with that account information
                print(f'Username: {user}')
                print(f'Password: {pwd}')
                print(f'Wallet: $0.00')

    except FileNotFoundError:  # if no user base established

        with open('blackjack_account_log.txt', 'w') as file:  # write a new line with the user's account information

            file.write(f'{user},{pwd},0.00\n')
            print(f'Username: {user}')
            print(f'Password: {pwd}')
            print(f'Wallet: $0.00')

def update_wallet(account):

    with open('blackjack_account_log.txt', 'r') as file: 

        lines = file.readlines() 
    
    found = False
    counter = 0

    while found == False and counter < len(lines):

        if lines[counter].split(',')[0] == account[0]:

            lines[counter] = f'{account[0]},{account[1]},{account[2]}\n'

            found = True
        
        counter += 1
    
    with open('blackjack_account_log.txt', 'w') as file: 

        file.writelines(lines)

def main():
    '''
    Main function of program. Launches game and provides user with menu of options.
    '''

    account = None  # this will be used retrieve / update account information while the user is logged in
    print('Welcome to Blackjack 1.0 !')

    while True:  # continual loop until broken, via 'QUIT'

        user_input = client_option_reader("What would you like to do (type 'Help' for more info)?: ", ('Create', 'Login', 'Play', 'Logout', 'Deposit', 'Balance', 'Quit', 'Help'))

        if user_input == 'Play':  # time to play blackjack

            if account == None:  # account is required, via 'Login'

                print('Login Required!')

                continue  # recycle through the loop

            wallet = float(account[2])  # if logged in, access / convert the user's wallet to numeric (dollars)

            if wallet < MINIMUM_BET:  # if the user does not have enough funds to play the minimum bet

                print('Please load funds to your wallet!')

                continue  # recycle through the loop

            play_again = True  # placeholder for when the user opts to stop playing (break's loop)
            inital_hand = True  # placeholder to denote when the inital hand is dealt

            print(f'Current wallet amount: ${wallet}')

            while wallet >= MINIMUM_BET and play_again == True:  # while the user's wallet can cover the minimum and they want to continue playing
                
                if inital_hand == False:  # if this is not the first hand dealt, ask the user if they want to continue playing

                    question = client_option_reader('Want to play another hand (Y/N)?: ', ('Y','N'))

                    if question == 'Y':  # if the answer is yes
                        
                        pass  # pass the game

                    else:  # if the answer is no

                        break  # breaking the loop

                else:
                    inital_hand = False  # if it is the initial hand, set to False for later hands

                new_wallet = play_game(wallet)  # play blackjack with the user's wallet amount

                if wallet > new_wallet:  # if the wallet amount before the game is greater than the wallet amount after the game
                    print(f'You Lost: ${str(abs(wallet - new_wallet))}')  # inform the user of their losses
                elif wallet < new_wallet:  # if the wallet amount before the game is less than the wallet amount after the game
                    print(f'You Won: ${str(abs(wallet - new_wallet))}')  # inform the user of their winnings

                print(f'Current wallet amount: ${new_wallet}')  # inform the user of their wallet balance, post game

                wallet = new_wallet  # update wallet to reflect the new wallet amount

            account[2] = str(wallet)  # when the Blackjack gameplay ends, update the user's account information with the newest wallet amount, reflecting their losses / winnings

            update_wallet(account)  # updating the user's wallet amount in account history log
        
        elif user_input == 'Login':

            if account != None:  # if a user is already logged in

                print(f'{account[0]} already logged in. Logout required!')

                continue  # recycle through the loop

            user, pwd = user_credentials()  # otherwise, obtain credentials

            account = user_login(user, pwd)  # retrieve their account information

            if account != None:  # if the user was successfully identified in the backend

                print(f'Welcome {user}, you are now logged in!')  # welcome them

        elif user_input == 'Logout':

            if account == None:  # if nobody is logged in

                print('Login Required!')

                continue  # recycle through the loop

            else:  # if someone is logged in

                print(f'Goodbye {account[0]}!')

                account = None  # set the account information to None
        
        elif user_input == 'Create':

            if account != None:

                print('Logout Required!')
                
                continue

            else:
                
                new_user()
        
        elif user_input == 'Balance':

            if account == None:  # if nobody is logged in

                print('Login Required!')

                continue  # recycle through the loop

            print(f'Your balance is ${account[2].strip()}')  # else, print the user's wallet balance

        elif user_input == 'Help':   # information about the commands

            pass

        elif user_input == 'Deposit':

            if account == None:  # if nobody is logged in

                print('Login Required!')
                
                continue  # recycle through the loop

            deposit = -1  # placeholder for deposit amount

            print(f'Your current wallet amount is ${account[2].strip()}')

            while deposit == -1:

                input_deposit = input('How much would you like to deposit?: ')

                if input_deposit.isdigit() == False:  # if the deposit is not an integer

                    print('Invalid amount - please try again!')

                    continue  # recycle through the deposit loop

                else:

                    deposit = float(input_deposit)  # take the valid deposit amount

            wallet = float(account[2])  # pull the current wallet amount
            wallet += deposit  # add the deposit
            account[2] = str(wallet)  # update the account information

            update_wallet(account)  # updating the user's wallet amount in account history log

            print(f'You sucessfully deposited ${deposit}, your wallet balance is ${wallet}')

        elif user_input == 'Quit':

            print('Thanks for playing!')

            break  # end the game

if __name__ == "__main__":

    main()