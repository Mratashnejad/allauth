from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, 'home.html')


class Game:
    def __init__(self, name, rull, result):
        self.gamename = name
        self.gamerull = rull
        self.gameresult = result


class Cards:
    def __init__(self, number, suit, color):
        self.cardnumber = number
        self.cardsuit = suit
        self.cardcolor = color


class Dealer:
    def __init__(self, name, result):
        self.dealername = name
        self.dealerresult = result


class Player:
    def __init__(self, name, result):
        self.playername = name
        self.playerresult = result


def blackjack(self):
    Game.gamename = blackjack
    Game.gameresult = []
    Player.playername = "ali"
    Dealer.dealername = "valeria"
