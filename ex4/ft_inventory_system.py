#!/usr/bin/env python3
import sys


# --- PARSING (NOT REQUIRED BY SUBJECT / MAY BREAK "AUTHORIZED" RULES) ---
# def parse(string: str) -> tuple[str, int] | None:
#     """Parse a 'key:value' argument into (key, value).
#
#     Return None and print an error if the format is invalid.
#     """
#     parts = string.split(":")
#
#     if len(parts) != 2:
#         print("Error: arguments must follow the format key:value")
#         return None
#
#     key = parts[0].strip()
#     if not key:
#         print("Error: missing key. Each pair must have a key")
#         return None
#
#     try:
#         value = int(parts[1].strip())
#     except ValueError:
#         print("Error: value must be a number")
#         return None
#
#     return key, value
# -----------------------------------------------------------------------


# --- ORIGINAL VERSION (requires parsing, not strictly allowed by subject) ---
#
# def data_input() -> dict[str, int]:
#     """Parse 'item:quantity' arguments and accumulate them into an inventory dict."""
#     inventory = {}
#
#     for arg in sys.argv[1:]:
#         result = parse(arg)
#
#         if result is None:
#             continue
#
#         key, value = result
#
#         # Accumulate quantities: get current value (or 0 if missing)
#         inventory[key] = inventory.get(key, 0) + value
#
#     return inventory
#
# -----------------------------------------------------------------------------


def data_input() -> dict[str, int]:
    """Return a sample inventory dictionary for the exercise demo."""
    return {
        "sword": 1,
        "potion": 5,
        "shield": 2,
        "armor": 3,
        "helmet": 1
    }


def system_analysis(inventory: dict[str, int]) -> int:
    """Print basic inventory stats and return total item count."""
    print("=== Inventory System Analysis ===")
    if not inventory:
        print("Error: No items provided")
        return 0

    total_items = 0
    for value in inventory.values():
        total_items += value
    print(f"Total items in inventory: {total_items}")

    unique_types = len(inventory)
    print(f"Unique item types: {unique_types}")
    return total_items


def percentage(partial: int, total: int) -> float:
    """Return partial as a percentage of total."""
    if total == 0:
        return 0.0
    result = (partial * 100) / total
    return result


def current(inventory: dict[str, int], total: int) -> None:
    """Print each item quantity and its share of the total."""
    print("\n=== Current Inventory ===")
    for key, value in inventory.items():
        if value == 1:
            print(f"{key}: {value} unit ({percentage(value, total):.1f}%)")
        else:
            print(f"{key}: {value} units ({percentage(value, total):.1f}%)")


def inv_statistics(inventory: dict[str, int]) -> None:
    """Print most and least abundant items from the inventory."""
    print("\n=== Inventory Statistics ===")
    if not inventory:
        print("No inventory statistics available (empty inventory).")
        return
    most_item = None
    most_qty = None
    least_item = None
    least_qty = None

    for item, qty in inventory.items():
        if most_item is None:
            most_item = item
            most_qty = qty
            least_item = item
            least_qty = qty
            continue

        if qty > most_qty:
            most_item = item
            most_qty = qty

        if qty < least_qty:
            least_item = item
            least_qty = qty
    print(f"Most abundant: {most_item} ({most_qty} units)")
    print(f"Least abundant: {least_item} ({least_qty} units)")


def item_categories(inventory: dict[str, int]) -> None:
    """Categorize inventory items by abundance using nested dictionaries."""
    print("\n=== Item Categories ===")
    if not inventory:
        print("No items to categorize")
        return

    categories = {
        "Abundant": {},
        "Moderate": {},
        "Scarce": {}
    }

    for item, qty in inventory.items():
        if qty >= 9:
            category = "Abundant"
        elif qty >= 5:
            category = "Moderate"
        else:
            category = "Scarce"
        categories[category].update({item: qty})

    print(f"Moderate: {categories['Moderate']}")
    print(f"Scarce: {categories['Scarce']}")


def dict_properties(inventory: dict[str, int]) -> None:
    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {inventory.keys()}")
    print(f"Dictionary values: {inventory.values()}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


def main() -> None:
    inventory = data_input()
    total_items = system_analysis(inventory)
    current(inventory, total_items)
    inv_statistics(inventory)
    item_categories(inventory)
    dict_properties(inventory)


if __name__ == "__main__":
    main()
