# Meeting Template

Go through this template in preparation for your meeting with the course staff member. We are not grading you on this template, just will help with questions and discussion. Please note, staff have the right to ask you to schedule a second meeting. The goal is to help you flesh out a reasonable project for this course, so make sure to use these meetings as a resource!

## Project Ideas
What are some ideas for your project? Why does that interest you?

Blackjack simulator. This is of interest because (1) it is my go-to casino game, (2) I know it very well, (3) I think it will be a doable challenge, given its nuanced rules / game design, and (4) I was interested a while back in doing this, mainly to simulate different strategies and to analyze which would prevail as the most profitable strategy (out of scope for what I am proposing).

## What are the big ideas?
How does this address some of the big learning ideas of 5001?

Here are some of the key components of this project and how they will tie back to learned areas:

(1) Having a menu to start from with different options - this incorporates parsing user options to navigate the application AND looping or recursive functionality until the user prompts to quit. 

(2) Allowing the user to "buy" chips - one thing I'd like this application to do is to keep record of a player's wallet (read/write to files). This entails that upon entering the application, the user must establish crendentials, which will be used to associate their wallet value.

(3) Allow the user to play blackjack - this entails shuffling 6 decks of cards, some of which have non-numeric labels (will use dictionary to tie back to values of "keys"). This also entails conditionals, for detecting whether the user busts, if the dealer reaches their limit/busts, if an Ace can be played High / Low, if a split opportunity arises,  i a player gets blackjack, etc.

(4) Allow the user to specify how much to bet, whether to hit / stand, split, double down, surrender

(5) Ensure the dealer is programmed sufficently, so that they are abiding by all game rules and are paying out the user in a fair manner

Assumptions

- Everytime a user launches the game, six new decks of cards (i.e., shoe) will be shuffled; the cards will be cut at random (i.e., this is the yellow card that signifies when the shoe needs to be replaced, as to not let the deck fully complete).  When the yellow card is reached, the active hand will be the last hand, followed by a reshuffle.

- When reshuffling occurs, the user will be asked if they'd like to play again.

- If the user wishes to leave the game while in progress, they will have to write LEAVE GAME when prompted for their next decision. Any hand currently being played will be voided (this, as opposed to asking if they want to play again after every hand).

- If a user runs out of chips, they will be informed and removed back to the main menu, of which will be the place to buy more chips.

## Code Design Thoughts
Are you including classes or APIs, what about dictionaries? One of the worst things you can do is go into a project assuming you are going to 'hard' code everything (this happens often with text based games, then students get stuck). You don't have to know details yet, but you should think about separation of concerns, and how to divide up your code. 

## Resources Found
What are some resources you have found already or already have access to? (APIs, libraries, past assignments, etc)

## Timeline
Setup a general timeline that includes research and development, and when you want to have certain aspects of the project done. 

11/13 - brainstorm design / necessary functions
11/20 - have functions implemented
11/27 - integration of functions to develop main program
12/4 - have program running and tested
12/7 - have program documented 