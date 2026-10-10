import csv
from project import get_top_repos
from project import get_language_stats
from project import export_csv

def test_get_top_repos():
    repos = [
            {"name": "A", "stargazers_count": 10},
            {"name": "B", "stargazers_count": 50},
            {"name": "C", "stargazers_count": 20}
        ]
    result = get_top_repos(repos, 2)
    assert result[0]["name"] == "B"
    assert result[1]["name"] == "C"

def test_get_language_stats():
    repos = [
            {"name": "A", "language": 'python'},
            {"name": "B", "language": 'c'},
            {"name": "C", "language": 'python'}
        ]
    result = get_language_stats(repos)
    assert result[0][0] == "python"
    assert result[1][0] == 'c'
    assert result[0][1] == 2

def test_export_csv(tmp_path):
    repos = [
        {"name": "A", "stargazers_count": 10, "language": "Python"},
        {"name": "B", "stargazers_count": 20, "language": "Java"}
    ]
    filename = tmp_path / "test.csv"
    export_csv(repos, filename)
    with open(filename, "r", newline = '', encoding = 'utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    assert rows[0]['name'] == 'A'
    assert rows[0]['stars'] == '10'
    assert rows[1]['language'] == 'Java'

