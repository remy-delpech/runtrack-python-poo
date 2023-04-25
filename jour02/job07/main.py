import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_value(self):
        if self.value in ['J', 'Q', 'K']:
            return 10
        elif self.value == 'A':
            return 11
        else:
            return int(self.value)

    def __str__(self):
        return f"{self.value}{self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(value, suit) for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
                      for suit in ['♠', '♥', '♦', '♣']]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

class Player:
    def __init__(self):
        self.cards = []

    def get_total_points(self):
        total_points = sum(card.get_value() for card in self.cards)
        num_aces = sum(1 for card in self.cards if card.value == 'A')

        while num_aces > 0 and total_points > 21:
            total_points -= 10
            num_aces -= 1

        return total_points

class Dealer:
    def __init__(self):
        self.cards = []

    def play(self, deck):
        while self.get_total_points() < 17:
            self.cards.append(deck.draw_card())

    def get_total_points(self):
        total_points = sum(card.get_value() for card in self.cards)
        num_aces = sum(1 for card in self.cards if card.value == 'A')

        while num_aces > 0 and total_points > 21:
            total_points -= 10
            num_aces -= 1

        return total_points

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        self.deck.shuffle()

    def deal_initial_cards(self):
        self.player.cards.append(self.deck.draw_card())
        self.player.cards.append(self.deck.draw_card())
        self.dealer.cards.append(self.deck.draw_card())
        self.dealer.cards.append(self.deck.draw_card())

    def print_game_status(self, show_dealer_card=False):
        # Affiche les cartes du joueur et le total de points
        print("Player's cards:")
        for card in self.player.cards:
            print(f"\t{card}")
        print(f"Player's total points: {self.player.get_total_points()}")

        if show_dealer_card:
            # Si l'argument est True, affiche toutes les cartes du croupier et son total de points
            print("Dealer's cards:")
            for card in self.dealer.cards:
                print(f"\t{card}")
            print(f"Dealer's total points: {self.dealer.get_total_points()}")
        else:
            # Sinon, n'affiche que la carte visible du croupier
            print(f"Dealer's visible card: {self.dealer.cards[0]}")

    def play(self):
        # Distribue les cartes initiales
        self.deal_initial_cards()
        # Affiche l'état actuel du jeu
        self.print_game_status()

        while True:
            # Demande au joueur s'il veut tirer une nouvelle carte ou s'arrêter
            decision = input("Do you want to hit or stand? (h/s)")

            if decision == 'h':
                # Si le joueur veut tirer une nouvelle carte, en tire une et l'ajoute à sa main
                self.player.cards.append(self.deck.draw_card())
                # Affiche l'état actuel du jeu
                self.print_game_status()

                if self.player.get_total_points() > 21:
                    # Si le joueur a dépassé 21 points, il a perdu
                    print("Bust! You lost!")
                    return
            else:
                # Si le joueur s'arrête, le croupier commence à jouer
                self.dealer.play(self.deck)
                # Affiche les cartes du croupier
                self.print_game_status(show_dealer_card=True)

                if self.dealer.get_total_points() > 21:
                    # Si le croupier a dépassé 21 points, le joueur a gagné
                    print("Dealer bust! You win!")
                    return

                if self.player.get_total_points() > self.dealer.get_total_points():
                    # Si le joueur a plus de points que le croupier, il a gagné
                    print("You win!")
                    return
                elif self.player.get_total_points() == self.dealer.get_total_points():
                    # Si le joueur et le croupier ont le même nombre de points, c'est une égalité
                    print("Push! It's a tie.")
                    return
                else:
                    # Sinon, le joueur a perdu
                    print("You lost!")
                    return
                

# Crée une instance de la classe Blackjack
game = Blackjack()

# Lance la partie
game.play()
    
