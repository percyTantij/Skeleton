"""
Welcome to the Python skeleton file for the 2023 CS113/114 project, Air-Race!

This skeleton is designed to provide you with a starting point for your project. Below is a brief explanation of how to use the skeleton. For more information, please refer to the [specification on the project website](https://www.cs.sun.ac.za/courses/cs114/).

At first, the skeleton might seem slightly overwhelming. There is a lot of text, the majority of which is documentation that explains some aspect of the project. Do not let this intimidate you. The skeleton is designed to help you. It is not designed to make your life more difficult. If you are confused about something, please ask us. We are here to help you. The project team's contact details are available on the project website. However, we encourage you to ask questions on the project's MS Teams channel. This way, other students can benefit from the answers as well.

We have included a few functions that you may find useful during the development of your project. In some cases, the functions are incomplete or do not work as intended. You must complete these functions or at least implement the functionality they represent as you see fit. You are not required to use all of the functions provided in this skeleton. So, unless we explicitly ask you to use a function, you may modify or delete them. Similarly, some of the code provided in the skeleton must be used exactly as it is given. Therefore, please make sure that you do not remove or rewrite the parts of the skeleton that must remain unaltered. Doing so may cause your program to behave in unexpected ways. Use the comments provided in the skeleton to help you understand what you are allowed to change and what you are not allowed to change.

The skeleton functions are highly documented, often providing helpful hints on how you can implement something. Keep an eye out for comments that start with `TODO`. These are comments that indicate that you must do something. They are usually placed in places where you must add code. You may also find comments that start with `NOTE`. These are comments that provide additional information about something.

Before submitting your project, please remember to rename your file to `SUxxxxxxxx.py`, where `xxxxxxxx` is your student number. This is important because we will use your student number to identify your submission. If you do not rename your file, we will not be able to mark your submission.

The skeleton is divided into sevral parts:
    - Imports:
        Here, we import the required packages such as stdio.
    - Constants:
        Constant variables are variables whose values do not change during the execution of the program. Constants are usually represented by variable names that are written in all capital letters. You do not have to use these, but you may find it useful to do so. It is important that you do not modify the constants that are given in the skeleton. Some of the functions we provide in the skeleton use them.
    - Error messages:
        These are variables that contain the text values of the error messages you will print to standard output when terminating the program. You must use these variables when terminating the program. You are given several of these variables. You must decide when to use which variable. See the project specification for more details.
    - Questions / Statements:
        These are variables that contain the text values of the messages you will print to standard output when asking the players to do something, or when providing them with game event information. You must use these variables when printing such information. Do not modify them. There are several such variables. You must decide when to use them according to the project specification website.
    - Global variables:
        These are variables that are defined outside of any function. The skeleton only defines one global variable, game_over, which indicates whether or not the game has ended. There is also a temporary global variable called PLACE_HOLDER_BOOLEAN, which we use throughout the skeleton as a placeholder to indicate missing functionality which you must implement. See the comments written underneath their definition for more information about these variables. You are allowed to add other global variables if you wish. However, try not to add too many of them.
    - Helper functions:
        These are functions that perform general tasks. Please refer to the documentation of each function to learn more about how you should/can use them. You are welcome to add more helper functions and are not required to place them in this section.
    - Gameplay functions:
        These are functions that control certain functionalities within the game. Many of the functions we provide in the skeleton are incomplete. You must complete them. You are not required to use many of these functions. Unless we explicitly ask you to use a function, you may modify or delete them. These functions often provide helpful hints.
    - Controller functions:
        These are functions that control the flow of the game. You may change or remove them, as long as you implement the functionalities they represent. They provide several helpful hints on how you can implement certain features.
    - Printing functions:
        These are the functions that you must call when printing certain things to the standard output. Since we mark your submission by comparing your program's output with the expected output, you should not modify the printing functions. Doing so may change the way your program writes output to standard output. If this were to happen, your output would not match the expected output. An important function is the `termination(msg)` function, which prints a message to standard output before terminating the program. Here, the `msg` parameter MUST be one of the error message variables that the skeleton provides. This ensures that your program will print messages as we expect them to be printed.
"""
###############################################################################################
########################################### Imports ###########################################
###############################################################################################
# Here, we import the required packages such as stdio.
# You may only use the patched version of the textbook's standard library packages.
# The patched version of the standard libraries can be found on the project website.
# You may also not explicitly import numpy. Use standard libraries' functions instead.
###############################################################################################

import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = str(1)
# Do not remove this! It is used to hide the pygame welcome message which would break your program's output.
import stdio
import stdarray
import sys
# import stddraw
# Standard Draw will only be needed for the second hand-in.


###############################################################################################
########################################## Constants ##########################################
###############################################################################################
# Constants are variables whose values do not change during the execution of the program.
# Constants are indicated by variable names that are written in all capital letters.
# You should not need to modify these constants, unless instructed to do so.
###############################################################################################

AIRPORTS = 10
# The number of airports in the game.
INITIAL_BALANCE = 100.0
# The initial balance of each player.
PLAYERS = 2
# The number of players in the game.
MAX_SUITCASE_VAL = 10
# The maximum number behind a suitcase.
SUITCASES_PER_AIRPORT = 4
# The number of suitcases at each airport.
NUM_OBSTACLE_DISKS = 6
# The number of obstacle disks each player has at the start of the game.
# However, only the red disk should be implemented for the first hand-in.

### These constants represent the indexes that correspond to each of the obstacle disks.
## For example, RED_DISK is the index of the red disk.
RED_DISK = 0
GREEN_DISK = 1
YELLOW_DISK = 2
CYAN_DISK = 3
BLACK_DISK = 4
MAGENTA_DISK = 5
# OBSTACLE_DISK_COLOURS = [stddraw.RED, stddraw.GREEN, stddraw.YELLOW, stddraw.CYAN, stddraw.BLACK, stddraw.MAGENTA]
# Colour constants for the obstacle disks for the second hand-in.
OBSTACLE_DISK_STRINGS = ['RED', 'GREEN', 'YELLOW', 'CYAN', 'BLACK', 'MAGENTA']

### Constants for drawing the game components. Do not modify!
WALL = '|'
CORN = '+'
LINE = '-'

#######################################################################################
################################### Error messages ####################################
#######################################################################################
# When your program terminates, it should print an appropriate message.
# You must call the function `termination(msg)` in such cases.
# The function `termination(msg)` prints a message before terminating the program.
# You must use the error messages below when calling the function `termination(msg)`.
# Error messages must be printed exactly as they are given here. Do not modify them!
# We compare your program's output to our expected output using these error messages.
# If you modify them, your program will not pass the tests.
# NOTE: The value 'Q' is always a valid option.
# NOTE: Players are allowed to terminate the game at any time by entering 'Q'.
# NOTE: In that case, terminate the game with the MSG_USER_TERMINATION message instead.
#######################################################################################
### Command-line-argument-related termination messages:
# You MUST use the following error messages when reporting errors about the command line arguments.
# See the read_command_line_args() function for an example of how you will use them.
ERR_TOO_FEW_ARGS = 'Too few command-line arguments were given.'
# This should terminate the program when too few command-line arguments are given.
ERR_TOO_MANY_ARGS = 'Too many command-line arguments were given.'
# This should terminate the program when too many command-line arguments are given.
ERR_UNIMPLEMENTED = 'This feature is not implemented for the current game mode!'
# Use this error message when the player tries to do something that is not yet implemented. This is only relevant during the first hand-in.
# For example, if the value of the command-line argument corresponding to the graphics mode is '1', this error message should be used, because the graphics mode is not yet supported during the first hand-in.
# Similarly, if a player tries to play an obstacle disk that is not supported in the current game mode, this error message should be used.
# NOTE: if a player enters an entirely invalid obstacle disk option, the error message ERR_INVALID_DISK should be used instead.
# Similarly, in game mode 2, players cannot ask their opponent to move from their current airport, so use ERR_UNIMPLEMENTED if they try to do this.

