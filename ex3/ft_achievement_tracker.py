#! /usr/bin/env python3

import random

ALL_ACHIEVEMENTS = [
    "Crafting Genius",
    "Strategist",
    "World Savior",
    "Speed Runner",
    "Survivor",
    "Master Explorer",
    "Treasure Hunter",
    "Unstoppable",
    "Hidden Path Finder",
    "First Steps",
    "Collector Supreme",
    "Untouchable",
    "Sharp Mind",
    "Boss Slayer",
]


def gen_player_achievements() -> set[str]:
    count = random.randint(4, 7)
    return set(random.sample(ALL_ACHIEVEMENTS, count))


def achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")
    alice = gen_player_achievements()
    print(f"Player Alice: {alice}")
    bob = gen_player_achievements()
    print(f"Player Bob: {bob}")
    charlie = gen_player_achievements()
    print(f"Player Charlie: {charlie}")
    dylan = gen_player_achievements()
    print(f"Player Dylan: {dylan}")

    distinct = alice.union(bob, charlie, dylan)
    print(f"\nAll distinct achievements: {distinct}")

    intersection = alice.intersection(bob, charlie, dylan)
    print(f"\nCommon achievements: {intersection}")

    only_alice = alice.difference(bob.union(charlie, dylan))
    print(f"\nOnly Alice has: {only_alice}")
    only_bob = bob.difference(alice.union(charlie, dylan))
    print(f"Only Bob has: {only_bob}")
    only_charlie = charlie.difference(alice.union(bob, dylan))
    print(f"Only Charlie has: {only_charlie}")
    only_dylan = dylan.difference(alice.union(bob, charlie))
    print(f"Only Dylan has: {only_dylan}")

    full_set = set(ALL_ACHIEVEMENTS)
    print(f"\nAlice is missing: {full_set.difference(alice)}")
    print(f"Bob is missing: {full_set.difference(bob)}")
    print(f"Charlie is missing: {full_set.difference(charlie)}")
    print(f"Dylan is missing: {full_set.difference(dylan)}")


if __name__ == "__main__":
    achievement_tracker()
