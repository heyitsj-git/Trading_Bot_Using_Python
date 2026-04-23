# Binance Futures Trading Bot

## Setup

1. Create virtual environment
2. Install requirements
3. Add API keys in .env

## Run

Market Order:

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order:

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
