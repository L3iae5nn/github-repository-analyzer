import requests
import csv
import os

def main():
    try:
        username = input("Github username: ")
        all_repos = get_repos(username)
        print(f"Total repositories: {len(all_repos)}")
        top5repos = get_top_repos(all_repos, 5)
        print('Top 5 Repositories: ')
        for i, repo in enumerate(top5repos, start = 1):
            print(f"{i} {repo['name']} {repo['stargazers_count']} stars")
        sorted_languages = get_language_stats(all_repos)
        for language in sorted_languages:
            print(f"{language[0]}: {language[1]} repositories")
        export_csv(all_repos)
        print("Repositories exported to repositories.csv")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return

def get_repos(username): #get user's all repos
    token = os.getenv("GITHUB_TOKEN")
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    page = 1
    all_repos = []
    while True:
        params = {"per_page": 100, "page": page}
        response = requests.get(
            f"https://api.github.com/users/{username}/repos",
            params = params,
            headers = headers,
            timeout = 10
        )
        response.raise_for_status()
        repos = response.json()
        all_repos.extend(repos)
        if len(repos) < 100:
            break
        page += 1
    return all_repos

def get_top_repos(all_repos, n = 5): #get top 5(default) repos by stargazers_count
    sorted_repos = sorted(all_repos, key = lambda repo: repo["stargazers_count"], reverse = True)
    return sorted_repos[:n]

def get_language_stats(all_repos): #get most used languages by user
    languages = {}
    for repo in all_repos:
        language = repo["language"]
        if language is None:
            continue
        languages[language] = languages.get(language, 0) + 1
    sorted_languages = sorted(languages.items(), key = lambda items: items[1], reverse = True)
    return sorted_languages

def export_csv(repos, filename = "repositories.csv"):
    with open(filename, "w", newline = "", encoding = "utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames = ['name', 'stars', 'language']
        )
        writer.writeheader()

        for repo in repos:
            writer.writerow({
                "name": repo["name"],
                "stars": repo["stargazers_count"],
                "language": repo["language"]
            })

if __name__ == "__main__":
    main()