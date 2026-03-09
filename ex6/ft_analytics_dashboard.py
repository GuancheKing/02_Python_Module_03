#!/usr/bin/env python3
def dashboard() -> None:
    """
    Display a simple game analytics dashboard using Python comprehensions.

    This function demonstrates:
    - List comprehensions for filtering and transforming data
    - Dict comprehensions for creating mappings and aggregations
    - Set comprehensions for extracting unique values

    The data represents a small dataset of players, their scores,
    regions, status and achievements.
    """
    data = [
        {"name": "alice", "score": 2300, "region": "north",
            "status": "active"},
        {"name": "bob", "score": 1800, "region": "north",
            "status": "active"},
        {"name": "charlie", "score": 2150, "region": "east",
            "status": "active"},
        {"name": "diana", "score": 2050, "region": "central",
            "status": "inactive"},
        {"name": "eve", "score": 900, "region": "north",
            "status": "inactive"}
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

    # List comprehension: filter players with high scores (>2000)
    top_scorers = [user['name'] for user in data if user['score'] > 2000]
    print(f"Top performers: {top_scorers}")

    # List comprehension: transform scores by doubling each value
    doubled_scores = [user['score'] * 2 for user in data]
    print(f"Scores doubled: {doubled_scores}")

    # List comprehension: filter players that are currently active
    active_players = [
        user['name'] for user in data
        if user['status'] == "active"
    ]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")

    # Dict comprehension: map each player name to their score
    player_scores = {user['name']: user['score'] for user in data}
    print(f"Player scores: {player_scores}")

    # Dictionary of score categories built from list comprehensions
    score_cats = {
        'high': len([user for user in data if user['score'] > 2000]),
        'medium': len([user for user in data if 1000 <= user['score'] < 2000]),
        'low': len([user for user in data if user['score'] < 1000])
    }
    print(f"Score categories: {score_cats}")

    # Dict comprehension: count achievements for each player
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

    # Set comprehension: extract unique player names
    unique_players = {user['name'] for user in data}
    print(f"Unique players: {unique_players}")

    # Nested set comprehension: collect all unique achievements
    unique_achs = {
        ach for user in achievements
        for ach in achievements[user]
    }
    print(f"Unique achievements: {unique_achs}")

    # Set comprehension: collect regions of active players
    act_regions = {
        user['region'] for user in data
        if user['status'] == 'active'
        }
    print(f"Active regions: {act_regions}")

    print("\n=== Combined Analysis ===")

    total_players = len({user['name'] for user in data})
    print(f"Total players: {total_players}")

    total_achs = len(
        {ach for user in achievements
         for ach in achievements[user]}
    )
    print(f"Total unique achievements: {total_achs}")

    sum_scores = sum([user['score'] for user in data])
    numb_scores = len(data)
    average_score = sum_scores / numb_scores
    print(f"Average score: {average_score}")

    # Filter the dataset to find the player(s) with the max score
    # If multiple players share the top score, the first one is selected
    max_score = max([user['score'] for user in data])
    max_player = [user for user in data if user['score'] == max_score][0]
    max_player_achs = len(achievements[max_player['name']])
    print(
        f"Top performer: {max_player['name']} ({max_player['score']} points,"
        f" {max_player_achs} achievement(s))")


def main() -> None:
    dashboard()


if __name__ == "__main__":
    main()
