import sys
import musicbrainzngs

musicbrainzngs.set_useragent("test project", "0.1", "jeremy.mullis@gmail.com")

artist = sys.argv[1]

limit = 100
offset = 0
recordings = []
page = 1

print("fetching page number %d.." % page)
result = musicbrainzngs.browse_recordings(artist=artist, limit=limit)
page_recordings = result['recording-list']
recordings += page_recordings
count = result['recording-count']
print("")

while len(page_recordings) >= limit:
    offset += limit
    page += 1
    print("fetching page number %d.." % page)
    result = musicbrainzngs.browse_recordings(
        artist=artist, limit=limit, offset=offset)
    page_recordings = result['recording-list']
    recordings += page_recordings
print("")

# print(recordings)

recording_list = []

for recording in recordings:
    recording_list += [recording['title']]

recording_list_dedupe = list(set(recording_list))

f = open("data/raw/" + artist + ".txt", 'a')

recording_list_dedupe.sort()

for recording in recording_list_dedupe:
    f.write(recording + "\n")
    print(recording)
