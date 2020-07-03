import random

try:
    import tkinter
except ImportError:  # python2
    import Tkinter as tkinter

""" card images will need to be scaled down in order to fit everything
    frames have their own independent grid from the existing window
    row 0 in main window has comp name and health, comp deck, comp hand, and comp discard pile
    row 1 in main window has comp card play field
    row 3 in main window has player play field
    row 4 in main window has player name and health, player discard, player hand, and player deck
    row 5 in main window had buttons to allow player to draw cards
    needs more refinement, not sure how to do it yet but will get there after setting everything up"""


def load_cards(card_pics):
    cards = ["water", "fire", "wind", "lightning", "stone", "holy", "shadow", "artificial", "celestial", "void"]
    # card_back = "back"
    # special = ["normal", "special", "mystic", "fast", "tank", ]

    if tkinter.TkVersion >= 8.6:
        extension = "png"
    else:
        extension = "ppm"
    # back = "cards/{}.{}".format(str(card_back), extension)
    # card_rear = tkinter.PhotoImage(file=back)
    # for each card type retrieve the image of the card
    for card_type in cards:
        name = "cards/{}.{}".format(str(card_type), extension)
        card_front = tkinter.PhotoImage(file=name)
        card_pics.append((card_type, card_front))


def card_backing(frame):
    card_back = ["back"]
    # card_back = "back"

    if tkinter.TkVersion >= 8.6:
        extension = "png"
    else:
        extension = "ppm"
    back = "cards/{}.{}".format(str(card_back), extension)
    frame = tkinter.PhotoImage(file=back)
    # frame = tkinter.PhotoImage()
    frame.append((card_back))
    # global card_back
    load = tkinter.Image.open("back.png")
    # add image to the label and display the label
    tkinter.Label(frame, image=card_back, relief="raised").pack(side="left")
    # card_back.append(load_deck_pic(comp_deck_frame)
    card_backing(comp_deck_frame)


def draw_card(frame):
    #  get the next card off top of deck
    pop_card = deck.pop(0)
    # put card back (on the bottom)
    deck.append(pop_card)
    # shuffle after use
    # add image to a label and display the label
    tkinter.Label(frame, image=pop_card[1], relief="raised").pack(side="left")
    return pop_card


def initial_draw():
    player_draw()
    comp_draw()


def comp_draw():
    comp_hand.append(draw_card(comp_player_frame))


def comp_health():
    health = 10



def player_draw():
    user_hand.append(draw_card(user_player_frame))

    user_player_hp = 10


def new_match():
    global comp_player_frame
    global user_player_frame


def shuffle():
    random.shuffle(deck)


mainWindow = tkinter.Tk()
# set up screen and frames for the player and opponent
mainWindow.title("Element Cards")
mainWindow.geometry("1200x700")
mainWindow.configure(background="gray")
# win condition not implemented yet, but here for reference anyways
# winner = tkinter.StringVar()
# result = tkinter.Label(mainWindow, textvariable=winner)
# result.grid(row=0, column=0, columnspan=3)
# calls the main loop to show screen until user closes it
##########################################################
# main window row 0
# create a frame within the window to hold the comp health label place holder
comp_health_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="bisque")
# set base parameters for the frame made above.
comp_health_frame.grid(row=0, column=0, sticky="ew", columnspan=1, rowspan=1)
# create a label to hold the comp title later will become user name as an enemy name
tkinter.Label(comp_health_frame, text="Enemy Health", background="bisque", fg="black").grid(row=0, column=0)
# create a label to hold the comp health value and place within the grid of comp_health_frame
tkinter.Label(comp_health_frame, textvariable=comp_health, background="bisque", fg="black").grid(row=1, column=0)
# comp_health_frame = tkinter.Frame(mainWindow, width=400, height=400, bg="bisque")
# create a frame within the window to hold the comp deck image place holder
comp_deck_frame = tkinter.Frame(mainWindow, relief="raised", borderwidth=1, background="bisque")
comp_deck_frame.grid(row=0, column=1, sticky="ew", columnspan=1, rowspan=1)
# card backing to the deck frame
comp_deck_frame = tkinter.Frame(comp_deck_frame, bg="bisque")
# frame for comp hand
comp_hand_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="bisque")
comp_hand_frame.grid(row=0, column=2, sticky="ew", columnspan=1, rowspan=5)

# draws a card to comp player hand through the comp draw button
comp_player_frame = tkinter.Frame(comp_hand_frame, background="bisque")
comp_player_frame.grid(row=0, column=1, sticky="nsew", rowspan=1)
# frame for comp discard pile
comp_dis_pile = tkinter.Frame(mainWindow, relief="sunken", borderwidth=3, background="bisque")
comp_dis_pile.grid(row=0, column=3, sticky="e", columnspan=1, rowspan=1)
#########################################################
# main window row 1
comp_player_field = tkinter.Frame(mainWindow, relief="raised", borderwidth=5, background="magenta")
comp_player_frame.grid(row=1, column=0, sticky="ew", rowspan=5)
########################################################
# main window row 3

#######################################################
# main window row 4
# get everything sorted for the comp set up and it's pretty much copypasta with a renaming of the variables
# create a frame for player name and health
player_health_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="yellow")
# set base parameters of frame items below are within the player_health_frame
player_health_frame.grid(row=1, column=0, sticky="ew", columnspan=1, rowspan=1)
# create a label to hold the player name
tkinter.Label(player_health_frame, text="Player Health", background="yellow", fg="black").grid(row=1, column=0)
# create a label to hold the player health value
tkinter.Label(player_health_frame, textvariable=player_health_frame, background="brown", fg="blue").grid(row=2, column=0)
# draw a card for player via the player draw button
user_player_frame = tkinter.Frame(comp_deck_frame, background="green")
user_player_frame.grid(row=3, column=1, sticky="ew", rowspan=2)

# for testing purposes to make sure things line ups do the copypasta early
# draw cards into the user hand window
user_hand_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="blue")
user_hand_frame.grid(row=4, column=2, sticky="ew", columnspan=1, rowspan=5)
# draws a card for the user player through the player draw button
user_player_frame = tkinter.Frame(user_hand_frame, background="magenta")
user_player_frame.grid(row=4, column=1, sticky="ew", rowspan=1)
########################################################
# main window row 5

# create frame for buttons within existing grid
########################################
button_frame = tkinter.Frame(mainWindow)
########################################
button_frame.grid(row=5, column=0, columnspan=3, sticky="w")

# create buttons and place in button frame
comp_button = tkinter.Button(button_frame, text="Comp Player", command=comp_draw)
comp_button.grid(row=0, column=0)

user_button = tkinter.Button(button_frame, text = "Player", command=player_draw)
user_button.grid(row=0, column=1)

new_match_button = tkinter.Button(button_frame, text="New Match", command=new_match)
new_match_button.grid(row=0, column=2)

shuffle_button = tkinter.Button(button_frame, text="Shuffle Cards", command=shuffle)
shuffle_button.grid(row=0, column=3)

cards = []
load_cards(cards)
print(cards)
deck = list(cards)
shuffle()

user_hand = []
comp_hand = []
tkinter.mainloop()