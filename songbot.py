import argparse
from generator import generate_song_titles

parser = argparse.ArgumentParser(
    prog="Song Title Bot 3",
    description="AI to generate funny song titles"
)

parser.add_argument('-n', '--number', default=1, type=int)
parser.add_argument('-p', '--prompt', default='')
parser.add_argument('-t', '--temperature', default=1.0, type=float)
# parser.add_argument('-s', '--save', action='store_true')
args = parser.parse_args()

song_titles = generate_song_titles(
    number=args.number,
    temperature=args.temperature,
    prompt=args.prompt
)

outputFile = open("output/log.txt", "a")

for song_title in song_titles:
    outputFile.write("\n")
    outputFile.write(song_title)
    print(song_title)

print(args)
