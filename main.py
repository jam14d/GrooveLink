# main.py
from artist_utils import find_similar_by_genre

def main():
    artist = input("Enter an artist you like: ").strip()
    print(f"\nDiscovering artists similar in genre to: {artist}\n")

    similar = find_similar_by_genre(artist)

    if not similar:
        print("Sorry, no similar artists found.")
        return

    print("You might also like:")
    for name in similar:
        print(f"  - {name}")

if __name__ == "__main__":
    main()
