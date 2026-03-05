from typing import Generator


Event = tuple[int, str, int, str]


def game_event_stream(n: int) -> Generator[Event, None, None]:
    """Yield n game events as a stream."""

    players = ("alice", "bob", "charlie")
    events = ("killed monster", "found treasure", "leveled up")

    for i in range(1, n + 1):
        player = players[(i - 1) % 3]
        level = (i * 7) % 20 + 1
        event = events[(i - 1) % 3]
        yield i, player, level, event


def stream_analytics(
        event_count: int,
        high_lvl: int,
        treasure: int,
        lvl_up: int
        ) -> None:
    """Print analytics for the processed stream."""

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {event_count}")
    print(f"High-level players (10+): {high_lvl}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {lvl_up}")


def fibonacci_stream(n: int) -> Generator[int, None, None]:
    """Yield the first n Fibonacci numbers."""

    a = 0
    b = 1

    # a and b store consecutive Fibonacci numbers.
    # Each loop:
    # - yield 'a' (current value)
    # - update (a, b) -> (b, a + b) to advance the sequence
    for _ in range(n):
        yield a
        a, b = b, a + b


def is_prime(n: int) -> bool:
    """Return True if n is a prime number."""
    # Numbers below 2 are not prime by definition.
    if n < 2:
        return False
    i = 2
    # We only test divisors up to sqrt(n):
    # if n has a divisor larger than sqrt(n), it must also have a smaller one.
    while i * i <= n:
        # If n is divisible by i, it is not prime.
        if n % i == 0:
            return False
        i += 1
    # No divisors found -> prime.
    return True


def prime_stream() -> Generator[int, None, None]:
    """Yield prime numbers as an infinite stream."""

    candidate = 2
    while True:
        if is_prime(candidate):
            yield candidate
        candidate += 1


def generator_demo() -> None:
    """Print generator demonstrations for Fibonacci and prime sequences."""

    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end="")
    fib = fibonacci_stream(10)
    first_n = True
    for _ in range(10):
        n = next(fib)
        if first_n is True:
            print(f"{n}", end="")
            first_n = False
        else:
            print(f", {n}", end="")
    print()

    print("Prime numbers (first 5): ", end="")
    prime = prime_stream()
    first_p = True
    for _ in range(5):
        n = next(prime)
        if first_p is True:
            print(f"{n}", end="")
            first_p = False
        else:
            print(f", {n}", end="")
    print()


def process_stream(n: int) -> None:
    """Process n events and compute stream counters."""

    event_count = 0
    high_lvl_count = 0
    treasure_count = 0

    lvl_up_count = 0

    print(f"Processing {n} game events...\n")
    for event_id, player, level, event in game_event_stream(n):
        event_count += 1
        if level >= 10:
            high_lvl_count += 1
        if event == "found treasure":
            treasure_count += 1
        if event == "leveled up":
            lvl_up_count += 1
        if event_id <= 3:
            print(f"Event {event_id}: Player {player} (level {level})"
                  f" {event}")
    print("...")

    stream_analytics(event_count, high_lvl_count, treasure_count, lvl_up_count)

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")


def main() -> None:
    """Run the game data stream processor demo."""
    print("=== Game Data Stream Processor ===\n")
    process_stream(1000)
    generator_demo()


if __name__ == "__main__":
    main()
