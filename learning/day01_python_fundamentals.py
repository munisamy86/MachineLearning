"""Day 1: Python fundamentals — variables, data types, operators, and conditions."""


def calculate_average(scores: list[int]) -> float:
    """Return the average score, or 0.0 when the list is empty."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def main() -> None:
    # Variables and common data types
    student_name: str = "Munisamy"
    student_age: int = 39
    daily_study_hours: float = 1.5
    is_learning_python: bool = True
    scores: list[int] = [85, 90, 78]

    average_score = calculate_average(scores)
    passed = average_score >= 50

    print("=== Python Fundamentals: Day 1 ===")
    print(f"Name: {student_name} (type: {type(student_name).__name__})")
    print(f"Age: {student_age} (type: {type(student_age).__name__})")
    print(
        f"Daily study hours: {daily_study_hours} "
        f"(type: {type(daily_study_hours).__name__})"
    )
    print(f"Learning Python: {is_learning_python}")
    print(f"Scores: {scores}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {average_score:.2f}")
    print(f"Result: {'PASS' if passed else 'KEEP PRACTICING'}")


if __name__ == "__main__":
    main()