ERR_UNEXPECTED = 'Unexpected input!'
# A generic error message that can be used when the input is unexpected. This will only be used in cases where no other error message is appropriate.
# Currently, this error message should not be used unless instructed to do so.
# We include this in the skeleton in case the project team finds a case where it is appropriate.
# Only if the project team finds a case where this error message is appropriate should you use it. You may use this error message in your own tests, but there is currently no case that specifies using this error message. Do not include this error message in your submission, except in the unlikely event where the project team notifies you of an overlooked termination event.
MSG_NO_NEW_GAME_TERMINATION = 'The game has ended.'
# When the user has indicated they do not want to play another game after the previous game has ended, print this message and terminate the program using the `termination(msg)` function.
ERR_INVALID_TURN_MENU_OPTION = 'Invalid turn menu option!'
# Use this error message when a player is prompted to choose whether they want to
#   - (A)sk their opponent to leave their current airport,
#   - (S)tay at their current airport,
#   - (F)ly to a different airport, or
#   - (U)se one of their obstacle disks:
#   - and they enter a value that does not correspond with one of the expected answers (A, S, F, U).
ERR_FLOAT_EXPECTED = 'A floating point number was expected!'
# Use this error message we expect a floating point number as input, but the associated value cannot be parsed as a float.
ERR_NOT_YES_OR_NO = 'Expected "Y" or "N" as input!'


#### Airport/ Flight related termination messages:
ERR_INVALID_AIRPORT = 'Invalid airport!'
# Use this error message when an invalid airport is given as input.
# For example, if the player enters 'Z' when they are asked to enter an airport, this error message should be used.
ERR_FLYING_TO_SAME_AIRPORT = 'You are already at this airport!'
# Use this error message when a player tries to fly to the airport they are already at.
ERR_FLYING_TO_OPPONENT_AIRPORT = 'You cannot fly to an airport that is occupied by your opponent!'
# Use this error message when a player tries to fly to an airport that is occupied by their opponent.

#### Suitcase-related termination messages:
ERR_FLIPPING_COLLECTED_SUITCASE = 'This suitcase cannot be flipped as it has already been collected.'
# Use this error message when a player tries to flip a suitcase that has already been collected by either player.
ERR_FLIP_RESTRICTED = 'You are not allowed to flip this suitcase. You are trying to flip a suitcase that you have already flipped during your visit.'
# Use this error message when a player tries to flip a suitcase that they have already flipped during their current stay at their current airport. The flip restriction is reset when the player leaves the airport, when they collect a suitcase, or when a helpful obstacle disk is played.
ERR_INVALID_SUITCASE_POSITION = 'Invalid suitcase position!'
# When giving the position of a suitcase as input, we expect a value between 1 and 4, both inclusive.
ERR_INVALID_SUITCASE_NUMBER = 'Invalid suitcase number! The number behind a suitcase must be a value between 1 and 10.'
# Use this error message when the number behind a suitcase is given as input and it is not a value between 1 and 10, both inclusive.
ERR_BALANCE = 'Insufficient funds!'
# Use this error message when a player tries to do something that would bankrupt themselves. For example, if they try to fly to another airport when they can't afford it.
ERR_CANT_STAY = 'You cannot stay at this airport! You cannot flip any suitcases here.'
# Use this error message when a player tries to stay at their current airport even though there are no suitcases left for them to flip.
ERR_CANT_ASK = 'You have already asked your opponent if they want to move this turn!'
# Use this error message when the player tries to ask their opponent to move to another airport after they have already done so during the current round.
ERR_EMPTY_STD_INPUT = 'Standard input is empty!'
# Use this error message when the standard input is empty.
MSG_USER_TERMINATION = 'Player terminated the game.'
# Use this termination message when the user enters 'Q' to quit the game.

#### Obstacle disk-related termination messages:
ERR_NO_DISKS = 'You have no obstacle disks that may be played at the moment!'
# Use this error message when the player tries to play an obstacle disk when they have no disks left or cannot currently play any of their remaining disks.
# For example, if the player enters 'U' when asked what they want to do, and they have no obstacle disks left or have already played an obstacle disk during this turn, this error message should be used.
# NOTE: The player can ONLY play the red disk directly after their opponent has refused their request to leave their current airport. If they enter 'U' on the options menu when their opponent has not refused to fly to another airport during this turn, and they have no other disks left, this error message should be used, even if the current player has not yet played their red disk.
# NOTE: This also has other implications. Say the current player has asked their opponent to leave their current airport, and the opponent has refused. Assume the current player has not played their red disk yet. Then, the current player can now play the red disk after they enter 'U' on the options menu. However, no other obstacle disks should be displayed at this point, as the current player can ONLY play their red obstacle disk after their opponent has refused their request to fly to another airport. Even if the current player still has other obstacle disks left, they should not be displayed at this point -- only the red disk should be displayed (assuming you have correctly validated whether or not the red disk can be played according to the specification on when a player can and cannot play the red disk).
# NOTE: Similarly, although mostly related to the requirements for the second hand-in, if the current player selects the 'U' option on the options menu but their opponent was not asked leave their current airport, then ONLY the (available, valid, and implemented) non-red obstacle disks should be displayed -- even if the current player has not yet played their red disk. The red disk may only be displayed directly after the opponent has refused the current player's request to fly to another airport -- in that case, only the red obstacle disk may be displayed, the other obstacle disks cannot be played in the turn where you ask your opponent to fly to another airport. If you don't ask your opponent to fly to another airport, the red disk cannot be played, no matter what.
ERR_INVALID_DISK = 'Invalid obstacle disk option given as input!'
# Use this error message when a player gives an invalid obstacle disk as input. For example, if they are asked to choose which disk to play and they enter 'Z'.
# The following are valid obstacle disk options: ['R', 'G', 'Y', 'C', 'B', 'M']

### NOTE: The following error messages are only relevant for the second hand-in.
ERR_ALREADY_PLAYED_DISK = 'You have already played this obstacle disk!'
# Use this error message when the player tries to play an obstacle disk that they have already played.
ERR_CANT_PLAY_RED_DISK = 'You can only play the red obstacle disk directly after your opponent has refused your request for them to leave their current airport'
# Use this error message when the player tries to play the red disk before their opponent has refused to leave their current airport.
# This may happen when a player enters 'U' when asked what they want to do during their turn, and they enter 'R' to play the red disk even though their opponent had not refused (or been asked) their request to leave during this turn. This will only be relevant for the second hand-in since the 'U' option will not be displayed when the red obstacle disk cannot be played during the first hand-in.
ERR_CANT_PLAY_CYAN_DISK = 'You cannot play the cyan disk until your opponent has moved from their first airport!'
# Use this error message when the player tries to play the cyan disk before their opponent has moved from their first airport.
ERR_CANT_PLAY_MAGENTA_DISK = 'You can only play the magenta disk if your opponent has collected more suitcases that you have.'
# Use this error message when the player tries to play the magenta disk while their opponent has not collected more suitcases than the player has.
ERR_CANT_PLAY_BLACK_DISK = 'You cannot play the black disk when you are not allowed to flip any of the suitcases at your current airport!'
# Use this error message when the player tries to play the black disk when there are no suitcases that they are allowed to flip at their current airport.
# This could happen when the player has already flipped all of the uncollected suitcases during their visit to their current airport.
ERR_MUST_PLAY_HELPFUL_DISK = 'You must play a helpful disk, given your current predicament!'
# Not relevant for the first hand-in.
# Use this error message when the player tries to play a disk that is not helpful to them but the only way for them to avoid losing was to play a helpful obstacle disk. For example, if they have no suitcases left to flip, cannot afford to fly, still have a yellow disk available, and try to play the green disk (which is assumed to be available as well).

#######################################################################################
############################### Questions / Statements ################################
#######################################################################################
# These messages must be used to ask the user for input or to provide information.
# Do not call the termination function in these cases.
# You must call the appropriate stdio.write*() function to print these messages.
# If a message contains a format specifier (like %d) you must call stdio.writef() and
# pass the appropriate arguments.
# For example, if a message requires the player number, you must call stdio.writef().
# If the message does not contain a format specifier, you must call stdio.writeln().
# These messages must be printed exactly as they are given here. Do not modify them!
# We compare your program's output to our expected output using these messages.
# If you modify them, your program will not pass the tests.
#######################################################################################
# Command-line-argument-related messages:
MSG_INVALID_GAME_MODE = 'Invalid game mode argument. Using the default value for game_mode instead.'
# This does not terminate the program. It just prints the error message and uses the default value for the game mode instead.
MSG_INVALID_GRAPHICS_MODE = 'Invalid graphics mode indicator argument. Using the default value for graphics_mode instead.'
# This does not terminate the program. It just prints the error message and uses the default value for graphics mode instead.

### Flight:
ASK_AIRPORT_DESTINATION = 'Player %d, please select the airport you would like to go to. (A-J)\n'
# Print this message when the player is asked to select an airport to fly to.
SAY_INITIAL_AIRPORT = 'Player %d has selected Airport %s as their first airport.\n\n'
# Print this message when the player selects their first airport. This should only happen once for each player per game.
SAY_FLIGHT_INFO = 'Player %d has flown from Airport %s to Airport %s at a cost of R%.2f.\n\n'
# Print this message when the player flies from one airport to another.

