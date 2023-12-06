# Final Project Report

* Student Name: Adam Brenner
* Github Username: brenneradam
* Semester: FALL 2023
* Course: CS 5001

## Description

This project is intended to simulate single-hand blackjack against a live dealer, and is inspired by the online casino experience. This is built as a console game, without any GUI.

I chose this as my project because I have always been a fan of Blackjack. More importantly, I once tried my hand (no pun intended) at building a python program, where the intention was to simulate / compare different blackjack strategies, to see which ones were more profitable. At the time, my python skills were lackluster, and so I wasn't able to get very far with the implementation.

Fast forward to today, where I feel more confident in my abilities to pick up where I left off. However, I thought it made more sense to focus this project's scope on replicating the experience of playing Blackjack in itself, as an initial way to prove my skills (considering the complexities associated with the game rules) - that, and I found the client-driven games we created during the semester to be fun and interesting, thereby making it the perfect idea.

## Key Features

### User Accounts

This program requires users to create their own account in order to gain access to the blackjack game play. One benefit to adopting this is that the program will continually track the progress (wins/losses/deposits) associated to a user's digital wallet, enabling the user's info to be saved after the program is terminated, giving way for the user's info to be easily recalled when the user starts a new session / logs in, in the future.

Usernames must be unique and are password protected. Users can easily log in / out using one of the accepted (respective) main() commands.

If you are a new user, it is very easy to create a new account using the correct main() command.

### Wallet Deposit

Once logged in, users can easily load their wallets by using the appropriate main() command and passing a whole, monetary value. Once accepted, this amount will then get instantly deposited into the users wallet. This functionality is very simple, and more so serves as a placeholder for a future payment transaction system, where users could (like a real online casino) enter their credit / debit / bank info to load their own REAL money into their digital wallet.

### Balance Checking

Gives users a quick way to check their wallet balance.

### Blackjack Game Play

The most important component of this program, where the user can put their own money on the table and play blackjack against a live dealer. Some of the interesting components of this feature include:

#### Traditional User Moves

Users have the ability to hit, stay, double down, and buy insurance (where appl.). This project does not support splitting (hence "single hand" blackjack), given the lack of a UI to simultaneously / seamlessly track multiple hands at a given time. In addition, surrendering is not supported, which was omitted due to its rarity as a blackjack move.

#### Auto Soft/Hard Ace Calculation

Hand value is contextually assessed using the optimal value for an ace (soft or hard), always giving the player the highest hand value possible without going over 21. In the case where a soft ace (11) will put the hand over 21, the hand value will automatically be re-calculated using the value of a hard ace (1).

#### Dealer Auto-Play

Once the player finishes their hand, the dealer will automatically play their hand until they hit soft/hard 17+.

#### Payout Tracking

Given the results of each hand (and the decisions that were made along the way), the program will inform the user how much money they won / lost, and will provide them with their updated wallet amount after each hand.

## Guide

When the program begins, you will be presented with a welcome message and a reserved line for user input.

```console
Welcome to Blackjack 1.0 !
What would you like to do (type 'Help' for more info)?:
```
The program will await your input, of which can be any of the accepted commands (run 'Help' for information on what commands are acceptable).

```console
What would you like to do (type 'Help' for more info)?: Help

Type any of the following options:

Create -> Setup your account by establishing a username and password.
Login -> You know the drill. Enter your username and password to access your wallet. (Hint: Required to Play)
Play -> Take a seat at the blackjack table. (Hint: Don't forget to load your wallet)
Logout -> Going so soon? We hope to see you again!
Deposit -> Loading your wallet. (Hint: Login Required)
Balance -> Curious to know how much you lost? Get a quick update on the balance of your wallet. (Hint: Login Required)
Quit -> End the program.
```

To play blackjack, a user account is required.  To create a user account, enter the 'Create' command and fill out the prompt.

