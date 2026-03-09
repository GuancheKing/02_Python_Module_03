#!/usr/bin/env python3
import sys


def custom_atoi(num_str: str) -> int:
    """
    Convert a numeric string into an integer.

    Raise ValueError if the string is empty or contains non-digit characters.
    """
    digits = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }
    if not num_str:
        raise ValueError("Error: value must be an integer")
    value = 0
    for c in num_str:
        if c not in digits:
            raise ValueError("Error: value must be an integer")
        value = value * 10 + digits[c]
    return value


def data_input() -> dict[str, int]:
    """
    Parse command-line arguments into an inventory dictionary.

    Each argument must follow the format 'item:quantity'.
    """
    result = {}
    for arg in sys.argv[1:]:
        key = ""
        value_str = ""
        reading_value = False
        colon_count = 0

        for c in arg:
            if c == ":":
                colon_count += 1
                if colon_count > 1:
                    raise ValueError("Error: invalid item format")
                reading_value = True
            elif not reading_value:
                key += c
            else:
                value_str += c

        if colon_count != 1 or key == "" or value_str == "":
            raise ValueError("Error: invalid item format")

        value = custom_atoi(value_str)
        result[key] = value
    return result


def system_analysis(inventory: dict[str, int]) -> int:
    """Print basic inventory stats and return total item count."""
    print("=== Inventory System Analysis ===")
    if not inventory:
        raise ValueError("Error: No items provided")

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
        raise ValueError(
            "No inventory statistics available (empty inventory)."
        )
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

    if most_qty == 1:
        most_unit = "unit"
    else:
        most_unit = "units"

    if least_qty == 1:
        least_unit = "unit"
    else:
        least_unit = "units"

    print(f"Most abundant: {most_item} ({most_qty} {most_unit})")
    print(f"Least abundant: {least_item} ({least_qty} {least_unit})")


def suggestions(inventory: dict[str, int]) -> None:
    """Print restocking suggestions for low-stock items."""
    print("\n=== Management Suggestions ===")
    restock = []
    for item, qty in inventory.items():
        if qty <= 1:
            restock.append(item)

    if not restock:
        print("Restock needed: None")
        return

    formatted = ""
    # Loop through the list using indexes (0, 1, 2, ...)
    for i in range(len(restock)):
        # Add the current item name to the string
        formatted += restock[i]
        # Check if this is NOT the last element in the list
        if i < len(restock) - 1:
            formatted += ", "
    print(f"Restock needed: {formatted}")


def item_categories(inventory: dict[str, int]) -> None:
    """Categorize inventory items by abundance using nested dictionaries."""
    print("\n=== Item Categories ===")
    if not inventory:
        raise ValueError("No items to categorize")

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
    """Demonstrate dictionary keys, values and membership operations."""
    print("\n=== Dictionary Properties Demo ===")
    keys_formatted = ""
    count = 0
    total = len(inventory)

    for key in inventory.keys():
        keys_formatted += key
        count += 1
        if count < total:
            keys_formatted += ", "

    print(f"Dictionary keys: {keys_formatted}")

    count = 0
    values_formatted = ""

    for value in inventory.values():
        values_formatted += f"{value}"
        count += 1
        if count < total:
            values_formatted += ", "

    print(f"Dictionary values: {values_formatted}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


def main() -> None:
    """Run the inventory system analysis workflow."""
    try:
        inventory = data_input()
        total_items = system_analysis(inventory)
        current(inventory, total_items)
        inv_statistics(inventory)
        item_categories(inventory)
        suggestions(inventory)
        dict_properties(inventory)
    except Exception as e:
        print(f"{e}")


if __name__ == "__main__":
    main()
