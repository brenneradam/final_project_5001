"""
Blackjack 1.0

A program that allows users to create an account, load/save their wallet, and play blackjack.

NAME: ADAM BRENNER
SEMESTER: FALL 2023
"""

import random

MINIMUM_BET = 25
ACCOUNT_LEDGER = 'blackjack_account_log.txt'

MIN_BET_MSG = f'Place your bet (min. ${MINIMUM_BET}): '
BLACKJACK_DEALER_MSG = 'Blackjack - Dealer Wins :('
BLACKJACK_PLAYER_MSG = 'Blackjack - You Win!'
BLACKJACK_PUSH_MSG = 'Push - blackjack for everyone'
BLACKJACK_NOBODY_HOME_MSG = "Dealer checked for Blackjack ... Nobody's Home!"
INSURANCE_QUESTION_MSG = 'Would you like insurance on your hand (Y / N)?: '
INVALID_INPUT_MSG = 'Invalid Input: Please Try Again!'
INSUFFICIENT_FUNDS_MSG = 'Insufficient Funds: Please visit menu to deposit more funds.'
MIN_BET_ERROR_MSG = 'Minimum bet not satisfied: Please place a bet equal or greater than the table minimum.'
DEALER_BUST_MSG = 'Dealer Busted - You Win!'
DEALER_WINS_MSG = 'Dealer wins!'
PLAYER_WINS_MSG = 'Player wins!'
PUSH_MSG = 'Push - nobody wins!'
INVALID_PASSWORD_MSG = 'Invalid password!'
UNIQUE_USERNAME_VIOLATION_MSG = 'Username already in use - please specify a unique username!'
LOGIN_REQ_MSG = 'Login Required!'
LOGOUT_REQ_MSG = 'Logout Required!'
LOAD_FUNDS_MSG = 'Please load funds to your wallet!'
INVALID_DEPOSIT_MSG = 'Invalid amount - please try again!'
GOODBYE_MSG = 'Thanks for playing!'
WELCOME_MSG = 'Welcome to Blackjack 1.0 !'
NO_USERS_FOUND_MSG = 'Username not found - please create an account to get started!'
USERNAME_ENTRY_MSG = 'Please enter your username: '
PASSWORD_ENTRY_MSG = 'Please enter your password (case sensitive): '
ACCOUNT_CREATED_MSG = 'Your account has been successfully created!'
HELP_MSG = '''\nType any of the following options:\n
Create -> Setup your account by establishing a username and password.
Login -> You know the drill. Enter your username and password to access your wallet. (Hint: Required to Play)
Play -> Take a seat at the blackjack table. (Hint: Don't forget to load your wallet)
Logout -> Going so soon? We hope to see you again!
Deposit -> Loading your wallet. (Hint: Login Required)
Balance -> Curious to know how much you lost? Get a quick update on the balance of your wallet. (Hint: Login Required)
Quit -> End the program.\n'''

doc = ('AH', 'AD', 'AC', 'AS',
       'KH', 'KD', 'KC', 'KS',
       'QH', 'QD', 'QC', 'QS',
       'JH', 'JD', 'JC', 'JS',
       '10H', '10D', '10C', '10S',
       '9H', '9D', '9C', '9S',
       '8H', '8D', '8C', '8S',
       '7H', '7D', '7C', '7S',
       '6H', '6D', '6C', '6S',
       '5H', '5D', '5C', '5S',
       '4H', '4D', '4C', '4S',
       '3H', '3D', '3C', '3S',
       '2H', '2D', '2C', '2S')

doc_values = {'A': None,  # since A is variable
              'K': 10,
              'Q': 10,
              'J': 10,
              '10': 10,
              '9': 9,
              '8': 8,
              '7': 7,
              '6': 6,
              '5': 5,
              '4': 4,
              '3': 3,
              '2': 2}

suit_values = {'H': 'Hearts', 'D': 'Diamonds', 'C': 'Clubs', 'S': 'Spades'}


class BlackjackHand:
    '''
    Represents a hand of blackjack
    '''

    def __init__(self):
        '''
        Constructs a randomized 2-card hand.
        '''

        self.hand = [random.choice(doc), random.choice(doc)]

    def hit(self):
        '''
        Pulls a random card and adds it to the hand.

        Returns:
            self.hand[-1]: the randomly chosen card
        '''

        self.hand.append(random.choice(doc))

        return self.hand[-1]

    def value(self):
        '''
        Calculates the current value of the hand.

        Returns:
            hand_calculator(self.hand): the current value of the hand
        '''

        return hand_calculator(self.hand)


