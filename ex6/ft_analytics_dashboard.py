#!/usr/bin/env python3
def dashboard() -> None:
    """
    Display a simple game analytics dashboard using Python comprehensions.

    This function demonstrates:
    - List comprehensions for filtering and transforming data
    - Dict comprehensions for creating mappings and aggregations

    The data represents a small dataset of players, their scores,
    regions, status and achievements.
    """
    data = [
        {"name": "alice", "score": 2300, "region": "north",
            "status": "active", "cluster": "normal"},
        {"name": "bob", "score": 1800, "region": "north",
            "status": "active", "cluster": "competitive"},
        {"name": "charlie", "score": 2150, "region": "east",
            "status": "active", "cluster": "normal"},
        {"name": "diana", "score": 2050, "region": "central",
            "status": "inactive", "cluster": "normal"},
        {"name": "eve", "score": 900, "region": "north",
            "status": "inactive", "cluster": "competitive"}
    ]

    achievements = {
        "alice": {'level_10', 'treasure_hunter', 'speed_demon', 'boss_slayer'},
        "bob": {'first_kill', 'level_10', 'boss_slayer', 'collector'},
        "charlie": {'level_10', 'treasure_hunter', 'perfectionist'},
        "diana": {'speed_demon', 'perfectionist', 'level_10', 'first_kill'},
        "eve": {'first_kill', 'level_10'},
    }

    print("=== Game Analytics Dashboard ===")
    print("\n=== List Comprehensions ===")

    # Filter players with high scores (>2000)
    top_scorers = [user['name'] for user in data if user['score'] > 2000]
    print(f"Top performers: {top_scorers}")

    # Transform scores by doubling each value
    doubled_scores = [user['score'] * 2 for user in data]
    print(f"Scores doubled: {doubled_scores}")

    # Filter players that are currently active
    active_players = [user['name'] for user in data if user['status'] == "active"]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")

    # Map each player name to their score
    player_scores = {user['name']: user['score'] for user in data}
    print(f"Player scores: {player_scores}")

    # Categorize players by score range
    score_cats = {
        'high': len([user for user in data if user['score'] > 2000]),
        'medium': len([user for user in data if 1000 < user['score'] < 2000]),
        'low': len([user for user in data if user['score'] < 1000])
    }
    print(f"Score categories: {score_cats}")

    # Count number of achievements per player
    achs_count = {
        user: len(achievements[user])
        for user in achievements
    }
    # Alternative, more Pythonic approach using .items()
    # achs_count = {
    #     user: len(ach)
    #     for user, ach in achievements.items()
    # }
    print(f"Achievement counts: {achs_count}")

    print("\n=== Set Comprehension Examples ===")
def main() -> None:
    dashboard()


if __name__ == "__main__":
    main()