### Asking your opponent to leave their current airport:
SAY_REQUEST_LEAVE = 'Player %d has asked Player %d if they would like to leave the airport.\n\n'
# Print this message when the player asks their opponent to leave their current airport.
ASK_WANT_TO_LEAVE = 'Player %d, would you like to leave the airport? (Y/N)\n'
# Print this message when the asking the opponent if they want to leave their current airport after being asked to do so.
SAY_PLAYER_LEFT = 'Player %d has left their airport upon Player %d\'s request.\n'
# Print this message when the opponent leaves their current airport after being asked to do so.
SAY_REFUSED_TO_LEAVE = 'Player %d has refused Player %d\'s request to leave their airport.\n\n'
# Print this message when the opponent refuses to leave their current airport after being asked to do so.

### Obstacle disks:
SAY_PLAY_OBSTACLE_DISK = 'Player %d has played their %s obstacle disk.\n\n'
# Print this message when the player plays an obstacle disk. NOTE: The second format specifier represents the name of the obstacle disk that the player played.
# The name of the obstacle disk is one of the following: 'RED', 'GREEN', 'YELLOW', 'CYAN', 'BLACK', or 'MAGENTA'.
# For safety, you can use the array OBSTACLE_DISK_STRINGS alongside the obstacle disk index constants to get the name of the obstacle disk.
# For example, if the player played the red disk, you can use the following code to get the name of the disk:
#   `disk_name = OBSTACLE_DISK_STRINGS[RED_DISK]`
# Then you should call stdio.writef() with the following format string:
#   `stdio.writef(SAY_PLAY_OBSTACLE_DISK, player_index + 1, disk_name)` # Where the value of player_index is 0 for player 1 and 1 for player 2.
# NOTE: Only the red obstacle disk is available during the first hand-in. You only need to use the messages that are relevant to the red obstacle disk during the first hand-in, the other obstacle disks should trigger an error if the player attempts to play any of them.
SAY_RED_DISK = 'Player %d, you are forced to move from your current airport, but Player %d will pay for your flight.\n'
# Use this message when the player is forced to move from their current airport because their opponent played the red obstacle disk.
SAY_RED_DISK_DEDUCTION = 'Player %d, you have paid for Player %d\'s flight at a cost of R%.2f. Your new balance is R%.2f\n\n'
# Use this message when the player is forced to pay for their opponent's flight because their opponent played the red obstacle disk.

ASK_WHICH_OBSTACLE_DISK = 'Player %d, which obstacle disk would you like to use? (R/G/Y/C/B/M)\n'
# This message should be printed when the player is asked to select an obstacle disk to play after they have entered 'U' as their option. See the `show_options()` function for more details.
# NOTE: The red disk is included in this message because it is the ONLY valid obstacle disk option when the current player is asked to select an obstacle disk to play, immediately after their opponent has refused the current player's request to fly to another airport (assuming the other restrictions on when the red obstacle disk can be played are taken into account).
# Players may only play the red disk after their opponent has refused to leave their current airport.
# You should call the `print_obstacle_disks()` function to print the obstacle disks that the player can play after selecting 'U' as their option in `show_options()`.
# If the player uses the 'U' option to print the red obstacle disk after their opponent has refused to leave their current airport, you are not allowed to display any other obstacle disks, even if they are available and valid according to the individual obstacle disk's rules. Only the red disk can be played after the opponent has refused to leave their current airport. This works both ways; if the opponent has not refused to leave their current airport, the current player is not allowed to play the red disk. However, since the other obstacle disks are not implemented during the first hand-in, the restriction is rather simplified for the other obstacle disks. Just make sure you print the correct error message when the player tries to play an obstacle disk that is not available to them at the time.
# TODO: The following messages about the obstacle disks are only relevant to the second hand-in.
SAY_GREEN_DISK = 'The positions of the four suitcases have been shuffled, at each airport.\n\n'
# Print this message when the player plays the green disk.
ASK_YELLOW_DISK_AIRPORT = 'Player %d, please select the airport whose suitcases will be swapped with the suitcases at your current airport. (A-J)\n'
# Ask the player who plays their yellow disk to select an airport whose suitcases will be swapped with the suitcases at their current airport.
SAY_YELLOW_DISK_AIRPORT = 'Player %d has swapped the suitcases of Airport %s with that of Airport %s.\n\n'
# Print this message when the player after the player has selected which airport's suitcases should be swapped with their current airport.
# The first string format specifier represents the player's current airport. The second string format specifier represents the airport whose suitcases were swapped with the player's current airport.
SAY_CYAN_DISK = 'Player %d is forced to pay R%.2f in taxes. Their new balance is R%.2f.\n\n'
# Print this message when the player plays the cyan disk, forcing their opponent to pay taxes equal to the cost of flying from the opponent's previous airport to the opponent's current airport.
SAY_BLACK_DISK = 'The black disk has revealed the following suitcases at Airport %s.\n\n'
# Print this message when the player plays the black disk. Afterwards, you should call the `black_disk_print()` function to print the suitcase numbers that are now revealed at that airport.
SAY_MAGENTA_DISK = 'The magenta disk has added R%.2f to the balance of Player %d. Their new balance is R%.2f.\n\n'
# Print this message when the player plays the magenta disk.

### The four options that the player can choose from during their turn:
# You must only display the options that are available to the player. For example, if a player cannot afford to fly to any other airport, you should not display the option to fly to another airport.
OPT_HEADER = 'Player %d, you can do the following:\n'
OPT_ASK_OPPONENT_TO_MOVE = '\t(A)sk your opponent to leave their airport.'
OPT_STAY_AT_CURRENT_AIRPORT = '\t(S)tay at your current airport.'
OPT_FLY_TO_ANOTHER_AIRPORT = '\t(F)ly to a different airport.'
OPT_USE_OBSTACLE_DISK = '\t(U)se one of your available obstacle disks.\n'

### Suitcase flipping:
ASK_SUITCASE_POSITION = 'Player %d, please enter the position of the suitcase you would like to flip. (1-4)\n'
# Print this message when a player needs to flip one of the four suitcases at their current airport.
SAY_SUITCASE_FLIPPED = 'Player %d has flipped the suitcase at position %d of airport %s to reveal:\n\n'
# Print this message when a player flips a suitcase at their current airport. After printing this message, you should call `print_single_suitcase_number()` to reveal the number behind the suitcase that was just flipped.
SAY_COLLECTED = 'Player %d has collected the suitcase at position %d of airport %s.\n\n'
# Print this message when a player collects a suitcase at their current airport. This should directly follow the call to `print_single_suitcase_number()`, if the player could collect the suitcase they have just flipped.
SAY_NOT_COLLECTED = 'Player %d could not collect the suitcase at position %d of airport %s.\n\n'
# Print this message when a player cannot collect the suitcase that they have just flipped. This should directly follow the call to `print_single_suitcase_number()`, if the player could not collect the suitcase they have just flipped.

### Win / Loss messages:
LOSS_NO_MORE_MOVES = 'Player %d cannot make any more moves!\n'
# Print this message when a player loses the game because they cannot make any more moves. This should happen when the player has no more suitcases to collect, cannot afford to fly to another airport, and has no more helpful obstacle disk left to play.
LOSS_BANKRUPT = 'Player %d has been bankrupted!\n'
# Print this message when a player loses the game because they have been bankrupted. This should happen when the player has a negative balance.
WIN_COLLECTED_ALL_SUITCASES = 'Player %d has collected all of their suitcases!\n'
# Print this message when a player wins the game because they have collected all 10 suitcase numbers in sequence.
WIN_MESSAGE = 'Player %d has won the game!\n\n'
# Print this after printing one of the three messages above.

### New game:
ASK_NEW_GAME = 'Do you want to start a new game? (Y/N)'
# Print this message when the player is asked if they want to start a new game.
SAY_YES_NEW_GAME = 'A new game is starting!\n'
# Print this message when the user has indicated they want to play another game after the previous game has ended.

#######################################################################################
################################## Global variables ###################################
#######################################################################################
# Global variables are variables that are defined outside of any function.
# You may add or remove global variables. Just make sure you do so correctly.
#######################################################################################

game_over = False
# A Boolean variable that indicates whether the game is over. It is set to True when the game is over.

