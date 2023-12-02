'''
Testing those functions / methods in blackjack.py that do not require input()

NAME: ADAM BRENNER
SEMESTER: FALL 2023
'''

# will test place_bet, client_option_reader, play_game, user_credentials, new_user, main with recorded test runs (see saved IO transcripts)
from blackjack import hand_calculator, dealer_play, card_to_text, user_login, user_already_exists, update_wallet, BlackjackHand
import sys, os

test_ledger_file = '/Users/adambrenner/Documents/CS 5001/Final Project/user_login_test.txt'  # account ledger file for testing

# found the following two functions here, as I was looking for a way to avoid print statements from called functions (https://stackoverflow.com/questions/8391411/how-to-block-calls-to-print#:~:text=If%20you%20don%27t%20want,the%20top%20of%20the%20file)

def blockPrint():
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    sys.stdout = sys.__stdout__

def test_hand_calculator() -> int:
    '''
    Tests hand calculator function

    Returns:
        failure_count: number of failed tests
    '''

    failure_count = 0

    if hand_calculator(['KH','10D','AC']) != 21:  # should be smart enough to read a hard ace value (1)

        failure_count += 1

    if hand_calculator(['2H','2H','AD','5C']) != 20:  # should be smart enough to read a soft ace value

        faulre_count += 1

    if hand_calculator(['JH','QD','QC']) != 30:

        failure_count += 1

    if hand_calculator(['AH','AC','AD']) != 13:  # should be smart enough to read one soft, two hard ace values

        failure_count += 1

    if hand_calculator(['AH','2D','3H','4S','5D','6C']) != 21:

        failure_count += 1

    return failure_count

def test_dealer_play() -> int:
    '''
    Tests dealer_play function

    Returns:
        failure_count: number of failed tests
    '''

    failure_count = 0
    counter = 0

    while counter < 100:  # simulating 100 hands

        hand = BlackjackHand()
        dealer_play(hand) 

        if hand_calculator(hand.hand[0:2]) >= 17 and len(hand.hand) > 2:  # if there inital hand is 17+, they should not finish with more than the two original cards they were dealt

            failure_count += 1

        elif hand.value() < 17 or hand.value() > 26:  # the range of values their final hand can be in, given the dynamic, soft 17 game play - their hand should not finish below 17 and should not exceed 26 (i.e., worst case, hitting on 16 and gettting a 10, as an ace would put them at 17)

            failure_count += 1
            
        counter += 1

    return failure_count

def test_card_to_text() -> int:
    '''
    Tests card_to_text function

    Returns:
        failure_count: number of failed tests
    '''

    failure_count = 0

    if card_to_text('QH') != 'Q of Hearts':

        failure_count += 1

    if card_to_text('KD') != 'K of Diamonds':

        failure_count += 1

    if card_to_text('5S') != '5 of Spades':

        failure_count += 1

    if card_to_text('AC') != 'A of Clubs':

        failure_count += 1

    return failure_count

def test_user_login() -> int:
    '''
    Tests user_login function

    Returns:
        failure_count: number of failed tests
    '''

    failure_count = 0

    account_info_1 = user_login('abren','123', test_ledger_file)

    if account_info_1 == None:  # should return the account info

        failure_count += 1

    elif type(account_info_1) != list:  # should be of type list

        failure_count += 1

    elif account_info_1[0] != 'abren':  # first element should be username

        failure_count += 1

    elif account_info_1[1] != '123':  # second element should be password

        failure_count += 1

    account_info_2 = user_login('abren','wrongpassword', test_ledger_file)  # wrong password should return no account info (you shall not PASS)

    if account_info_2 != None:

        failure_count += 1

    account_info_3 = user_login('fake_user','123', test_ledger_file)  # username does NOT exist, therefore nothing should be returned

    if account_info_3 != None:

        failure_count += 1

    account_info_4 = user_login('abren','123','fake_ledger.txt')  # ledger file DNE - should return nothing

    if account_info_4 != None:

        failure_count += 1

    return failure_count

def test_user_already_exists() -> int:
    '''
    Tests user_already_exists function

    Returns:
        failure_count: number of failed tests
    '''

    failure_count = 0

    if user_already_exists('abren', test_ledger_file) is not True:  # should be True that abren exists

        failure_count += 1

    if user_already_exists('fake', test_ledger_file) is True:  # fake does not exist

        failure_count += 1

    # if user_already_exists('abren', 'fake_ledger.txt') is True:  # not including, as this function is not referenced anywhere where the ledger file is not in existence

    #     failure_count += 1

    return failure_count

def test_update_wallet() -> int:
    '''
    Tests user_already_exists function

    Returns:
        failure_count: number of failed tests
    '''

    failure_count = 0

    with open(test_ledger_file,'r') as file:

        account = file.readlines()[0].split(',')  # find the current wallet value

    inital_wallet = float(account[2])

    account[2] = inital_wallet + 100  # add $100 to it

    update_wallet(account, test_ledger_file)  # update wallet function

    with open(test_ledger_file,'r') as file:  # re-pull from the account ledger

        new_wallet = float(file.readlines()[0].split(',')[2])

    if new_wallet - 100 != inital_wallet:  # the new wallet value in the ledger should be 100 more than the original wallet value

        failure_count += 1

    return failure_count

def main():
    '''
    Main driver of testing
    '''

    blockPrint()  # blocking prints

    hand_calculator_fails = test_hand_calculator()
    dealer_play_fails = test_dealer_play()
    card_to_text_fails = test_card_to_text()
    user_login_fails = test_user_login()
    user_already_exists_fails = test_user_already_exists()
    update_wallet_fails = test_update_wallet()

    enablePrint()  # enabling prints

    print('\nFunction Testing Results:\n')
    print(f'hand_calculator: {hand_calculator_fails} failed tests')
    print(f'dealer_play: {dealer_play_fails} failed tests')
    print(f'card_to_text: {card_to_text_fails} failed tests')
    print(f'user_login: {user_login_fails} failed tests')
    print(f'user_already_exists: {user_already_exists_fails} failed tests')
    print(f'update_wallet: {update_wallet_fails} failed tests\n')

if __name__ == '__main__':

    main()