def place_bet(wallet_value: int) -> int:
    '''
    Prompts the user to place a bet; required to be equal or greater than minimum bet

    Arguments:
        wallet_value: the amount of money available in the user's account

    Returns:
        bet_amount: the amount of the money the user is wagering from their wallet
    '''

    bet_amount = input(MIN_BET_MSG)  # prompt the user to enter their bet

    if bet_amount.isdigit() == False:  # if the bet is not a whole number (will not not support cents on the dollar, as this is uncommon in most casinos)
        print(INVALID_INPUT_MSG)  # re-prompt
        return place_bet(wallet_value)

    bet_amount = float(bet_amount)  # convert the str to float

    if (wallet_value - bet_amount) < 0:  # if the bet can't be covered by the wallet amount
        print(INSUFFICIENT_FUNDS_MSG)  # re-prompt
        return place_bet(wallet_value)

    elif bet_amount < MINIMUM_BET:  # if the bet does not meet the minimum
        print(MIN_BET_ERROR_MSG)  # re-prompt
        return place_bet(wallet_value)

    return bet_amount


def hand_calculator(hand: list) -> int:
    '''
    Takes a hand of cards and calculates the value of the hand;
    Aces will default as high (11) until the hand value exceeds 21, in which case the ace value(s) will revert to low (1) automatically, where appl.

    Arguments:
        hand: list of cards that make up the blackjack hand - can be either player or dealer

    Returns:
        hand_value: the assessed value of the blackjack hand
    '''

    hand_value = 0
    ace_cnt = 0

    for card in hand:  # iterating through each card in hand

        if card[:-1] == 'A':  # if the card is an ace
            ace_cnt += 1  # count it and move on (will handle in the end)

        else:
            # for all non-ace cards, add the card value to the hand value
            hand_value += doc_values[card[:-1]]

    for ace in range(ace_cnt):  # for the number of aces counted

        if hand_value + \
                11 > 21:  # if the ace will put the hand over 21, count it as a hard ace (1)
            hand_value += 1
        else:  # otherwise, count it as a soft ace (11)
            hand_value += 11

    return hand_value


def dealer_play(hand: object) -> None:
    '''
    Automatic hitting for the dealer, based on soft 17 game play.

    Arguments:
        hand: a hand of blackjack
    '''

    while hand.value() < 17:  # dealer will stand on soft 17 or higher

        hit_card = hand.hit()  # hand hit

        print(
            f"Dealer was dealt the {card_to_text(hit_card)} ... their hand value is now {hand.value()}")


def card_to_text(card: str) -> str:
    '''
    Takes a card from the deck and represents it in a phrase

    Arguments:
        card: the card from a deck of cards, with value and suit

    Returns:
        return_str: the phrase representation of a card (i.e., 10H = 10 of Hearts)
    '''

    # phrase creation
    return_str = (card[:-1] + ' of ' + suit_values[card[-1]])

    return return_str


def client_option_reader(input_msg: str, options: tuple) -> str:
    '''
    Prompts the user with a message, and checks for valid, inputted commands

    Arguments:
        input_msg: phrase to be printed at the console
        options: the valid strings that the user can enter

    Returns:
        client: the valid option entered, from options
    '''

    client = input(input_msg)  # prompts the user with a message at the console

    client = client.strip()  # stripping any whitespace

    if client in options:  # if the stripped input exists within the options

        return client  # return that input

    else:

        # prompt the user that their input is not within the the set of
        # expected options
        print(INVALID_INPUT_MSG)

        # re-prompt them with the client_option_reader()
        return client_option_reader(input_msg, options)


