from python_ai_learning.main import create_learning_profile


def test_create_learning_profile():
    profile = create_learning_profile("Munisamy", "Learn Machine Learning")

    assert profile["name"] == "Munisamy"
    assert profile["goal"] == "Learn Machine Learning"
    assert profile["current_stage"] == "Python Fundamentals"
