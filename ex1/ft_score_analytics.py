#!/usr/bin/env python3
import sys


class NotNumberError(ValueError):
    """
    Raised when a command-line argument cannot be converted to int.
    """
    pass


def error_checker(argv: str, index: int) -> None:
    """Validate that an argument is an integer.

    Args:
        arg: Raw command-line argument to validate.
        index: Argument position in sys.argv (1-based for user arguments).

    Raises:
        NotNumberError: If arg is not a valid integer string.
    """
    try:
        int(argv)
    except ValueError:
        raise NotNumberError(f"Oops, you typed '{argv}'"
                             f", all arguments must be numbers")


def ft_mean(scores: list[int]) -> float:
    """
    Return the arithmetic mean of a non-empty list of integers.
    """
    return (sum(scores) / len(scores))


def ft_score_analytics() -> None:
    """
    Parse scores from sys.argv and print basic descriptive statistics.
    """
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