def play_game(wallet) -> int:
    '''
    Replicates the player experience in a single game of blackjack.

    Arguments:
        wallet: the amount of funds a user has to spend at the blackjack table

    Returns:
        wallet: the user's updated wallet value, reflecting the winnings / losses from their single game of blackjack
    '''

    bet = place_bet(wallet)  # place your initial bet

    wallet -= bet  # subtracting the initial bet from the user's wallet value

    insurance = 0  # initializing insurance amount of zero

    player = BlackjackHand()  # creating a random hand for the player
    dealer = BlackjackHand()  # creating a random hand for the dealer

    print(
        f'Your hand is the {card_to_text(player.hand[0])}' +
        ' & ' +
        f'{card_to_text(player.hand[1])}, with a value of {str(player.value())}')

    print(f'Dealer showing {card_to_text(dealer.hand[0])}')

    if doc_values[dealer.hand[0][:-1]] == 10 or dealer.hand[0][:- \
        1] == 'A': # if the dealer shows a card worthy of checking for blackjack

        # if you can still afford the insurance price, we will ask if you would
        # like insurance
        if (wallet - (bet / 2)) >= 0:

            question = client_option_reader(
                INSURANCE_QUESTION_MSG, ('Y', 'N'))  # asking about insurance

            if question == 'Y':  # if the user prompts yes, they will be charged 50% of their initial bet
                insurance += (.5 * bet)  # funds applied to insurance
                wallet -= insurance  # insurance taken out of wallet

        if dealer.value() == 21 and player.value(
        ) != 21:  # if the dealer has blackjack and the user does NOT

            print(
                f'Dealer flips ... their hidden card is a {card_to_text(dealer.hand[1])}, yielding a dealer hand value of {dealer.value()}')
            print(BLACKJACK_DEALER_MSG)  # informing user of loss

            # user gets 3x their insurance bet (if any); this includes initial
            # insurance bet (1x) + 2:1 winnings (2x)
            wallet += (insurance * 3)

            return wallet

        elif dealer.value() == 21 and player.value() == 21:  # if both dealer and player have 21

            print(
                f'Dealer flips ... their hidden card is a {card_to_text(dealer.hand[1])}, yielding a dealer hand value of {dealer.value()}')
            print(BLACKJACK_PUSH_MSG)  # informing user of push

            # user gets their original bet back + 3x insurance (if any)
            wallet += (bet + (insurance * 3))

            return wallet

        else:  # if there is no scenario where the dealer has blackjack

            print(BLACKJACK_NOBODY_HOME_MSG)  # nobody is home!

    if player.value() == 21:  # if the player has blackjack and the dealer did NOT

        print(BLACKJACK_PLAYER_MSG)  # winner winner !
        wallet += (2.5 * bet)  # return the original bet and 1.5x that amount

        return wallet

    stay = False
    double_down = False

    while player.value() < 21 and stay == False and double_down == False:

        if len(player.hand) == 2 and (wallet - bet) >= 0:
            # if you still have your initially dealt hand and can afford another bet, you are presented with
            # a double down opportunity

            move = client_option_reader(
                'Would you like to Stay [S] / Hit [H] / Double Down [D]?: ', ('S', 'H', 'D'))

        else:

            move = client_option_reader(
                'Would you like to Stay [S] / Hit [H]?: ', ('S', 'H'))

        if move == 'H':  # if you are opting to hit
            hit_card = player.hit()  # the player's hand gets hit
            print(
                f"You were dealt the {card_to_text(hit_card)} ... your hand value is now {player.value()}")

        elif move == 'S':  # if you are staying, set the stay variable to True to break loop
            stay = True

        # if you are doubling down - no need to check if you can afford (done
        # above)
        elif move == 'D':
            wallet -= bet  # subtract an additional bet from the user's wallet
            hit_card = player.hit()  # take a hit
            print(
                f"Doubled Down! You were dealt the {card_to_text(hit_card)} ... your hand value is now {player.value()}")
            double_down = True  # set the double down variable to True to break loop

    if player.value() > 21:  # if the player has over 21 (busted)
        print(f'You busted with {str(player.value())}')
        return wallet  # current value of wallet, with losses already reflected

    print(
        f'Dealer flips ... their hidden card is a {card_to_text(dealer.hand[1])}, yielding a dealer hand value of {dealer.value()}')
    # dealer automatically hits until they hit soft/hard 17+ or bust
    dealer_play(dealer)

    if dealer.value() > 21:  # if the dealer busts
        print(DEALER_BUST_MSG)
        if double_down:
            wallet += (bet * 4)  # player gets 2x original and 2x in winnings
            return wallet
        else:
            wallet += (bet * 2)  # player gets original bet plus 1x in winnings
            return wallet
    elif dealer.value() > player.value():  # if the dealer beats the player's hand
        print(DEALER_WINS_MSG)
        return wallet  # current value of wallet, with losses already reflected
    elif dealer.value() < player.value():  # if the player beats the dealer's hand,
        print(PLAYER_WINS_MSG)
        if double_down:
            # player gets 2x original bet plus 2x in winnings
            wallet += (bet * 4)
            return wallet
        else:
            wallet += (bet * 2)  # player gets original bet plus 1x in winnings
            return wallet
    else:  # both player and dealer have hands of equal value
        print(PUSH_MSG)
        if double_down:
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

    # user inputs their username
    username = input(USERNAME_ENTRY_MSG)
    # user inputs their password
    password = input(PASSWORD_ENTRY_MSG)

    username = username.strip()
    password = password.strip()

    return username, password


