#! /usr/bin/env python3

import sys


def analyze_scores() -> None:
    argv = sys.argv
    argc = len(argv)

    print("=== Player Score Analytics ===")

    list_scores = []
    i = 1
    while i < argc:
        try:
            score = int(argv[i])
            list_scores += [score]
        except ValueError:
            print(f"Invalid parameter: '{argv[i]}'")
        i += 1

    if not list_scores:
        print("No scores provided. ", end="")
        print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    print(f"Scores processed: {list_scores}")

    players = len(list_scores)
    print(f"Total players: {players}")

    scores = sum(list_scores)
    print(f"Total score: {scores}")

    average = scores / players
    print(f"Average score: {average:.1f}")

    high = max(list_scores)
    low = min(list_scores)
    print(f"High score: {high}")
    print(f"Low score: {low}")

    print(f"Score range: {high - low}")


if __name__ == "__main__":
    analyze_scores()