```console
What would you like to do (type 'Help' for more info)?: Create

Please enter your username: newuser1
Please enter your password (case sensitive): thisgamerocks!

Your account has been successfully created!
Username: newuser1
Password: thisgamerocks!
```

Once created, your account will automatically log itself in. Now let's check your wallet balance.

```console
What would you like to do (type 'Help' for more info)?: Balance

Your balance is $0.00
```

Looks like you will need to deposit some $; to do that, enter the 'Deposit' command. Once prompted, enter the amount you'd like to deposit (must be a whole number, with no formatting).

```console
What would you like to do (type 'Help' for more info)?: Deposit

Your current wallet amount is $0.00
How much would you like to deposit?: 100

You successfully deposited $100.00, your wallet balance is $100.00
```

If we check your balance again ...

```console
What would you like to do (type 'Help' for more info)?: Balance

Your balance is $100.00
```

Great! Now you are ready to play. Go ahead and start your game, place your bet (look out for the posted bet minimum), and win some money!

```console
What would you like to do (type 'Help' for more info)?: Play

Current wallet amount: $100.00
Place your bet (min. $25): 25

Your hand is the J of Spades & 2 of Diamonds, with a value of 12
Dealer showing J of Spades
```

If the dealer is showing a card with a value of 10 or an A, you will be asked for insurance. In this example, we are not going to opt for insurance. Thankfully, they don't have blackjack!

```console
Would you like insurance on your hand (Y / N)?: N
Dealer checked for Blackjack ... Nobody's Home!
```

Now the user must choose to stay, hit, or double down. Let's play the hand out and see what happens. Once you finish your hand, the dealer will take care of the rest!

```console
Would you like to Stay [S] / Hit [H] / Double Down [D]?: H
You were dealt the 7 of Diamonds ... your hand value is now 19

Would you like to Stay [S] / Hit [H]?: S

Dealer flips ... their hidden card is a 2 of Spades, yielding a dealer hand value of 12
Dealer was dealt the 2 of Diamonds ... their hand value is now 14
Dealer was dealt the 5 of Spades ... their hand value is now 19

Push - nobody wins!
Current wallet amount: $100.00
```

Looks like a good old-fashioned push - once the hand finishes and our wallet amount is updated, we will be asked if we'd like to play another hand. If we opt to play another hand, another hand will begin. In this example, let's end the game play and return to the program menu.

```console
Want to play another hand (Y/N)?: N
```
To logout, enter the 'Logout' command. To then terminate the program, enter the 'Quit' command.

```console
What would you like to do (type 'Help' for more info)?: Logout
Goodbye newuser1!

What would you like to do (type 'Help' for more info)?: Quit
Thanks for playing!
```

## Installation Instructions

To run the program, execute the below at the command line.

```console
python3 ./blackjack.py
```

Currently, the only package that is being used is 'random', of which you should already have installed, via python's standard library.

## Code Review

As an alternative to manage the shuffling / reshuffling of card shoes, I opted to define a standard deck of 52 cards (via, tuple) and decided to enable a random draw from this tuple (with replacement) every time a new card is needed within the blackjack game play.

```python
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

doc_values = {'A': None,
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
```

You can see that the values of each card are stored in a dictionary. Notice how the ace has no value ... that's because an ace is a special card in the game of blackjack, as it can play as either a soft (11) or hard (1) value; in later functions, you will see how this ace gets handled.

To represent a hand of blackjack, I opted to build a class 'BlackjackHand', which has an attribute 'hand', representing the list of cards in the hand, and two functions; hit and value.

```python
class BlackjackHand:

   def __init__(self):

       self.hand = [random.choice(doc), random.choice(doc)]

   def hit(self):

       self.hand.append(random.choice(doc))

       return self.hand[-1]

   def value(self):

       return hand_calculator(self.hand)
```

When initializing a hand, the 'random' module is pulling a random 2-card draw from our standard 52 card deck. Likewise, every time a hit method is called, a random card is pulled and added to the hand (see more information on hand_calculator below in functions).

### Functions