PLACE_HOLDER_BOOLEAN = False # TODO: remove this variable once you have added the missing functionalities it represents.
# This is only a placeholder variable.
# We use this placeholder variable throughout the skeleton to indicate missing functionality.
# Whenever you see this variable, you should replace it with the correct value/ functionality.
# You may delete this variable once you have implemented the functionalities that are currently missing.

###############################################################################################
###################################### Helper functions #######################################
###############################################################################################
# You may add helper functions here if you wish.
# The following functions are provided to help you get started.
# Some of these functions are incomplete. You must complete them.
###############################################################################################

def end_game():
    """
    This function is called when the game is over.
    Remember to reset the global variables to their initial values when starting a new game.
    To seperate global variables from local variables, global variables are changed in their own function. While this is not required, it is considered good practice.
    You may delete this function if you wish.
    """
    global game_over
    game_over = True

def get_opponent(player):
    """
    Given the index associated with a player, this function returns the index of the opponent.
    NOTE: These are indexes, not player numbers. The player numbers are 1 and 2, but the indexes are 0 and 1.

    You are not required to use this function. You may delete it if you wish. Furthermore, while the skeleton often uses indexes when referring to players, there are other ways to implement this. The project team felt this was the most versatile way to implement it. NOTE: some of the printing functions assume that the player index is 0 or 1. If you choose to use a different way to represent players, you must keep the printing functions in mind. You should not modify the printing functions. Doing so may change the way your program writes output to standard output. If this were to happen, your output would not match the expected output.

    Parameters
    ----------
    player
        The index of the current player. (0 for player 1, 1 for player 2)

    Returns
    -------
        The index of the opponent. (0 for player 1, 1 for player 2)
    """
    return 1 - player

def check_stdio_empty():
    """
    Check whether standard input is empty. If it is, terminate the game and display the associated error message.
    The code within this function should give you an idea of how you should terminate the program when an error occurs, using the appropriate error message.
    You are not required to use this function, but you MUST use the variable `ERR_EMPTY_STD_INPUT` to terminate the program using the error message associated with an empty standard input.
    """
    if stdio.isEmpty():
        termination(ERR_EMPTY_STD_INPUT)

def int_to_char(index):
    """
    Convert an integer to a character.

    This function is the inverse of `char_to_int(ch)`. This is used to convert airport indices to their corresponding letters. It works by adding 65 (the ASCII code for 'A') to the given integer. You are allowed to modify or delete this function if you wish.

    Keep in mind that this function performs no error checking. If you accidentally pass an invalid index, your program may behave incorrectly.

    Parameters
    ----------
    index
        An integer value that corresponds to the index of an airport that will be converted to its associated upper case letter. Since the airports are represented by the letters A-J, the index should fall between 0 and 9, both inclusive.

    Returns
    -------
        The character corresponding to the given integer. Python interprets the returned value as a string.

    Examples
    --------
    >>> stdio.writeln(int_to_char(0))
    A
    >>> stdio.writeln(int_to_char(1))
    B
    >>> stdio.writeln(int_to_char(9))
    J
    """
    return chr(index + 65)

def char_to_int(ch):
    """
    Converts a character to an integer.

    This function is the inverse of `int_to_char`. It is used to convert airport letters to their corresponding indices. It works by subtracting 65 (the ASCII value 'A') from the given character. Consequently, this function expects the parameter `ch` to be an upper-case letter. You are allowed to modify or delete this function if you wish.

    This function does not check perform any validation on the parameter `ch`. If you accidentally pass an invalid character, your program may behave incorrectly.

    Parameters
    ----------
    ch
        The character (given as a string of length 1) corresponding to the upper-case airport letter.

    Returns
    -------
        The index of the airport corresponding to the given character.

    Examples
    --------
    >>> stdio.writeln(char_to_int('A'))
    0
    >>> stdio.writeln(char_to_int('B'))
    1
    >>> stdio.writeln(char_to_int('J'))
    9
    """
    return ord(str(ch).upper()) - 65

def read_command_line_args():
    """
    Read the command-line arguments.

    The game client should take two command-line arguments as input, in the following order:
    1. The game mode (default is 0):
       - 0 means the game functions according to the specification for the first hand-in.
       - 1 means the game functions according to the specification for the second hand-in.
       - 2 invokes the automatic solver.
    2. The GUI indicator (default is 0):
       - 0 means the game is played in the terminal (text mode).
       - 1 means the game is played in the GUI (graphical mode).

    You must perform input validation on the command-line arguments. A command-line argument is invalid if it is not one of the values listed above.
    If the value of a command-line argument is invalid, you must print a message using the appropriate message variable and set the value of the corresponding variable to its default value. Invalid command-line arguments do not terminate the program. Instead, the program should use the default value and inform the user with a message.
    During the first hand-in, the program only supports game mode 0 and graphics mode 0. If the user tries to use any other game mode or graphics mode, terminate the program using the appropriate error message. You should remove this check during the second hand-in, at which time the program should support all game modes and graphics modes.

    You may change the structure of this function if you wish, but you MUST use the constant variables that correspond to the correct error/information messages. When terminating the program, you MUST use the `termination(msg)` function.

    Returns
    -------
        A list containing the values of the arguments game_mode and graphics_mode. The first element is the game mode, the second element is the graphics mode.
    """
    game_mode = 0 # The default game mode is 0.
    graphics_mode = 0 # The default graphics mode is 0.

    # TODO: Check whether the expected number of command-line arguments were passed to the program.
    if PLACE_HOLDER_BOOLEAN: # TODO: Replace PLACE_HOLDER_BOOLEAN with the correct condition or rewrite this if statement without it.
        # Below is an example of what we mean by using the error messages defined at the beginning of the skeleton file to terminate the program.
        # This terminates the program with the error message ERR_TOO_FEW_ARGS, when the condition above is True.
        # Specifically, call the `termination(msg)` with the error message variable ERR_TOO_FEW_ARGS when too few command line arguments are given.
        # The code below serves as a guideline on how to terminate the program with an appropriate message.
        termination(ERR_TOO_FEW_ARGS)
    if PLACE_HOLDER_BOOLEAN: # TODO: Replace PLACE_HOLDER_BOOLEAN with the correct condition or rewrite this if statement without it.
        # Similarly, call the `termination(msg)` function with the error message variable ERR_TOO_MANY_ARGS when too many command line arguments are given.
        termination(ERR_TOO_MANY_ARGS)

    # TODO: Read the game mode and the graphics mode from the command line arguments.
    # NOTE: Do not call the termination() function if the value of either argument is invalid.
    # Instead, print the associated information message (MSG_INVALID_GAME_MODE or MSG_INVALID_GRAPHICS_MODE) using stdio.writeln and set the associated variable to its default value.
    # If the value of only one argument is invalid, you must still read the other argument. Only if both arguments are invalid should you use both default values.
    # Remember, there is a difference between an invalid argument value and a currently unimplemented argument value.
    # An invalid argument value is one that is not one of the specifiec options. For example, if the game mode is 'A', it is invalid.
    # An unimplemented argument value is one that is valid, but the functionality is not yet implemented. For example, if the game mode is '1', it is unimplemented during the first hand-in.

    # Do some validation checks on the arguments and set the game mode and graphics mode accordingly.
    # TODO: If the game mode is invalid, print the message MSG_INVALID_GAME_MODE. You may want to modify this to include some sort of if-else logic.
    stdio.writeln(MSG_INVALID_GAME_MODE) # If the game mode is invalid, print this message.

    # TODO: If the graphics mode is invalid, print the message MSG_INVALID_GRAPHICS_MODE. You may want to modify this to include some sort of if-else logic.
    stdio.writeln(MSG_INVALID_GRAPHICS_MODE) # If the graphics mode is invalid, print this message.


    # If the argument value is a valid option, but the functionality is not yet implemented, you should terminate the program.
    # For the first hand-in, only game mode 0 is supported.
    # For the second hand-in, all game modes (0, 1, and 2) are supported.
    # TODO: Remove the following if statement for the second hand-in.
    if game_mode != 0 or graphics_mode != 0: # if the game mode is not 0 or if the graphics mode is not 0, terminate the program.
        termination(ERR_UNIMPLEMENTED)

    # Return a list containing the values of the arguments game_mode and graphics_mode.
    # You may change the way this function returns the values if you wish.
    return [game_mode, graphics_mode]

