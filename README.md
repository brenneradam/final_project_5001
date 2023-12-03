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
How do we run your project? What should we do to see it in action? - Note this isn't installing, this is actual use of the project.. If it is a website, you can point towards the gui, use screenshots, etc talking about features. 

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

If the dealer is showing a 10 or A, you will be asked for insurance. In this example, we are not going to opt for insurance. Thankfully, they don't have blackjack!

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

Looks like a good old-fashioned push - once the hand finishes and our wallet amount is updated, we will be asked if we'd like to play another hand. If we opt to play another hand 'Y', another hand will begin. In this example, lets end the gameplay and return to the program menu.

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
If we wanted to run this project locally, what would we need to do?  If we need to get API key's include that information, and also command line startup commands to execute the project. If you have a lot of dependencies, you can also include a requirements.txt file, but make sure to include that we need to run `pip install -r requirements.txt` or something similar.

To run the program, execute the below at the command line.

```console
python3 ./blackjack.py 
```

Currently, the only package that is being used in this script is random, of which should already be included in python's standard library.

## Code Review
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did. 

### Major Challenges
Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.


## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

## Testing
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 

> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_


## Missing Features / What's Next
Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future. 

## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.