#### Placing a bet

The place_bet() function takes the user's current wallet value as an argument and will request / validate how much a user is willing and able to bet (see line 115 -> blackjack.py). In the case where a user has $100 and the table minimum is $25 ...

```python
MINIMUM_BET = 25
place_bet(100)
```

The function will only allow the user to input a whole, monetary denomination that is >= $25 (since that is the table minimum) and <= $100 (since that is all they can afford). This function only accepts round numbers and will re-prompt if invalid input is provided.

#### Calculating Hand Value

Remember I said we would revisit the ace value conundrum! Dynamically calculating the value of a hand was also a feat in itself, as I needed an easy way to account for the hard / soft rule (see hand_calculator(), line 145 -> blackjack.py). It starts by taking a list of cards in the hand ...

```python
hand_value = 0
ace_cnt = 0

for card in hand:

   if card[:-1] == 'A':
       ace_cnt += 1:

   else:
       hand_value += doc_values[card[:-1]]
```

The hand is iterated through, separating the aces and accounting for all non-ace values. Only then, do we account for the aces ...

```python
for ace in range(ace_cnt):

   if hand_value + 11 > 21:
       hand_value += 1
   else:
       hand_value += 11
```

For each ace, if taking the soft value won't bust the hand, add the soft value to the current hand value and move to the next ace. If the ace will bust the hand, assume the hard value of 1 and move to the next ace. This function was added as a method to the BlackjackHand class, so that someone can take any hand (object) and immediately call the value of that hand.

#### Automatic Dealer Playing

I also needed a way for the dealer to automatically play their own hand ...

```python
while hand.value() < 17:
   hit_card = hand.hit()
```

The solution: force the dealer to continually hit their hand until they reach a soft (or hard) value of 17 or above.

#### Blackjack Game Play

This function will replicate an entire single hand of blackjack from start to finish. Once a bet is placed and deducted from the user's wallet, two hands are initiated; one for the dealer and one for the player.

```python
player = BlackjackHand()
dealer = BlackjackHand()
```
Importantly, every transaction is immediately applied / deducted from the user's wallet as decisions are made. This is important when deciding how much money to pay back the user, once their hand is over and based on what decisions they made throughout the game.

We must check if the dealer has a high card, for the purpose of offering insurance (only if the user can afford the insurance premium) ...

```python
if doc_values[dealer.hand[0][:-1]] == 10 or dealer.hand[0][:-1] == 'A':
      
       if (wallet - (bet / 2)) >= 0:

           question = client_option_reader(
               INSURANCE_QUESTION_MSG, ('Y', 'N'))
```

The next steps entail checking everyone's hand for blackjack, and either paying out the user or concluding the game (or in some cases, both).

Assuming the player made it through the initial checks, they will then be prompted to make decisions regarding their hand, until they choose to double down (appl. only on first move), hit, stay, or reach 21+.

```python
stay = False
double_down = False

while player.value() < 21 and stay == False and double_down == False:
```

The input options ...

```python
if move == 'H':
   hit_card = player.hit()

elif move == 'S':
   stay = True

elif move == 'D':
   wallet -= bet
   hit_card = player.hit()
   double_down = True
```

In the case that the player busts, the game will end. Otherwise, we go to the showdown and make payouts accordingly, based on the decisions the user made throughout the game. All winnings (if any) are reapplied to the user's wallet (including principal), and the wallet amount is returned.

#### Account System

The account system is built utilizing three data elements (username, password, wallet value) that are comma separated and stored as a line in a text file. To create an account, a user will input some phrase that will denote their account and (separately) password, to protect their account. It's important to note that any commas are removed from what the user inputs, as it will make parsing the account information difficult.

```python
user, pwd = user_credentials()
user = user.replace(',', '')
pwd = pwd.replace(',', '')
```

Assuming the username is not already in use (see user_already_exists(), line 456 -> blackjack.py), a new line will be added to the account ledger (.txt) file. If that file does not yet exist, a new file will be created with the user's account information.

