#!/usr/bin/env python3
def main() -> None:
    """Demonstrate set operations for tracking and analyzing achievements."""

    print("\033[32m=== \033[0mAchievement Tracker System \033[32m===\033[0m\n")
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    print(f"Player alice achievements: {alice}")
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    print(f"Player bob achievements: {bob}")
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer',
               'speed_demon', 'perfectionist'}
    print(f"Player charlie achievements: {charlie}")

    print("\n\033[32m=== \033[0mAchievement Analytics \033[32m===")
    unique = alice.union(bob, charlie)
    print(f"\033[0mAll unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}")
    common = alice.intersection(bob, charlie)

    print(f"\nCommon to all players: {common}")
    players = [alice, bob, charlie]
    rare = set()
    for p in players:
        others = set()
        for q in players:
            if q is not p:
                others = others.union(q)
        only_p = p.difference(others)
        rare = rare.union(only_p)
# Non-scalable approach (kept for reference):
    # only_alice = alice.difference(bob.union(charlie))
    # only_bob = bob.difference(alice.union(charlie))
    # only_charlie = charlie.difference(alice.union(bob))
    # rare = only_alice.union(only_bob.union(only_charlie))
    print(f"Rare achievements (1 player): {rare}")

    print(f"\nAlice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    main()