def generate_cost_matrix(airport_coordinates_matrix):
    """
    Returns a cost matrix used to look up the cost of traveling between from one airport to another.

    # TODO: call this function to generate the cost matrix from the airport coordinates.

    The cost matrix is calculated from the airport coordinates which were previously read from the input file, which are given as a parameter to this function.
    Do not modify the contents of this function unless you are sure you know what you are doing. If the cost matrix is not generated correctly, the game will not work properly.

    You are not required to understand how this function calculates the cost matrix entries. You just need to be able to use the cost matrix this function returns. In short, this function calculates the cost of traveling between two airports by calculating the Euclidean distance between the two airports and scaling that value a bit.

    Once you get the cost matrix, you can use it to look up the cost of traveling between two airports. For example, if you want to know the cost of traveling from airport A (index 0) to airport B (index 1), you can use the following code:
        `cost_from_A_to_B = cost_matrix[0][1]`
    Since the cost matrix will always be symmetric, you can also use the following code to get the same result:
        `cost_from_B_to_A = cost_matrix[1][0]` # This will give the same result as the previous line (cost_from_A_to_B).
    Similarly, the cost matrix entries on the diagonal will always be 0. For example, the cost of traveling from airport A (index 0) to airport A (index 0) is 0:
        `cost_from_A_to_A = cost_matrix[0][0]` # This will always be 0.

    Make sure that the you understand how the parameter `airport_coordinates_matrix` should be populated. This parameter is a 2D array of size `10 x 2` which corresponds to the `x` and `y` coordinates of each airport. For example, the `x` coordinate of the airport at index 0 (airport A) is `airport_coordinates_matrix[0][0]` and the `y` coordinate of the same airport is `airport_coordinates_matrix[0][1]`. Similarly, the `x` coordinate of the airport at index 9 (airport J) is `airport_coordinates_matrix[9][0]` and the `y` coordinate of the same airport is `airport_coordinates_matrix[9][1]`.

    You should only need to call this function once -- before the first game starts.

    Parameters
    ----------
    airport_coordinates_matrix
        A 2D array of size 10 x 2 which corresponds to the `x` and `y` coordinates of each airport.
        For example, the `x` coordinate of the airport at index 0 (airport A) is `airport_coordinates_matrix[0][0]` and the `y` coordinate of the same airport is `airport_coordinates_matrix[0][1]`.

    Returns
    -------
        A 2D array of size `10 x 10`, where each entry corresponds to the cost of traveling the two associated airports.
    """
    max_c = float('-inf')
    min_c = float('+inf')
    new_cost_matrix = stdarray.create2D(AIRPORTS, AIRPORTS, 0.0)
    for a1 in range(AIRPORTS):
        new_cost_matrix[a1][a1] = 0.0
        for a2 in range(a1 + 1, AIRPORTS):
            new_cost_matrix[a1][a2] = (airport_coordinates_matrix[a1][0] - airport_coordinates_matrix[a2][0])**2
            new_cost_matrix[a1][a2] += (airport_coordinates_matrix[a1][1] - airport_coordinates_matrix[a2][1])**2
            new_cost_matrix[a1][a2] = new_cost_matrix[a1][a2]**0.5
            new_cost_matrix[a2][a1] = new_cost_matrix[a1][a2]
            if new_cost_matrix[a2][a1] < min_c:
                min_c = new_cost_matrix[a2][a1]
            if new_cost_matrix[a2][a1] > max_c:
                max_c = new_cost_matrix[a2][a1]
    # Scale the cost matrix values to be between 0 and upper_limit.
    upper_limit = 20.0
    for a1 in range(AIRPORTS):
        for a2 in range(a1 + 1, AIRPORTS):
            new_cost_matrix[a1][a2] = upper_limit*((new_cost_matrix[a1][a2] - min_c) / (max_c - min_c))
            new_cost_matrix[a2][a1] = new_cost_matrix[a1][a2]
    # Return the cost matrix, as calculated above.
    return new_cost_matrix

def calculate_magenta_disk_bonus(player_last_suitcase, opponent_last_suitcase):
    """
    Calculates the bonus that the player receives if they play their magenta obstacle disk.

    NOTE: You do not need to use this function during your implementation of the first hand-in. In fact, you should only try to use it if you are done with the implementation for the first hand-in and you want to start with the implementation of the second hand-in early on. The magenta disk should only be implemented for the second hand-in.

    The magenta disk can be played to add money to the player's wallet. The magenta disk only benefits a player if they have collected fewer suitcases than their opponent.
    This function calculates the bonus that the player receives if they play their magenta disk using the following formula:

    Let `x` = the number of suitcases collected by the player who plays the magenta disk.
    Let `y` = the number of suitcases collected by the opponent of the player who plays the magenta disk.
        `bonus = (9 - x) * max(0, y - x)`

    Parameters
    ----------
    player_last_suitcase
        The last suitcase number collected by the player who plays the magenta disk. This is equal to the number of suitcases collected by the player.
    opponent_last_suitcase
        The last suitcase number collected by the opponent of the player who plays the magenta disk. This is equal to the number of suitcases collected by the opponent.

    Returns
    -------
        The bonus that the player receives if they play their magenta disk.
    """
    return (9 - player_last_suitcase) * max(0, opponent_last_suitcase - player_last_suitcase)

###############################################################################################
##################################### Gameplay functions ######################################
###############################################################################################
# The following functions are used to control certain functionalities during the game.
# You may change the structure of these functions or opt not to use them.
# You may also add additional functions if you wish.
# Some of these functions are incomplete. You must complete them.
###############################################################################################


