#!/usr/bin/env python3
import sys

class NotNumberError(ValueError):
    """
    A custom error to be raised when the argv is not an int
    """
    pass


def error_checker(argv: str, index: int) -> None:
    try:
        int(argv)
    except ValueError:
        raise NotNumberError(f"Oops, you typed '{argv}'"
                             f", all arguments must be numbers")

def ft_mean(scores: list[int]) -> int:
    return (sum(scores) / len(scores))


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")
    scores: list[int] = []
    for i in range(1, len(sys.argv)):
        try:
            error_checker((sys.argv[i]), i)
            scores.append(int(sys.argv[i]))
        except NotNumberError as e:
            print(e)

    if not scores:
        print("No scores provided. "
              "Usage: : python3 ft_score_analytics.py <score1> <score2> ...")
        return

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {ft_mean(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    ft_score_analytics()
