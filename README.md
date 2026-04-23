# 🚀 Binance Futures Trading Bot (Python CLI)

A clean, modular, and production-inspired Python trading bot built for **Binance Futures Testnet (USDT-M)**.

This project demonstrates how to place **MARKET** and **LIMIT** orders through a structured command-line application while maintaining strong engineering practices such as:

* Clean architecture
* API abstraction
* Input validation
* Logging
* Error handling
* Reusable code structure
* Binance Futures Testnet integration

---

# ✨ Project Overview

This trading bot was built as a lightweight yet scalable foundation for automated trading systems.

Instead of creating a single script, the project follows a modular design pattern that separates:

* CLI logic
* Binance API communication
* Validation rules
* Logging
* Order execution

This makes the codebase easier to maintain, extend, debug, and scale.

---

# 📁 Project Structure

```bash
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py              # Binance Futures client wrapper
│   ├── orders.py              # Order placement logic
│   ├── validators.py          # CLI input validation
│   ├── logging_config.py      # Logger setup
│
├── logs/
│   └── bot.log                # API logs
│
├── cli.py                     # Command-line entry point
├── requirements.txt
├── README.md
├── .env
```

---

# ⚡ Features

### Core Requirements Implemented

✅ Binance Futures Testnet Integration
✅ MARKET Orders
✅ LIMIT Orders
✅ BUY & SELL Support
✅ CLI-based User Input
✅ Structured Logging
✅ Exception Handling
✅ Modular Codebase
✅ Request/Response Tracking
✅ Validation Layer

---

# 🛠 Tech Stack

* Python 3.x
* Binance Futures Testnet API
* python-binance
* argparse
* dotenv
* logging

---

# 🔐 Binance Testnet Setup

### Step 1: Open Futures Testnet

Visit:

```text
https://testnet.binancefuture.com
```

### Step 2: Generate API Keys

1. Login to Binance Futures Testnet
2. Navigate to API Key section
3. Generate HMAC API credentials
4. Copy API Key and Secret Key

---

# 🔑 Environment Variables

Create a `.env` file in the root directory.

```env
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/trading_bot.git
```

Move into project directory:

```bash
cd trading_bot
```

Create virtual environment:

```bash
py -3.14 -m venv venv
```

Activate virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running The Bot

## MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

## LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
```

---

# 🧠 CLI Arguments

| Argument     | Description                     |
| ------------ | ------------------------------- |
| `--symbol`   | Trading pair (example: BTCUSDT) |
| `--side`     | BUY or SELL                     |
| `--type`     | MARKET or LIMIT                 |
| `--quantity` | Quantity to trade               |
| `--price`    | Required only for LIMIT orders  |

---

# 📄 Example Output

```bash
Order Success
-------------------
Order ID: 5487123
Status: FILLED
Executed Qty: 0.001
```

---

# 📜 Logging

Every request, response, and exception is logged automatically.

Logs are stored in:

```text
logs/bot.log
```

The logger captures:

* Order payloads
* Binance API responses
* Validation failures
* Network/API errors
* Runtime exceptions

---

# 🧱 Architecture Design

The project follows a separation-of-concerns architecture.

### CLI Layer

Handles user input and interaction.

### Validation Layer

Ensures required parameters are valid before execution.

### API Layer

Handles Binance Futures communication.

### Order Layer

Builds and executes trading requests.

### Logging Layer

Tracks all activity for debugging and auditing.

---

# ⚠️ Error Handling

This bot includes exception handling for:

* Missing parameters
* Invalid order type
* LIMIT order without price
* API authentication errors
* Binance request failures
* Network interruption
* Invalid quantity or symbol

---

# 🧪 Sample Tested Cases

| Test Case           | Result      |
| ------------------- | ----------- |
| BUY MARKET          | ✅ Success   |
| SELL MARKET         | ✅ Success   |
| BUY LIMIT           | ✅ Success   |
| SELL LIMIT          | ✅ Success   |
| Invalid CLI Input   | ✅ Handled   |
| Missing LIMIT Price | ✅ Prevented |

---

# 💡 Design Philosophy

This project was intentionally designed beyond a simple assignment solution.

The goal was to build a clean, maintainable trading application that resembles a real-world backend workflow.

The structure enables future upgrades such as:

* Stop-Loss Orders
* Take Profit Orders
* Position Tracking
* Risk Management
* Strategy Engine
* Web Dashboard
* Live Trading Support

---

# 🚀 Future Improvements

Potential upgrades:

* Interactive CLI UX
* Real-time websocket price feed
* Position monitoring
* Multi-symbol support
* Trade history storage
* Docker deployment
* Unit testing

---

# 📌 Assumptions

* Binance Futures Testnet account is active
* API keys are valid
* Internet connection is available
* Symbol exists on Binance Futures

---

# 👨‍💻 Author

Built with Python and Binance Futures Testnet.

Focused on clean architecture, modular design, and developer-friendly implementation.

---

# ⭐ Why This Project Stands Out

Unlike a single-script implementation, this bot follows a scalable engineering approach.

It demonstrates:

* Code organization
* API integration
* Logging practices
* Validation design
* CLI development
* Error resilience

This creates a strong foundation for production-grade trading systems.

---

# 📬 Submission Contents

* Source Code
* README.md
* requirements.txt
* Log Files
* Binance Futures Testnet Integration
* CLI Order Placement

---

# 🔥 Final Note

This project is not just about placing orders.

It demonstrates how to engineer a reliable trading workflow with clean code principles and reusable architecture.

A small trading bot today can become a full trading engine tomorrow.

---

### Built for Binance Futures Testnet • Python • CLI • Trading Automation