def show_options(player, can_ask_opponent_to_leave, can_play_obstacle, game_mode):
    """
    At the start of their turn, show the player what they can do at their current airport.

    The name '`show_options`' is quite vague, considering you are presented with several options throughout the game. Feel free to rename it. You may interpret this function as a 'main menu' of sorts since it is the entry point of a decision tree during every turn (except for the initial airport selection phase). As with most main menu's, no move is made when a player enters one of the options `(A, S, F, U)`. Instead, the player will presented with new questions based on their choice, usually leading to an actual gameplay-related interaction -- unless the input of `show_options` is invalid, in which case we terminate the game (with the appropriate error message).

    A player has four possible options at this stage:
        - Ask the opponent to leave their airport.
        - Stay at the current airport.
        - Fly to another airport.
        - Use an obstacle disk.

    NOTE: The menu is dynamically generated based on the player's current state. Consider how you will implement the following:
        - When the player has already asked their opponent to leave their airport during this turn, the option to ask the opponent to leave their airport is not shown.
        - When the player cannot afford to fly to another airport, the option to fly to another airport is not shown.
        - When the player has no obstacle disks that they can use when the menu is printed, the option to use an obstacle disk is not shown.
        - When the player cannot flip any of the suitcases at the current airport (e.g., as a result of the flip restriction rule or suitcases that have already been collected), the option to stay at the current airport is not shown.

    NOTE: You must decide how you will implement the above. This will be a crucial part of your implementation. Since the menu is printed at least once per turn, broken functionality will deviate from the expected behaviour of the game. We mark your implementation by comparing your program's output with the expected output. Thus, if your menu does not behave as expected, your program will produce output that will differ from the expected output throughout the rest of the marking process. Thus, even if your implementation of some other functionality is completely correct, a broken menu that results in output differing from the expected output will still result in you receiving 0 for any test case where the menu is not printed correctly. This is an extremely important point to consider.

    You may modify certain parts of this function. However, ensure you do not disturb how the output is printed. If you want to remove or add any parameters, you may do so. The current parameters are provided as a guide.

    Parameters
    ----------
    player
        The index of the player (an index of 0 means player 1, and a index of 1 means player 2).
    can_ask_opponent_to_leave
        A Boolean variable. True if the player can ask the opponent to leave their airport, False otherwise. This happens when the player has not already asked the opponent to leave their airport during this turn, for example.
    can_play_obstacle
        A Boolean variable. True if the player is allowed to play an obstacle disk at the moment, False otherwise. NOTE: this variable is not used to indicate the case where all obstacle disks have already been used, or even whether or not the rules of the individual obstacle disks do not allow them being played. For example, lack of restrictions associated with playing the yellow disk rarely results in the yellow disk not being played. However, the yellow disk is cannot be played when the player has already asked the opponent to leave their airport during this turn, since only the red obstacle disk can be played after such a request -- of course, this example assumes you have considered the other rules/restrictions associated with playing the red obstacle disk as well.
    game_mode
        The game mode, with value according to the first command-line argument. This is either 0, 1, or 2. There are much more efficient ways to implement this functionality, but it was easiest to illustrate how we use the `game_mode` variable by simply specifying it as a parameter.
    """
    if game_mode == 2:
        # Furthermore, when the game_mode variable is set to 2, indicating AI game-play, then the (AI) players cannot use obstacle disks.
        can_play_obstacle = False
        can_ask_opponent_to_leave = False
    can_fly = PLACE_HOLDER_BOOLEAN # TODO: Replace the placeholder boolean with your own code.
    can_stay = PLACE_HOLDER_BOOLEAN # TODO: Replace the placeholder boolean with your own code.
    # The four Boolean variables above indicate whether the player can do the corresponding action.
    # For example, if the player can ask the opponent to leave their airport, then the can_ask_opponent_to_leave variable will be set to True.
    #               This may be false if the player has already asked the opponent to leave their airport during this round.
    # The can_fly variable indicates whether the player can fly to another airport.
    # The can_stay variable indicates whether the player can stay at their current airport.
    # The can_play_obstacle variable indicates whether the player can play an obstacle disk.
    # NOTE: the current player can only play the red obstacle disk immediately after their opponent has refused the current player's request to fly to another airport -- assuming the current player has not yet played their red disk.
    # For the first hand-in, only the red obstacle disk is implemented. A player can only play the red obstacle disk when they have already asked the opponent to leave their airport, and the opponent has refused to leave. This implies that the red obstacle disk is only displayed sometimes!
    # When the show_options function is called after the opponent has refused to fly to a different airport, the current player will be able to select the 'U' option, but it will only display the red obstacle disk (assuming the current player has not played the red disk yet) -- no other disks should be displayed in this case!
    # If the current player has already used their red obstacle disk, the 'U' option should not be displayed after calling show_options after the opponent has refused the current player's request.
    # If the current player did not ask their opponent to leave their airport, the 'U' option should only display the other obstacle disks (depending on the non-red disks' availabilities), even if the player has not used the red disk yet.
    # Since the other disks will only be implemented for the second hand-in, only the red disk should be displayed here (noting the aforementioned rules about when the red disk can be used).

    # TODO: Replace the following placeholder code with your own code.
    # Here, you want to check if the player has lost the game because they cannot make a move that would benefit their case.
    # If the player cannot make a move that would benefit their case, they lose.
    # You may want to use a combination of the boolean variables above, as well as the helpful_disk_available() function.
    if PLACE_HOLDER_BOOLEAN:
        return

    # DO NOT MODIFY THE FOLLOWING PRINT MESSAGES. These are the options to present to the player.
    # The options are only printed if the player can make that move.
    # For example, if the player cannot fly to another airport, then the option to fly is not printed.
    # If you feel the need to change the logic of the if statements, you may do so.
    # Just be sure that the options are only printed if the player can make that move and that the options are printed in the same order as they are listed below.
    # To reiterate, you may change the logic of the if statements, but you may not change the print messages.
    stdio.writef(OPT_HEADER, player + 1)
    if can_ask_opponent_to_leave:
        stdio.writeln(OPT_ASK_OPPONENT_TO_MOVE)
    if can_stay:
        stdio.writeln(OPT_STAY_AT_CURRENT_AIRPORT)
    if can_fly:
        stdio.writeln(OPT_FLY_TO_ANOTHER_AIRPORT)
    if can_play_obstacle:
        stdio.writeln(OPT_USE_OBSTACLE_DISK)
        # TODO: Modify the following code by implementing the functionality of the red obstacle. For the first hand-in, the non-red-disk entries of the `print_obstacle_disks` array can be set to False at all times, since the other obstacle disks will only be required for the second hand-in.
        can_play_red = PLACE_HOLDER_BOOLEAN # TODO: replace the `PLACE_HOLDER_BOOLEAN` variable appropriately
        can_play_disk_array = [can_play_red, False, False, False, False, False] # TODO: You will need to add similar functionality for the other non-red disks during your implementation of the second hand-in.
        print_obstacle_disks(can_play_disk_array)
        # You will need to modify the function arguments in the previous line appropriately.
        # The majority of the `print_obstacle_disks` function is mainly applicable to the second hand-in, since the red disk is the only obstacle disk implemented for the first hand-in. Ensure that you understand when you need to display the red obstacle using `print_obstacle_disks` disk, however!
    stdio.writeln() # Make sure you do not remove this line. It is used to separate the options above from the output that follows. This is important for the marking of your program.

    # TODO: Read input from standard input, appropriately.
    # We expect the following possible inputs:
    #   - "`A`" for Ask
    #   - "`S`" for Stay
    #   - "`F`" for Fly
    #   - "`U`" for Use an obstacle disk
    # Then decide what to do next, based on the input.


###############################################################################################
#################################### Controller functions #####################################
###############################################################################################
# The following functions are used to control the flow of the game.
# You may change the structure of these functions, as long as everything works correctly.
# You may also add additional functions if you wish.
# Some of these functions are incomplete. You must complete the functionality they represent.
###############################################################################################

def runner():
    """
    This is the first function that will be called when the program is run. The following steps should take place:
    1. Read the command line arguments.
    2. Read the airport layout from standard input.
    3. Generate the cost matrix.
    4. Finally, start the game.

    You are allowed to change the structure of this function if you wish, but you must ensure that everything works correctly.
    The skeleton acts as a guide to help you get started. Use it to find hints and tips on how to complete the project.
    """
    # Read and store the command line arguments.
    # You may change the way in which the command line arguments are read and stored, as long as everything works correctly.
    # In the following line, the function `read_command_line_args()` is called and the variables `game_mode` and `graphics_mode` are set accordingly.
    game_mode, graphics_mode = read_command_line_args()

    # Print the command line arguments.
    print_command_line_args(game_mode, graphics_mode)

    # TODO: Read and store the contents of the input file redirected to standard input in an appropriate fashion.
    # The input file contains the airport layout. Refer to the project specification for more details.
    # Remember to do any necessary error checking.

    # TODO: Generate the cost matrix by calling the function `generate_cost_matrix()`.
    # The function `generate_cost_matrix()` takes one parameter, which is a two-dimenstional list of airport coordinates. The 2D list is a 10x2 matrix, where each row represents the `x` and `y` coordinates of an airport, in that order. You must perform validation on the input file to ensure that the input file contains the correct number of airports and that the coordinates are valid. What would happen if a the person who created the input file suddenly became sleepy and decided to enter `Q` in the airport layout section of the input file?
    # The airport layout should be read in the previous step and stored in an appropriate variable.

    # TODO: Start an instance of the game.
    # This is were the actual gameplay takes place. Read the project specification for more details.
    # Remember, players may start a new game after the previous game has ended. We have not provided any code to handle this, but you should implement the functionality to restart a game, as many times as the user would like to play.
    # NOTE: a new game does not mean that the program is restarted. The program should continue to run, but the game should be reset to its initial state and play the game as if it was the first time the game was played.
    # NOTE: When a new game is started, use the same command line arguments, airport coordinates, initial airport suitcase number assignments, and cost matrix as the previous game.
    game()

def game():
    """
    This is an example of a function that you may use to start the game.
    You do not have to use this function. If you do, you should change it appropriately.
    """
    # TODO: First we want the players to select their starting positions and flip their first suitcases.

    # TODO: Next, we want to loop through the game rounds. One round consists of two turns, one for each player.
    # For example, the following `while` loop will loop until the global variable game_over is set to `True`, indicating that the game has ended.
    while not game_over:
        # TODO: play the game. You will need to change the contents of this while loop
        stdio.writeln('Game is running...')
        end_game()
        # This is an example of how to end the game. You should change this appropriately.
        # The `end_game()` function sets the global variable game_over to `True`, indicating that the game has ended.
    stdio.writeln('Game has ended.') # TODO: Remove this. We only need to print information about winning/ losing. Besides, you must use the messages defined in the constants section.
    # If you run the skeleton program as is, you will see the above message printed to standard output.

###############################################################################################
##################################### Printing functions ######################################
###############################################################################################
# The following functions are used to print the game state to standard output.
# DO NOT MODIFY THESE FUNCTIONS.
# We expect a very specific output format since we will be using an automated marking script.
# During marking, we compare the output of your program with the expected output.
# If the output does not match, your program will be marked as incorrect.
###############################################################################################

def termination(msg):
    """
    Terminate the program and display an appropriate message.

    This function should be called when user input should cause the program to terminate.
    This is the only function that should be used to terminate the program and print the associated termination message.

    Parameters
    ----------
    msg
        The message to be displayed to the user before terminating. This message should correspond to one of the constants defined at the top of the program. Ensure that you specify the correct constant when calling this function, according to the error that has occurred. See the project specification for more details.
    """
    stdio.writef('Termination: %s', str(msg))
    sys.exit(0)


