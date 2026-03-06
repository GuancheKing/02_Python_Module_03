#!/usr/bin/env python3
import sys


def data_input() -> dict[str, int]:
    result = {}
    for arg in sys.argv[1:]:
        key = ""
        value = 0
        reading_value = False

        for c in arg:
            if c == ":":
                reading_value = True
            elif not reading_value:
                key += c
            else:
                value = value * 10 + (ord(c) - ord('0'))
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
        raise ValueError("No inventory statistics available (empty inventory).")
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
    """Demonstrate dictionary operations such as keys, values & membership."""
    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {inventory.keys()}")
    print(f"Dictionary values: {inventory.values()}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


def main() -> None:
    """Run the inventory system analysis workflow."""
    inventory = data_input()
    try:
        total_items = system_analysis(inventory)
        current(inventory, total_items)
        inv_statistics(inventory)
        item_categories(inventory)
        dict_properties(inventory)
    except Exception as e:
        print(f"{type(e)}: {e}")


if __name__ == "__main__":
    main()