def user_login(
        username: str,
        password: str,
        ledger: str = ACCOUNT_LEDGER) -> list:
    '''
    References a provided username and password to access the user's account information

    Arguments:
        username: the provided username
        password: the provided password

    Returns:
        account: the user's account information if username is found and password is correct
    '''

    try:

        with open(ledger, 'r') as file:  # trying to open the account ledger

            for line in file:  # for each line in the file

                # split all the account information (comma separated)
                account = line.split(',')

                # if the username (in account line) matches the provided
                # username
                if account[0] == username:

                    if account[1].strip(
                    ) == password:  # if the user name and password match

                        return account  # return all the account information as a list

                    # if the username matches but the password does not
                    elif account[1].strip() != password:

                        print(INVALID_PASSWORD_MSG)

                        return None

                else:

                    pass  # continue to the next account (line) in the file

        # indicate if there is no username found
        print(
            f"We can't find an account under the provided username: {username} - please create an account to get started!")

        return None

    except FileNotFoundError:  # if the file can't be found, there is no existing account ledger

        print(NO_USERS_FOUND_MSG)

        return None


def user_already_exists(user: str, ledger: str = ACCOUNT_LEDGER) -> bool:
    '''
    Checks to see whether a username is already in existence.

    Arguments:
        user: a username

    Returns:
        True: Whether the username already exists
    '''

    with open(ledger, 'r') as file:  # open the file

        for line in file:  # iterate through each line

            # split up the account information (comma separated)
            x = line.split(',')

            if x[0] == user:  # if the username exists, return True

                return True


def new_user():
    '''
    Creates a new user account. Requires unique username.
    '''

    user, pwd = user_credentials()  # get credentials
    # can't allow commas, or else it will disrupt reading / writing to account
    # info
    user = user.replace(',', '')
    # can't allow commas, or else it will disrupt reading / writing to account
    # info
    pwd = pwd.replace(',', '')

    account_info = f'{user},{pwd},0.00\n'

    try:  # if the ledger exists

        username_exists = False

        with open(ACCOUNT_LEDGER, 'r') as file:  # read the file

            if user_already_exists(user):  # if the username already exists
                print(UNIQUE_USERNAME_VIOLATION_MSG)
                username_exists = True

        if username_exists == False:  # if the username does not exist

            with open(ACCOUNT_LEDGER, 'a') as file:

                # append a new line with that account information
                file.write(account_info)
                print(ACCOUNT_CREATED_MSG)
                print(f'Username: {user}')
                print(f'Password: {pwd}')

            return account_info.split(',')

    except FileNotFoundError:  # if there is not an established ledger

        # write a new file with a new line to represent the user's account
        # information
        with open(ACCOUNT_LEDGER, 'w') as file:

            file.write(account_info)
            print(ACCOUNT_CREATED_MSG)
            print(f'Username: {user}')
            print(f'Password: {pwd}')

        return account_info.split(',')


def update_wallet(account: list, ledger: str = ACCOUNT_LEDGER):

    with open(ledger, 'r') as file:

        lines = file.readlines()  # read lines in file

    found = False
    counter = 0

    while found == False and counter < len(
            lines):  # while we haven't found the logged in account and have not exhausted all accounts

        if lines[counter].split(
                ',')[0] == account[0]:  # if we find the account

            # overwrite their account info with the most up-to-date account
            # information
            lines[counter] = f'{account[0]},{account[1]},{account[2]}\n'

            found = True  # mark found to kill loop

        counter += 1  # increment counter if not found

    # write new lines to file (likely need a better way to implement, instead
    # of reading all lines into memory)
    with open(ledger, 'w') as file:

        file.writelines(lines)


