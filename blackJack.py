import random

class GameClass:

    # Dunder method to initialize the game with the list of cards
    def __init__(self):
        self.cardList = [2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9,
                        'J','Q','K','A','J','Q','K','A','J','Q','K','A','J','Q','K','A']
        self.playerHand = []
        self.dealerHand = []
        self.playerIn = True
        self.dealerIn = True
        self.gameLoop()

    # Deal the cards
    def cardDealer(self, player):
        self.card = random.choice(self.cardList) # choose a random card
        player.append(self.card) # add the randomly drawn card to the players deck
        self.cardList.remove(self.card)

    # Calculate the total of the players hand
    def handTotal(self, player):
        self.total = 0
        faceCards = ['J', 'K', 'Q']
        for card in player:
            if card in faceCards:
                self.total += 10
            elif card in range(1,11):
                self.total += card
            else:
                if self.total >= 11:
                    self.total += 1
                else:
                    self.total += 11
        return self.total

    # Reveal the dealers hand
    def showDealerCards(self):
        if len(self.dealerHand) == 2:
            return self.dealerHand[0]
        elif len(self.dealerHand) > 2:
            return self.dealerHand[0:2]

    # Find the winner of the game
    def checkWinner(self):
        if self.handTotal(self.playerHand) == 21:
            print(f'\nYou have got a total of {self.handTotal(self.playerHand)} and the dealer had {self.handTotal(self.dealerHand)}.')
            print(f'\nYou got blackjack!! You win!')
        elif self.handTotal(self.dealerHand) == 21:
            print(f'\nYou have got a total of {self.handTotal(self.playerHand)} and the dealer had {self.handTotal(self.dealerHand)}.')
            print(f'\nThe dealer got blackjack!! You lose!')
        elif self.handTotal(self.dealerHand) > 21 or self.handTotal(self.playerHand) > 21:
            if self.handTotal(self.dealerHand) > 21:
                print(f'\nYou have got a total of {self.handTotal(self.playerHand)} and the dealer had {self.handTotal(self.dealerHand)}.')
                print(f'\nYou win!')
            elif self.handTotal(self.playerHand) > 21:
                print(f'\nYou have BUSTED with a total of {self.handTotal(self.playerHand)} and the dealer had {self.handTotal(self.dealerHand)}.')
                print(f'\nYou Lose!')
        elif self.handTotal(self.playerHand) > self.handTotal(self.dealerHand):
            print(f'\nYou have got a total of {self.handTotal(self.playerHand)} and the dealer had {self.handTotal(self.dealerHand)}.')
            print(f'\nYou win!')
        elif self.handTotal(self.playerHand) < self.handTotal(self.dealerHand):
            print(f'\nYou have got a total of {self.handTotal(self.playerHand)} and the dealer had {self.handTotal(self.dealerHand)}.')
            print(f'\nYou Lose!')
        elif self.handTotal(self.playerHand) == self.handTotal(self.dealerHand):
            print(f'\nYou have got a total of {self.handTotal(self.playerHand)} and the dealer had {self.handTotal(self.dealerHand)}.')
            print(f'\nYou TIED!')
        else:
            print(f'\nYou have got a total of {self.handTotal(self.playerHand)} and the dealer had {self.handTotal(self.dealerHand)}.')
            print(f'\nYou both Lose!')

    # Game Loop
    def gameLoop(self):       
        for _ in range(2):
            self.cardDealer(self.playerHand)
            self.cardDealer(self.dealerHand)

        while self.playerIn or self.dealerIn:
            print(f'Dealer had {self.showDealerCards()} and X(hidden card)')
            print(f'You have {self.playerHand} for a total of {self.handTotal(self.playerHand)}')

            # Stay or Hit logic for Player
            if self.playerIn:
                decision = int(input("Choose 1: Stay, Choose 2: Hit\n"))
                if decision == 1:
                    self.playerIn = False
                else:
                    self.cardDealer(self.playerHand)

            # Stay or Hit logic for Dealer
            if self.handTotal(self.dealerHand) > 16:
                self.dealerIn = False
            else:
                self.cardDealer(self.dealerHand)

            # Logic for busting
            if self.handTotal(self.playerHand) >= 21:
                break
            elif self.handTotal(self.dealerHand) >= 21:
                break
        self.checkWinner()


instance = GameClass()