def print_obstacle_disks(can_play_disk_array):
    """
    Print the obstacle disks available to the given player.

    NOTE: The Red disk should only be displayed here after the player has asked their opponent to leave their airport, and the opponent has refused to leave -- assuming they have not used it previously. In the case where it is possible to display the red disk, no other obstacle disks should be displayed, even if they have not been played yet. In the case where the player did not ask their opponent to leave their airport, only the non-red obstacle disks should be displayed (noting that, for the first hand-in, the non-red obstacle disks will never be available).

    Parameters
    ----------
    player
        the index of the current player. `0` for `P1` and `1` for `P2`.
    can_play_disk_array
        an array of six Booleans (`True` or `False`) corresponding to whether or not the disk at that index can be played or not.
        NOTE: the order of the array elements are important: `[can_play_red, can_play_green, can_play_yellow, can_play_cyan, can_play_black, can_play_magenta]`. When it is possible for can_play_red to be `True`, the others should be false, even if the player has not played any of the non-red disks yet. Similarly, when the other values can possibly be `True`, the red disk should not be `True`, even if the player has not played their red obstacle disk yet since the red obstacle disk can only and is the only obstacle disk that can played immediately after the current player has asked their opponent to leave their airport, and the opponent has refused to do so.
    """
    if game_over: return
    middle = ' x%11sx '
    outer1 = '     x x x     '
    outer2 = '  x         x  '
    colour_characters_array = ['R', 'G', 'Y', 'C', 'B', 'M']
    for row in range(7):
        for disk in range(len(colour_characters_array)):
            if disk == 0: stdio.write('\t')
            if not can_play_disk_array[disk]: continue
            if row == 0 or row == 6:
                stdio.write(outer1)
            elif row == 1 or row == 5:
                stdio.write(outer2)
            elif row == 2 or row == 4:
                stdio.writef(middle, ' ')
            else:
                stdio.writef(middle, colour_characters_array[disk].center(10))
        stdio.writeln()

def black_disk_print(suitcase_numbers_array, collected_array):
    """
    This function reveals the numbers behind the suitcases at their current airport. It also shows which of these suitcases have already been collected by either player.

    This function must only be called after a player correctly plays their black card. ''Correcly'', here, implies that you still have to perform logical checks to see whether the player is allowed to play their black card before calling this function.

    Parameters
    ----------
    suitcase_numbers_array
        A one-dimensional array with four elements. The elements are integer values -- the (usually hidden) numbers of each corresponding suitcase index. The array must contain four integer values, each between 1 and 10. These are the numbers the player needs to collect in sequence. The index of each number in the array corresponds to the index of the corresponding suitcase at the aiport.
    collected_array
        A one-dimensional array with four elements. The elements are boolean values, indicating whether or not a suitcase has already been collected by either player. If a suitcase at index `x` has been collected by either player, the value of `collected_array[x]` will be `True`. In contrast, if the suitcase at index `x` has not yet been collected, the value of `collected_array[x]` will be `False`.
        This variable is used to decide whether a cross should be drawn through the card. If the suitcase has been collected, a cross is drawn through the card and the number corresponding to that suitcase is displayed in the middle of the card. If the suitcase has not been collected, the number is displayed in the middle of the card, but no cross is drawn through the card.
        The index of each Boolean in the array corresponds to the index of the corresponding suitcase at the aiport.
    """
    if game_over: return
    space = ' '*5
    card_edge = '%5s' + CORN + LINE * 7 + CORN
    inside = space + WALL + '%-7s' + WALL
    empty = ' '*7
    uncollected = [empty, empty, ' ' * 3, empty, empty]
    taken1 = 'x     x'
    taken2 = ' x   x '
    collected = [taken1, taken2, ' ' * 3, taken2, taken1]

    for card_pos in range(SUITCASES_PER_AIRPORT):
        stdio.writef(card_edge, space)
    stdio.writeln()

    for i in range(5):
        for card_pos in range(SUITCASES_PER_AIRPORT):
            val = str(suitcase_numbers_array[card_pos]) if i == 2 else ''
            if collected_array[card_pos]:
                stdio.writef(inside, collected[i] + val)
            else:
                stdio.writef(inside, uncollected[i] + val)
        stdio.writeln()

    for card_pos in range(SUITCASES_PER_AIRPORT):
        stdio.writef(card_edge, str(card_pos+1) + '. ')
    stdio.writeln('\n')

def print_single_suitcase_number(number):
    """
    Print an image of a single suitcase with the given number. This is used to reveal the number behind a suitcase when a player flips it.

    Do not use this function to display suitcase numbers when a black obstacle disk is played. Use the `black_disk_print()` function instead.
    This function only prints the number behind a single suitcase. You must perform the logical checks involved in flipping a suitcase before you call this function to print the number behind that suitcase.

    Parameters
    ----------
    number
        The number behind the suitcase that has just been flipped. This must be an integer between 1 and 10, both inclusive.
    """
    if game_over: return
    card_edge = CORN + LINE * 7 + CORN
    middle = WALL + '%7s' + WALL + '\n'
    blank = ' '*7
    card_number = str(number).center(7)
    stdio.writeln(card_edge)
    for i in range(5):
        stdio.writef(middle, card_number if i == 2 else blank)
    stdio.writeln(card_edge + '\n')

def print_airport_suitcases(suitcase_numbers_array, collected_array, allowed_to_flip_array):
    """
    Print the four cards representing the suitcases at an airport. This function is only used for printing purposes only -- it does not perform logic checking. You must ensure that the values you give as arguments to this function are correct before you call this function.

    DO NOT MODIFY the contents of this function. If you do, you risk changing the way the suitcases are printed. That would be a disaster.

    The parameters of this function will give you a good idea of what you should keep track of. Each parameter is a one dimensional array with four entries. Each entry corresponds to information about the suitcase at that index. Make sure that the elements of each array correspond with the index of the suitcases at the current airport. For example, the first card at an airport has an index of 0. For each parameter, the array entry at index 0 must correspond to the information about the first suitcase. See the argument explanations below for more details.

    Parameters
    ----------
    suitcase_numbers_array
        A one-dimensional array with four elements. The elements are integer values -- the (usually hidden) numbers of each corresponding suitcase index. The array must contain four integer values, each between 1 and 10. These are the numbers the player needs to collect in sequence. This function uses the `suitcase_numbers_array` to determine whether or which numbers to print on the cards. If the suitcase has not yet been collected, the number is not printed. If the card was already collected by either player, the number is printed, but the card will have a cross drawn through it. See the explanation on the parameter `collected_array` for more details.

        For example, let's say the third suitcase at this airport corresponds to the number 7. If we want to know the number of the suitcase at index 2 (the THIRD suitcase at this airport), we can use the following code:

        >>> suitcase3_number = suitcase_numbers_array[2]
        >>> stdio.writeln(suitcase3_number)
        7
    collected_array
        A one-dimensional array with four elements. The elements are boolean values, indicating whether or not a suitcase has already been collected by either player. If a suitcase at index `x` has been collected by either player, the value of `collected_array[x]` will be `True`. In contrast, if the suitcase at index `x` has not yet been collected, the value of `collected_array[x]` will be `False`.
        This variable is used to decide whether a cross should be drawn through the card. If the card has been collected, a cross is drawn through the card and the number corresponding to that card is displayed in the middle of the cross.
    allowed_to_flip_array
        A one-dimensional array with four elements. The elements are boolean values, indicating whether or not a suitcase can be flipped by the current player because they might have already flipped that card during their current visit to their airport. If a player flips a card, they cannot flip it again until the flip restriction is lifted. This is to avoid players simply flipping cards forever. Note: this variable only checks the flip restriction. It does not take into account whether a card has already been collected, for example.
        If the current player has not yet flipped the suitcase at position `x` since the last reset of their flip restrtiction, the value of `allowed_to_flip_array[x]` will be `True`. In contrast, if the current player has already flipped the suitcase at position `x` during their visit to this airport (and the flip restriction has not yet been reset), the value of `allowed_to_flip_array[x]` will be False.
        If `allowed_to_flip_array[x]` is `True`, the suitcase at position `x` will not be displayed to the player. It will simply not be printed. Make sure the flip restriction does not prevent already collected cards from being printed.
    """
    if game_over: return
    space = ' '*5
    card_edge = '%5s' + CORN + LINE * 7 + CORN
    inside = space + WALL + '%-7s' + WALL
    empty = ' '*7
    unflipped = ['   _   ', ' xX Xx ', ' x   x ', ' xXXXx ', empty]
    taken1 = 'x     x'
    taken2 = ' x   x '
    collected = [taken1, taken2, ' ' * 3, taken2, taken1]
    stdio.writeln('Suitcases at the current airport:')

    for card_pos in range(SUITCASES_PER_AIRPORT):
        if allowed_to_flip_array[card_pos]:
            stdio.writef(card_edge, space)
    stdio.writeln()

    for i in range(5):
        for card_pos in range(SUITCASES_PER_AIRPORT):
            if not allowed_to_flip_array[card_pos]:
                continue
            if collected_array[card_pos]:
                val = str(suitcase_numbers_array[card_pos]) if i == 2 else ''
                stdio.writef(inside, collected[i] + val)
            else:
                stdio.writef(inside, unflipped[i])
        stdio.writeln()

    for card_pos in range(SUITCASES_PER_AIRPORT):
        if allowed_to_flip_array[card_pos]:
            stdio.writef(card_edge, str(card_pos+1) + '. ')
    stdio.writeln('\n')

