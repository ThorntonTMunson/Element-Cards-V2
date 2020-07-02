# def import_cards(card_pics):
#     """Function creates a window and load in the cards
#
#     Card type is the cards element:
#         Each element has a strong vs and weak vs respectively
#            ex: water weak to electric, strong vs fire
#         combination = two or more elements
#         artificial = artifacts
#         celestial = star
#         void = void
#         holy = light
#         shadow = dark
#
#     normal: no attributes beyond element.
#     special: has an extra ability
#     mystic: has an ability that is not usually associated with the cards element
#     fast: essentially is allowed to deal it's damage first (MTG first strike)
#     tank: bonus health when face against a weak vs (ex: fire vs water)
#     resist: reduces damage from weak against
#     """
#     card_type = ["water", "fire", "wind", "lightning", "stone", "hoy", "shadow", "artificial", "celestial", "void"]
#     special = ["normal", "special", "mystic", "fast", "tank", ]
#
#     if tkinter.TkVersion >= 8.6:
#         extention = "png"
#     else:
#         extention = "ppm"
#     # for each card type retrieve the image of the card
#     for type in types:
#         name = "cards/{}".format(str(type), card_type, extention)
#         image = tkinter.PhotoImage(file=name)
#         card_pics.append(type, image)





