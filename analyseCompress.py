import os

topFiles = []

# folder path input
print("Enter folder path")
# path = os.path.abspath(input())
path = os.path.abspath("/Users/aaron/Pictures/")
print(path)
# for storing size of each
# file
size = 0

# for storing the size of
# the largest file
max_size = 60000000

# for storing the path to the
# largest file
max_file =""

if not os.path.exists("completed_videos.text"):
    f= open("completed_videos.txt","w+")

for folder, subfolders, files in os.walk(path):

    # checking the size of each file
    for file in files:
        size = os.stat(os.path.join( folder, file  )).st_size

        # updating maximum size
        if size>max_size:
            s = os.path.join(folder, file)
            s = s.replace("/Users/aaron/Pictures/Photos Library.photoslibrary/originals", "/Users/aaron/Pictures/Photos\ Library.photoslibrary/originals")

            if file in open('completed_videos.txt').read():
                break
                if ".mov" in file:
                    print("not dkipped")
                    print(file)
                    topFiles.append(s)


with open('completed_videos.txt', 'w') as f:
    for i in topFiles:
        save_file = i.split("/")

        # print(save_file[-1])
        os.system("ffmpeg -i " + i + " -map_metadata 0 /Users/aaron/Desktop/"+ save_file[-1])
        # os.system("exiftool -TagsFromFile " + i + " -all:all>all:all -ee " + "/Users/aaron/Desktop/"+ save_file[-1])
        f.write("%s\n" % save_file[-1])
        # os.system("exiftool -TagsFromFile " + i + " -FileModifyDate<XMP:DateTimeOriginal" + " -FileModifyDate<EXIF:CreateDate" + " -FileModifyDate<XMP:CreateDate" + " -FileModifyDate<$IPTC:DateCreated $IPTC:TimeCreated" + " -FileModifyDate<EXIF:DateTimeOriginal " + "/Users/aaron/Desktop/"+ save_file[-1])

print("Done!")
