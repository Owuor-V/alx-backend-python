def stream_user_ages(users):
    """
    Generator that yields ages one by one from a list of users.
    Each user is represented as a dictionary with an 'age' field.
    """
    for user in users:
        yield user["age"]


def average_age(users):
    """
    Uses the generator to compute the average age
    without loading all data into memory at once.
    """
    total = 0
    count = 0
    for age in stream_user_ages(users):
        total += age
        count += 1
    return total / count if count > 0 else 0


if __name__ == "__main__":
    # Example dataset (replace this with a large dataset later)
    users = [
        {"name": "Alice", "age": 24},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 28},
        {"name": "Diana", "age": 35},
    ]

    avg = average_age(users)
    print(f"Average age of users: {avg}")