To login, a user will enter their username and password, of which will get iteratively searched for in the account ledger (.txt) file. If found (and credentials are matching), the user's info will be returned, including the current value of their wallet.

As the user deposits money and/or incurs winnings or losses from their game play, we will need to update their wallet value in the account ledger. To do that, we will take their username to find their line of account information, and overwrite their wallet value, via overwriting the .txt file with their new wallet amount (see update_wallet(), line 530 -> blackjack.py).

#### Main Driver

The driver function of the program presents the user with a menu of options, all of which have different functionality.

```python
while True:

   user_input = client_option_reader(
       "What would you like to do (type 'Help' for more info)?: ",
       (   'Create',
           'Login',
           'Play',
           'Logout',
           'Deposit',
           'Balance',
           'Help',
           'Quit'))
```

A user can create an account, login to their existing account, play blackjack, logout of their account, deposit (fake) money into their account, obtain the balance of their account, ask for help on what their options are, or quit the program entirely (required to end the loop). Once a command is inputted, an if/elif statement is used to identify the right command and execute the proper functionality.

One important thing about this is that there is a variable, 'account' that is used to store the user's account info. If nobody is logged in, then the value of the account will default to None. Otherwise, a user's account information will be stored here, as a list. This variable is used throughout most of the menu commands, as it is imperative to know who is logged in when performing almost all functionality.

### Major Challenges

Some major challenges I had when doing this project were as follows:

* Although I decided to leave hand splitting out of scope (due to the difficulty of tracking multiple hands in a console game), that was not the original idea. In fact, I spent a lot of time trying to think about the solution for solving hand splitting; this came after I had a good chunk of the code base built out (and specifically, with the play game function). In all transparency, I was unable to think of the right way of implementing. I convinced myself that splitting is a naturally recursive problem, especially since someone can split multiple times in a single game (if they are lucky enough) AND since the rules of the game apply identically to each sub-hand. While I still don't think I cracked the code, I think part of the problem was how I designed the play_game function, as it should probably be abstracted a bit, since not all parts would apply to a sub hand (ex. the dealer checking for blackjack). However, even then, I found it to be awfully difficult (and confusing) on how to manage / present decisions to the user in a clear way WITHOUT a GUI.

* I repeatedly went back and forth about how the code would be designed. Primarily, I wanted to focus on writing a program that was client driven, based on what the user inputs. However, I still have future ambitions to simulate different strategies, to test out which are more profitable than others. The debacle I kept running into is that I was not leaving much of a backdoor for me to repurpose this code for that secondary application. Importantly, nearly every function has input() and print() built into it, in addition to there being no way for someone to pass some kind of decision logic besides user-input decisions. I kept thinking to myself that if I designed it right, both applications would be easy to implement, but it really wasn't clear to me how I could accomplish that. Looking back, I probably could have benefited from taking more time to plan if I really wanted to perfect the abstracted design approach that supports multiple decision making implementations.

Some things I am very proud of:

* Dynamically calculating the hand value, as this was something I struggled with when I tried my hand at building that python script a long time ago. It's really encouraging to see that I have the aces dynamically adjusting in value, based on how the hand is played out.
* The integrated account management system. I thought that would be a really interesting challenge to add. Glad to see it is working with the current implementation.

## Example Runs

