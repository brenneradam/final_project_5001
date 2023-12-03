# Final Project Report

* Student Name: Adam Brenner
* Github Username: brenneradam
* Semester: FALL 2023
* Course: CS 5001



## Description
General overview of the project, what you did, why you did it, etc.

This project is intended to simulate single-hand blackjack against a live dealer, and is inspired by the online casino experience. This is built as a console game, without any GUI.

I chose this as my project because I have always been a fan of Blackjack. More importantly, I once tried my hand (no pun intended) at building a python program, where the intention was to simulate / compare different blackjack strategies, to see which ones were more profitiable. At the time, my python skills were lackluster, and so I wasn't able to get very far with the implementation. 

Fast forward to today, where I feel more confident in my abilities to pick up where I left of. However, I thought it made more sense to focus this project's scope on replicating the experience of playing Blackjack in itself, as an initial way to prove my skills (considering the complexities associated with the game rules) - that, and I found the client-driven games we created during the semester to be fun and interesting, therby making it the perfect idea.

## Key Features
Highlight some key features of this project that you want to show off/talk about/focus on. 

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

To run the project, you will need to execute blackjack.py at the command line; once executed, the program will appear at the console, awaiting your input, of which can be any of the accepted commands (run 'Help' for information on what commands are acceptable).

## Installation Instructions
If we wanted to run this project locally, what would we need to do?  If we need to get API key's include that information, and also command line startup commands to execute the project. If you have a lot of dependencies, you can also include a requirements.txt file, but make sure to include that we need to run `pip install -r requirements.txt` or something similar.

## Code Review
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did. 

```python
s = "Python syntax highlighting"
print s
```

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