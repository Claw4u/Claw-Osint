import requests
import threading

# ANSI escape codes for colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_banner():
    banner = f"""
{Colors.OKBLUE}{Colors.BOLD}

 ██████╗██╗      █████╗ ██╗    ██╗
██╔════╝██║     ██╔══██╗██║    ██║
██║     ██║     ███████║██║ █╗ ██║
██║     ██║     ██╔══██║██║███╗██║
╚██████╗███████╗██║  ██║╚███╔███╔╝
 ╚═════╝╚══════╝╚═╝  ╚═╝ ╚══╝╚══╝
{Colors.ENDC}
"""
    print(banner)

def check_username(username, platform, url, results):
    try:
        response = requests.get(url, allow_redirects=False)
        if response.status_code == 200:
            results[platform] = f"{Colors.OKGREEN}Username ditemukan! Link: {url}{Colors.ENDC}"
        else:
            results[platform] = f"{Colors.FAIL}Username tidak ditemukan.{Colors.ENDC}"
    except requests.RequestException:
        results[platform] = f"{Colors.WARNING}Gagal menghubungi situs.{Colors.ENDC}"

def check_usernames(username):
    platforms = {
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "Reddit": f"https://www.reddit.com/user/{username}/",
        "Facebook": f"https://www.facebook.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}/",
        "YouTube": f"https://www.youtube.com/{username}",
        "Tumblr": f"https://{username}.tumblr.com/",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "Flickr": f"https://www.flickr.com/people/{username}",
        "Dribbble": f"https://dribbble.com/{username}",
        "Behance": f"https://www.behance.net/{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "MixCloud": f"https://www.mixcloud.com/{username}",
        "500px": f"https://500px.com/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "LastFM": f"https://www.last.fm/user/{username}",
        "Badoo": f"https://www.badoo.com/en/{username}",
        "VK": f"https://vk.com/{username}",
        "Medium": f"https://medium.com/@{username}",
        "AngelList": f"https://angel.co/{username}",
        "Goodreads": f"https://www.goodreads.com/{username}",
        "WeHeartIt": f"https://weheartit.com/{username}",
        "Patreon": f"https://www.patreon.com/{username}",
        "Wattpad": f"https://www.wattpad.com/user/{username}",
        "Flipboard": f"https://flipboard.com/@{username}",
        "HackerNews": f"https://news.ycombinator.com/user?id={username}",
        "LiveJournal": f"https://{username}.livejournal.com/",
        "Quora": f"https://www.quora.com/profile/{username}",
        "Keybase": f"https://keybase.io/{username}",
        "Kik": f"https://kik.me/{username}",
        "ReverbNation": f"https://www.reverbnation.com/{username}",
        "About.me": f"https://about.me/{username}",
        "TripAdvisor": f"https://www.tripadvisor.com/Profile/{username}",
        "MyAnimeList": f"https://myanimelist.net/profile/{username}",
        "Etsy": f"https://www.etsy.com/people/{username}",
        "Bandcamp": f"https://{username}.bandcamp.com/",
        "Kongregate": f"https://www.kongregate.com/accounts/{username}",
        "Giphy": f"https://giphy.com/{username}",
        "CodePen": f"https://codepen.io/{username}",
        "Canva": f"https://www.canva.com/{username}",
        "ProductHunt": f"https://www.producthunt.com/@{username}",
        "Discogs": f"https://www.discogs.com/user/{username}",
        "Houzz": f"https://www.houzz.com/user/{username}",
        "OpenSea": f"https://opensea.io/{username}",
        "HackerRank": f"https://www.hackerrank.com/{username}",
        "CTFTime": f"https://ctftime.org/team/{username}",
        "TryHackMe": f"https://tryhackme.com/p/{username}",
        "HackTheBox": f"https://app.hackthebox.com/profile/{username}",
        "Discord": f"https://discord.com/users/{username}",
        "Clubhouse": f"https://www.joinclubhouse.com/@{username}",
        "Telegram": f"https://t.me/{username}",
        "Slack": f"https://{username}.slack.com",
        "Yelp": f"https://www.yelp.com/user_details?userid={username}"
    }

    results = {}
    threads = []

    for platform, url in platforms.items():
        thread = threading.Thread(target=check_username, args=(username, platform, url, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results

if __name__ == "__main__":
    print_banner()
    username = input(f"{Colors.OKBLUE}Masukkan username yang ingin dicek: {Colors.ENDC}")
    hasil = check_usernames(username)

    for platform, status in hasil.items():
        print(f"{platform}: {status}")