I would suggest watching the linked video called main.mov (visit https://northeastern-my.sharepoint.com/:f:/g/personal/brenner_a_northeastern_edu/El0-eZ3hlEVMhMCRab-6oe4BMJ18axY6wTg0gipSIXIxJA), where I spend some time navigating through the entire program, as if I was a user. Here, I generally follow the steps laid out in the guide (above), in addition to playing a few hands of blackjack and making sure that the results of the hand are as expected (spoiler - everything looks as expected).

You can find the output from this session in main.txt (see test_logs in git repo); towards the bottom of main.txt, you will also find more output from another testing session that I conducted offline.

## Testing

I tested the code in two ways:

1. Writing units tests for those functions that did not require user input. Please see blackjack_test.py, of which (in some areas) makes use of the provided user_login_test.txt file.
2. Recording a series of videos where I voiced over the testing of each input-driven function; the output is provided in the submission (see test_logs folder in git repo).

See the following videos here (I suggest downloading them for clear resolution): https://northeastern-my.sharepoint.com/:f:/g/personal/brenner_a_northeastern_edu/El0-eZ3hlEVMhMCRab-6oe4BMJ18axY6wTg0gipSIXIxJA

Please reach out to me if you have any trouble gaining access / downloading from the linked onedrive folder.

## Missing Features / What's Next

Below are some of the things I would like to explore, given more time to work on this project:

* Create a GUI so that the game is more visually appealing, instead of having to keep up with a bunch of printed statements to figure out what is going on. This would of course open the door for easier hand splitting for the user.
* Solving the right way for implementing hand splitting.
* Integrate a better method of storing account information than just comma-separated values in a text file. This option was chosen because it was learned throughout the semester, and so I thought it was appropriate to make use of / convey my understanding of this approach. That said, I imagine it would make sense to create a database and read/write to this database when accounts are either created / needed to be fetched. I believe this would make for a more streamlined approach, not to mention making it easier to obtain account information in other scripts / environments.
* Store game play history, so that users can see what hands they've played, how they played them, and other metadata elements surrounding the result.
* Refactor / add functionality to simulate game play based on different strategies
* Create an actual paywall within the 'Deposit' area, so that users can really load their own wallets (would be cool, but probably illegal). Also - would want a function to withdraw your winnings (if any).
* AI generated hints when playing, in case the user is unsure

## Final Reflection

Overall, I found this course to be a helpful refresher on the core python competencies that I learned in my previous studies. In light of this, I'd rather take this opportunity to focus on the things I learned for the first time / high level takeaways (post-midterm)! 

For starters, this class finally gave me the confidence in my understanding of what classes and objects are. This whole time, I was convinced they were some mysterious phenomena ... and to find out that all the data structures I knew / used / understood were really objects in disguise, built from classes ... it honestly makes me laugh now. Another interesting concept we covered - that was new to me - were stacks and queues; I've always been aware of the LIFO and FIFO methodologies, but more from the lens of inventory accounting. Therefore, I found these concepts very easy to wrap my head around, and had an easy time comprehending it's implementation as an ADT (via, Class). I've yet to cover the final module (as I write this) but I imagine there will be some new, unearthed topics there for me to learn for the first time. Additionally, recursion was new for me, and in some cases a bit challenging (I personally thought it was the hardest homework assignment, as it required the most thought / time, compared to other assignments). Error handling was not new to me, but I definitely feel more comfortable with try/except blocks - I also never knew you could raise your own errors!

Importantly, I think back to the initial residency in Boston, and remember the phrase "Divide, Glue, Conquer". Having gone through this experience, I now see the importance of doing so when faced with large problems at hand. This project alone was challenging (and I'm already sure that I could have done a better job of applying this principle), so I can only imagine how increasingly complicated problems can become in the field and how increasingly important it is to not deviate from this mantra. Lastly, I think it's been really interesting to start considering the efficiencies of programs and to compare different algorithms that ultimately solve the same problem differently. Up until now, I've had a tendency to just program the first design that comes to mind ... I now see why that might not always be the best idea!

If there is one thing I'd like to learn more of (in reference to what was covered in this course), I feel as though my recall on object methods is really poor. For example, the amount of times I had to look up methods for string manipulation (because I forgot what exists or that I knew the operation I wanted but couldn't remember the name / arguments) was overbearing. I imagine the answer is 'it comes with practice', but in all honesty, that was one of the more frustrating parts of this semester.

Nonetheless, thank you to all of the TAs for their efforts throughout the semester, and to Prof. Lionelle for bringing us all together for this experience.

Adam