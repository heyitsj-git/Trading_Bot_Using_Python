import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger

setup_logger()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:

    validate_order(args.type, args.price)

    client = get_client()

    response = place_order(
        client,
        args.symbol.upper(),
        args.side.upper(),
        args.type.upper(),
        args.quantity,
        args.price
    )

    print("\nOrder Success")
    print("-------------------")
    print(f"Order ID: {response['orderId']}")
    print(f"Status: {response['status']}")
    print(f"Executed Qty: {response['executedQty']}")

except Exception as e:
    print(f"Error: {e}")