def write_center(text, length=5):
    stdio.writef(' %s |', text.center(length))

def print_cost_matrix(flight_cost_matrix, cur_player, cur_player_wallet, cur_round_number):
    """
    Print the given cost matrix to standard output. DO NOT THE CONTENTS MODIFY THIS FUNCTION!

    Modifying this function may affect how the cost matrix is printed. Since we mark via differencing, you may lose points if your cost matrix is not displayed as we expect it to be.

    The cost matrix is printed in a table format, with a header providing information about the game state.
    The header contains the round number on the left, the player number in the middle, and the player's balance on the right.
    Header information must be passed as arguments to this function.

    Parameters
    ----------
    flight_cost_matrix
        The cost matrix to be printed. The parameter `flight_cost_matrix` must be given in the expected format. The contents of `flight_cost_matrix` should be equal to that which was previously obtained by calling the `generate_cost_matrix()` function. Make sure you correctly applied the `generate_cost_matrix()` function.
    cur_player
        The index of the current player (0 for P1, 1 for P2). The parameter cur_player must be an integer between 0 and 1.
    cur_player_wallet
        The balance of the current player. The parameter cur_player_wallet must be a float.
    cur_round_number
        The current round number. The parameter cur_round_number must be an integer, indicating the current round number.
    """
    if game_over: return
    header_line = WALL + ' %-28s%s%28s ' + WALL
    stdio.writeln(CORN + LINE * (87) + CORN)
    round_info = f'Round {cur_round_number}'
    player_info = f'Player {cur_player + 1}'.center(29)
    wallet_info = f'Balance: R{float(cur_player_wallet):.2f}'
    stdio.writef(header_line, round_info, player_info, wallet_info)
    edge = '\n' + CORN + (LINE * 7 + CORN) * 11
    stdio.writeln(edge)
    stdio.writef('%s', WALL)
    write_center(' ', length=5)
    for col in range(AIRPORTS):
        write_center(int_to_char(col))
    stdio.writeln(edge)
    for row in range(AIRPORTS):
        stdio.writef('%s', WALL)
        write_center(int_to_char(row), length=5)
        for col in range(AIRPORTS):
            write_center(f'{float(flight_cost_matrix[row][col]):.2f}')
        stdio.writeln()
    stdio.writeln(edge[1:] + '\n')

def print_suitcase_grid(p1_last_suitecase, p2_last_suitecase):
    """
    Print the grid of suitcases to standard output indicating which suitcases each player has already collected.

    The grid is a `2 x 5` grid, where each cell represents a number between 1 and 10. The grid will show the players' last suitcase numbers, or a blank space if they have not yet collected a suitcase. Thus, if player 1 has collected all suitcases up to and including 5, the grid indicate that player one is currently on the cell with 5. Similarly, if player 2 has collected all suitcases up to and including 8, the grid will indicate that player 2 is currently on the cell with 8. All other cells will be blank. If a player has not yet, the value of the corresponding argument should be 0.

    Please make sure you give the correct values of each player's last suitcase number as the arguments of this function. If you do not, the grid will not be printed correctly.

    Do not modify the contents of this function.

    Parameters
    ----------
    p1_last_suitecase
        The number corresponding to the last suitcase collected by player 1. This must be an integer between 0 and 10.
    p2_last_suitecase
        The number corresponding to the last suitcase collected by player 2. This must be an integer between 0 and 10.
    """
    header = 'Player Suitcases'
    generic_grid_print(header, p1_last_suitecase, p2_last_suitecase, True, False)

def print_airport_grid(p1_airport_id, p2_airport_id):
    """
    Print the airport grid to standard output. The airport grid displays the positions of the two players on the grid. The grid is a 2x5 grid, where each cell represents an airport. The grid will show the players' positions, or a blank space if they are not on that airport. Thus, if player 1 is on airport A, the grid will indicate that player one is currently on the cell with A. Similarly, if player 2 is on airport D, the grid will indicate that player 2 is currently on the cell with D. All other cells will be blank.

    Please note: the parameters `p1_airport_id` and `p2_airport_id` expect integer values that correspond to the INDEX of the associated airport. Thus, if player `1` is on airport `A`, the value of `p1_airport_id` should be `0`. If player `2` is on airport `D`, the value of `p2_airport_id` should be `3`. If a player is not currently at an airport, the value of the corresponding argument should be an integer that does NOT fall between `0` and `9`, both inclusive. For example, a value of `-1` is acceptable and indicates that the player is not currently at an airport.

    Furthermore, P1 and P2 are never allowed to be on the same airport at the same time. If they are, you have made a mistake somewhere.

    Do not modify the contents of this function.

    Parameters
    ----------
    p1_airport_id
        The index of the airport that player 1 is currently on. This must be an integer.
    p2_airport_id
        The index of the airport that player 2 is currently on. This must be an integer.
    """
    header = 'Airplane Locations'
    generic_grid_print(header, p1_airport_id, p2_airport_id, False, True)

def generic_grid_print(header_text, p1_position, p2_position, seperate_players, use_letters):
    """
    This function controls the printing of the airport and suitcase grid. DO NOT MODIFY IT!

    This function is called by print_airport_grid and print_suitcase_grid. It is not intended to be called by the student.

    We mark your code based on the difference between the expected output and that of your implementation. If you modify this function, there is a large risk that you will modify how the grids are printed.
    """
    if game_over: return
    p1 = 'P1'
    p2 = 'P2'
    player_indicator = ' %2s'+ ' '*5 + '%2s ' + WALL
    centre_indicator = ' '*5 + '%-2s' + ' '*4 + WALL
    seperator = CORN + (LINE * 11 + CORN) * 5
    stdio.writeln(CORN + LINE * (12 * 5 - 1) + CORN)
    stdio.writef('%s%s%s\n', WALL, header_text.center(len(seperator) - 2), WALL)
    for row in range(2):
        stdio.writef('%s\n', seperator)
        for i in range(5):
            stdio.write(WALL)
            for col in range(5):
                cell = row * 5 + col
                if i == 2:
                    stdio.writef(centre_indicator, int_to_char(cell) if use_letters else cell + 1)
                elif seperate_players and i == 0:
                    stdio.writef(player_indicator, p1 if cell+1 == p1_position else ' ', p2 if cell+1 == p2_position else ' ')
                elif seperate_players and i == 4:
                    stdio.writef(player_indicator, p2 if cell+1 == p2_position else ' ', p1 if cell+1 == p1_position else ' ')
                elif cell == p1_position and (i == 0 or i == 4):
                    stdio.writef(player_indicator, p1, p1)
                elif cell == p2_position and (i == 0 or i == 4):
                    stdio.writef(player_indicator, p2, p2)
                else:
                    stdio.writef(centre_indicator, ' ')
            stdio.write('\n')
    stdio.writef('%s\n\n', seperator)

def print_command_line_args(game_mode_val, graphics_mode_val):
    """
    Prints the command line arguments to standard output.

    Call this after the command line arguments have been parsed.

    Parameters
    ----------
    game_mode_val
        The value of the game mode command line argument. (0, 1, or 2)
    graphics_mode_val
        The value of the graphics mode command line argument. (0 or 1)
    """
    stdio.writef('Game mode: %d\nGraphics mode: %d\n\n', game_mode_val, graphics_mode_val)

###############################################################################################
##################################### The main function #######################################
###############################################################################################
# The following line is used to run the program.
# It basically says: "If this file is being run as a program, start here and call the function `runner()`."
# It should appear at the end of your program, after all of the functions have been defined.
# This ensures that all of your functions and variables are in scope when the program is run.
if __name__ == '__main__':
    runner()
