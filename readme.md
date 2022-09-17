# JBA Project - Hangman

## bugs?
It seems to have an error with the letter 'v', so I had to create an exception for this letter.

## stage 1: Hello, Hangman
Hangman is a popular, funny, yet very grim game. A cruel computer hides a word from you and you need to guess it, letter by letter. If you fail, you'll be hanged, if you win, you'll survive.

You're probably familiar with the rules; now you can create this game yourself!

Let's take a brief look at what you are going to build in this project. Here is what the gameplay will look like:

    In the main menu, players can choose to either play or exit the game;
    If players choose to play, the computer picks a word from a list — it will be the answer;
    The computer asks players to enter a letter that may or may not be in the word;
    If players suggest a letter that does not appear in the word for the first time, It's a miss. A player can miss 8 times before the game is over;
    If the letter does occur in the word, the computer notifies the players. If there are letters left to guess, the computer invites the player to go on;
    When the entire word is uncovered — it's a victory! The game should calculate the final score and return to the main menu.

This may sound complex, but the project is split into small stages with the hints that will guide you. We guarantee that the final product is replayable and quite engaging!

Let's start with an announcement that will greet the player. You already know how to print with Python. Apply that knowledge to entice your friends to play with an announcement for your game!

## stage 2: Let's play a game
In this stage, we will add some simple gameplay. There will be two possible outcomes. Let's first print a welcoming message and then ask players to guess the word we have set for the game. If they guess the word, the game reports a win; otherwise, it will "hang" the player.

## stage 3: Make your choice
If there is only one word, the game becomes dull. You already know the word, and there’s no challenge. In this stage, let's make the game more difficult by choosing a word from the special list with a variety of options. This way, our game gains in replayability.

## stage 4: Help is on the way
The game is now more difficult to beat; your chances of guessing the word depend on the list size. If there are four words in the list, you have a 25% chance. Let's show a little mercy and add hints for our players.

## stage 5: Keep trying
Let's make the game iterative. In this stage, we'll adjust our game to resemble the classic version of Hangman. Players should now guess the letters in a word instead of inputting an entire word. If an attempt is successful, uncover the letter. We also need to add the lose condition — players have eight attempts to guess all letters that appear in the word. When players run out of attempts, the game ends.

Don't forget to get rid of the hints: replace all the letters in a word with hyphens at the beginning. Players input one lowercase letter at a time, so there is no need to worry about that.

Later on, we will also determine the win conditions, but in this stage, let's just see how well our player guesses the word on each attempt.

## stage 6: So far, our game has been some kind of a draft; we still lack a way to handle the player's victory. The player has only eight attempts, and the number of remaining attempts decreases every turn, even if players guess them correctly.
In this stage, we will start reducing the attempts only after players make a mistake. They can be mistaken eight times: attempts are reduced if the suggested letter is not in the word or if it has already been suggested before (no matter whether it's been a correct one or not). If a player has guessed all the letters, they win. If a player has some attempts after guessing the word, discard them, notify the player, and terminate the game.

## stage 7: Error
The skeleton of the game is ready; let's put some more gameplay meat on it.

In the previous stage, if players entered the same letter twice or more, the program reduced the number of remaining attempts regardless of whether this was a correct letter or not. This doesn’t seem fair, right? Players gain nothing, and the number of attempts gets smaller. Let's fix it!

## stage 8: Menu, please
In this stage, let's add a little more flavor to the game by constructing a menu to restart the program after the current session ends.