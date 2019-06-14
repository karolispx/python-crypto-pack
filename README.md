
# Python Crypto Pack

***This is my first ever Python script!  There's probably many better ways to do things, use this at your own risk!***

---

## Introduction

It becomes problematic when you have crypto-currencies in several different exchanges, it's hard to know how much you've lost/made. This is a simple tool that allows calculating profits/losses for your crypto-currencies. 

Script has been build having Arduino in mind, I've previously built something similar in GoLang and have written a small script for Arduino that made a call to the GoLang endpoint to calculate profits and display on an LCD screen. Cool little project!

---

## Getting Started

To get started, simply populate `coins` array with your coins and you're good to go!
```
coins = [
	{'id': 'bitcoin', 'invested': 1000, 'amount': 1, 'price_eur': 0, 'worth': 0, 'made_loss': 0},
	{'id': 'ethereum', 'invested': 3000, 'amount': 3, 'price_eur': 0, 'worth': 0, 'made_loss': 0}
]
```
- ***id*** - the ID of the coin, used to get coin info from https://coinmarketcap.com/
	- Full list available: https://api.coinmarketcap.com/v1/ticker/
- ***invested*** - amount of money invested, i.e. 4000
- ***amount*** - amount of coin, i.e. 10
- ***price_eur***, ***worth*** and ***made_loss*** - 0 by default, will be populated when data comes back from CMC

---

## Run It Locally
1. Clone this repository
2. Open the folder in your terminal
3. Run `python profits.py`
4. Open `http://127.0.0.1:8082/` in your browser to see your profits