def main():
    '''
    Main driver of program. Launches game and provides user with menu of options.
    '''

    account = None  # this will be used to retrieve / update account information while the user is logged in
    print(WELCOME_MSG)

    while True:  # continual loop until broken, via 'QUIT'

        user_input = client_option_reader(
            "What would you like to do (type 'Help' for more info)?: ",
            ('Create',
             'Login',
             'Play',
             'Logout',
             'Deposit',
             'Balance',
             'Quit',
             'Help'))

        if user_input == 'Play':  # time to play blackjack

            if account is None:  # account is required, via 'Login'

                print(LOGIN_REQ_MSG)

                continue  # recycle through the loop

            # if logged in, access / convert the user's wallet to numeric
            # (dollars)
            wallet = float(account[2])

            if wallet < MINIMUM_BET:  # if the user does not have enough funds to play the minimum bet

                print(LOAD_FUNDS_MSG)

                continue  # recycle through the loop

            # placeholder for when the user opts to stop playing (break's loop)
            play_again = True
            initial_hand = True  # placeholder to denote when the initial hand is dealt

            print(f'Current wallet amount: ' + '${:,.2f}'.format(wallet))

            # while the user's wallet can cover the minimum and they want to
            # continue playing
            while wallet >= MINIMUM_BET and play_again:

                if initial_hand == False:  # if this is not the first hand dealt, ask the user if they want to continue playing

                    question = client_option_reader(
                        'Want to play another hand (Y/N)?: ', ('Y', 'N'))

                    if question == 'Y':  # if the answer is yes

                        pass  # continue playing

                    else:  # if the answer is no

                        break  # breaking the loop

                else:
                    initial_hand = False  # if it is the initial hand, set to False for later hands

                # play blackjack with the user's wallet amount
                new_wallet = play_game(wallet)

                if wallet > new_wallet:  # if the wallet amount before the game is greater than the wallet amount after the game

                    # inform the user of their losses
                    print(f'You Lost: ' +
                          '${:,.2f}'.format(abs(wallet - new_wallet)))

                elif wallet < new_wallet:  # if the wallet amount before the game is less than the wallet amount after the game

                    # inform the user of their winnings
                    print(f'You Won: ' +
                          '${:,.2f}'.format(abs(wallet - new_wallet)))

                # inform the user of their wallet balance, post game
                print(
                    f'Current wallet amount: ' +
                    '${:,.2f}'.format(new_wallet))

                wallet = new_wallet  # update wallet to reflect the new wallet amount

            # when the Blackjack game play ends, update the user's account
            # information with the newest wallet amount, reflecting their
            # losses / winnings from the session
            account[2] = str(wallet)

            # updating the user's wallet amount in account ledger
            update_wallet(account)

        elif user_input == 'Login':

            if account is not None:  # if a user is already logged in

                print(f'{account[0]} already logged in. Logout required!')

                continue  # recycle through the loop

            user, pwd = user_credentials()  # otherwise, obtain credentials

            # retrieve their account information
            account = user_login(user, pwd)

            if account is not None:  # if the user was successfully identified in the backend

                # welcome them
                print(f'Welcome {user}, you are now logged in!')

        elif user_input == 'Logout':

            if account is None:  # if nobody is logged in

                print(LOGIN_REQ_MSG)

                continue  # recycle through the loop

            else:  # if someone is logged in

                print(f'Goodbye {account[0]}!')

                account = None  # set the account information to None

        elif user_input == 'Create':

            if account is not None:

                print(LOGOUT_REQ_MSG)

                continue

            else:

                account = new_user()

        elif user_input == 'Balance':

            if account is None:  # if nobody is logged in

                print(LOGIN_REQ_MSG)

                continue  # recycle through the loop

            # else, print the user's wallet balance
            print(f'Your balance is ' + '${:,.2f}'.format(float(account[2])))

        elif user_input == 'Help':   # print information about the available commands

            print(HELP_MSG)

            continue

        elif user_input == 'Deposit':

            if account is None:  # if nobody is logged in

                print(LOGIN_REQ_MSG)

                continue  # recycle through the loop

            deposit = -1  # placeholder for deposit amount

            print(
                f'Your current wallet amount is ' +
                '${:,.2f}'.format(
                    float(
                        account[2])))

            while deposit == -1:

                input_deposit = input('How much would you like to deposit?: ')

                if input_deposit.isdigit() == False:  # if the deposit is not an integer

                    print(INVALID_DEPOSIT_MSG)

                    continue  # recycle through the deposit loop

                else:

                    # take the valid deposit amount
                    deposit = float(input_deposit)

            wallet = float(account[2])  # pull the current wallet amount
            wallet += deposit  # add the deposit
            account[2] = str(wallet)  # update the account information

            # updating the user's wallet amount in account history log
            update_wallet(account)

            print(
                f'You successfully deposited ' +
                '${:,.2f}'.format(deposit) +
                ', your wallet balance is ' +
                '${:,.2f}'.format(wallet))

        elif user_input == 'Quit':

            print(GOODBYE_MSG)

            break  # end the game


if __name__ == "__main__":

    main()
