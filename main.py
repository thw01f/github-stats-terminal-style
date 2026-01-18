import os
import requests

def get_stats():
    # If you haven't set the secret yet, this line might fail locally, but works in Actions
    token = os.environ.get("GHT")
    headers = {"Authorization": f"token {token}"} if token else {}
    
    # Change 'thw01f' to your actual GitHub username if different
    response = requests.get("https://api.github.com/users/thw01f", headers=headers)
    data = response.json()
    
    return {
        "name": "w01f",  # FORCE display name to w01f
        "public_repos": data.get("public_repos", 0),
        "followers": data.get("followers", 0),
        "following": data.get("following", 0),
    }

def make_svg(data):
    # HACKER RED THEME CONFIGURATION
    bg_color = "#0D1117"   # GitHub Dark Mode Background
    text_color = "#FF0000" # Bright Red
    border_color = "#FF0000"
    
    svg = f"""<svg width="400" height="200" viewBox="0 0 400 200" fill="none" xmlns="http://www.w3.org/2000/svg">
    <style>
    .header {{ font: 600 18px 'Courier New', monospace; fill: {text_color}; }}
    .stat {{ font: 400 14px 'Courier New', monospace; fill: {text_color}; }}
    </style>
    
    <rect width="100%" height="100%" rx="10" fill="{bg_color}" stroke="{border_color}" stroke-width="2"/>
    
    <text x="20" y="35" class="header">root@w01f:~# ./status</text>
    
    <text x="20" y="80" class="stat">User: {data['name']}</text>
    <text x="20" y="110" class="stat">Repos: {data['public_repos']}</text>
    <text x="20" y="140" class="stat">Followers: {data['followers']}</text>
    <text x="20" y="170" class="stat">Following: {data['following']}</text>
    
    <rect x="20" y="180" width="10" height="2" fill="{text_color}">
      <animate attributeName="opacity" values="0;1;0" dur="1s" repeatCount="indefinite" />
    </rect>
    </svg>"""
    return svg

def main():
    try:
        data = get_stats()
        svg = make_svg(data)
        with open("github_stats.svg", "w") as f:
            f.write(svg)
        print("✅ SVG Generated Successfully")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
