"""Starter application for the Python and AI learning repository."""


def create_learning_profile(name: str, goal: str) -> dict[str, str]:
    """Create a small learning profile."""
    return {
        "name": name,
        "goal": goal,
        "current_stage": "Python Fundamentals",
    }


def main() -> None:
    profile = create_learning_profile(
        name="Munisamy",
        goal="Learn Python, Machine Learning, and AI",
    )
    print("Welcome to Python AI Learning!")
    for key, value in profile.items():
        print(f"{key.replace('_', ' ').title()}: {value}")


if __name__ == "__main__":
    main()
