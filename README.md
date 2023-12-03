# Final Project Report

* Student Name: Adam Brenner
* Github Username: brenneradam
* Semester: FALL 2023
* Course: CS 5001

## Description

This project is intended to simulate single-hand blackjack against a live dealer, and is inspired by the online casino experience. This is built as a console game, without any GUI.

I chose this as my project because I have always been a fan of Blackjack. More importantly, I once tried my hand (no pun intended) at building a python program, where the intention was to simulate / compare different blackjack strategies, to see which ones were more profitiable. At the time, my python skills were lackluster, and so I wasn't able to get very far with the implementation. 

Fast forward to today, where I feel more confident in my abilities to pick up where I left of. However, I thought it made more sense to focus this project's scope on replicating the experience of playing Blackjack in itself, as an initial way to prove my skills (considering the complexities associated with the game rules) - that, and I found the client-driven games we created during the semester to be fun and interesting, therby making it the perfect idea.

## Key Features

### User Accounts

This program requires users to create their own account in order to gain access to the blackjack gameplay. One benfeit to adopting this is that the program will continually track the progress (wins/losses/deposits) associated to a user's digital wallet, enabling the user's info to be saved after the program is terminated, giving way for the user's info to be easily recalled when the user starts a new session / logs in, in the future. 

Usernames must be unique and are password protected. User can easily log in / out using one of the accepted (respective) main() commands.

If you are a new user, it is very easy to create a new account using the correct main() command.

### Wallet Deposit

Once logged in, users can easily load their wallets by using the appropriate main() command and passing a whole, monetary value. Once accepted, this amount will then get instantly deposited into the users wallet. This functionality is very simple, and more so serves as a placeholder for a future payment transaction system, where users could (like a real online casino) enter their credit / debit / bank info to load their own REAL money into their digital wallet.

### Balance Checking

Gives users a quick way to check their wallet balance.

### Blackjack Gameplay

The most important (and time-consuming) piece of this project, where the user can put their own money on the table and play blackjack against a live dealer. Some of the interesting components of this feature include:

#### Traditional Users Moves

Users have the ability to hit, stay, double down, and buy insurance (where appl.). This project does not support splitting (hence "single hand" blackjack), given the lack of a UI to simultaneously / seamlessly track multiple hands at a given time, in addition to not supporting surrendering, which was ommited due to its rareity.

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

Your account has been sucessfully created!
Username: newuser1
Password: thisgamerocks!
```

No need to login - you already are once your account is created. Now lets check your wallet balance.

```console
What would you like to do (type 'Help' for more info)?: Balance

Your balance is $0.00
```

Looks like you will need to deposit some $; to do that, enter the 'Deposit' command. Once prompted, enter the amount you'd like to deposit (must be a whole number, with no formatting).

```console
What would you like to do (type 'Help' for more info)?: Deposit

Your current wallet amount is $0.00
How much would you like to deposit?: 100

You sucessfully deposited $100.00, your wallet balance is $100.00
```

If we check your balance again ...

```console
What would you like to do (type 'Help' for more info)?: Balance

Your balance is $100.00
```

Great! Now you are ready to play. Go ahead and start you game, place your bet (look out for the posted minimum), and win some money!

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

Now the user must choose to stay, hit, or double down. Lets play the hand out and see what happens. Once you finish your hand, the dealer will take care of the rest!

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

Looks like a good old-fashioned push - once the hand finishes and our wallet amount is updated, we will be asked if we'd like to play another hand. If we opt to play another hand, another hand will begin. In this example, lets end the gameplay and return to the program menu.

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
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did. 

### Major Challenges

Some major challenges I had when doing this project were as follows:

* Although I decided to leave hand splitting out of scope (due to the difficulty of tracking multiple hands in a console game), that was not the original idea. In fact, I spent a lot of time trying to think about the solution for solving hand splitting; this came after I had a good chunk of the code base built out (and specifically, with the play game function). In all transparency, I was unable to think of the right way of implementing. I convinced myself that splitting is a naturally recursive problem, especially since someone can split multiple times in a single game (if they are lucky enough) AND since the rules of the game apply identically to each sub-hand. While I still don't think I cracked the code, I think part of the problem was how I designed the play_game function, as it should probably be abstracted a bit, since not all parts would apply to a sub hand (ex. the dealer checking for blackjack). However, even then, I found it to be awfully difficult (and confusing) on how to manage / present decisions to the user in a clear way WITHOUT a GUI.
* I repeatedly went back and forth about how the code would be designed. Primarily, I wanted to focus on writing a program that was client driven, based on what the user inputs. However, I still have future ambitions to simulate different strategies, to test out which are more profitable than others. The debacle I kept running myself into is that I was not leaving much of a backdoor for me to repurpose this code for that secondary application. Importantly, nearly every function has input() and print() built into it, in addition to there being no way for someone to pass some kind of decision logic besides user-input decisions. I kept thinking to myself that if I designed it right, both applications would be easy to implement, but it really wasn't clear to me how I could accomplish that. Looking back, I probably could have benefited from taking more time to plan if I really wanted to perfect the abstracted design approach that supports multiple decision making implementations.

Some things I am very proud of:

* Dynamically calculating the hand value, as this was something I struggled with when I tried my hand at building that python script a long time ago. It's really awesome to see the aces dynamically adjust in value, based on how the hand is played out.
* The integrated account management system. I thought that would be a really interesting challenge to add it is working out as intended.

## Example Runs

I would suggest watching the linked video called main.mov (visit https://northeastern-my.sharepoint.com/:f:/g/personal/brenner_a_northeastern_edu/El0-eZ3hlEVMhMCRab-6oe4BMJ18axY6wTg0gipSIXIxJA), where I spend some time navigating through the entire program, as if I was a user. Here, I generally follow the steps laid out in the guide (above), in addition to playing a few hands of blackjack and making sure that the results of the hand are as expected (spoiler - everything looks as expected). 

You can find the outut from this session in main.txt (see test_logs in git repo); towards the bottom of main.txt, you will also find more output from another testing session that I conducted offline.

## Testing

I tested the code in two ways: 

1. Writing units tests for those functions that did not require user input. Please see blackjack_test.py, of which (in some areas) makes use of the provided user_login_test.txt file.
2. Recording a series of videos where I voiced over the testing of each input-driven function; the output is provided in the submission (see test_logs folder in git repo). 

See the following videos here (I suggest downloading them for clear resolution): https://northeastern-my.sharepoint.com/:f:/g/personal/brenner_a_northeastern_edu/El0-eZ3hlEVMhMCRab-6oe4BMJ18axY6wTg0gipSIXIxJA

Please reach out to me if you have any trouble gaining access / downloading from the linked onedrive folder.

## Missing Features / What's Next

Below are some of the things I would like to explore, given more time to work on this project:

* Create a GUI so that the game is more visually appealing, instead of having to keep up with a bunch of printed statements to figure out what is going on. This would of course open the door for easier hand splitting for the user.
* Integrate a better method of storing account information than just comma-seperated values in a text file. This option was chosen because it was learned throughout the semester, and so I thought it was appropriate to make use / convery my understanding of this approach. That said, I imagine it would make sense to create a database and read/write to this database when accounts are either created / needed to be fetched. I believe this would make for a more streamlined approach, not to mention making it easier to obtain account information in other scripts / environments.
* Store gameplay history, so that user's can see what hands they've played, how they played them, and other metadata elements surrounding the result.
* Refactor / add functionality to simulate gameplay based on different strategies
* Create an actual paywall within the 'Deposit' area, so that users can really load their own wallets (would be cool, but probably illegal). Also - would want a function to withdrawl your winnings (if any).
* AI generated hints when playing, in case the user is unsure

## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.