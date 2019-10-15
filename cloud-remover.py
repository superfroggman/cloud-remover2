import sys
import imageio

vid = imageio.get_reader(sys.argv[1],  'ffmpeg')
base_img = vid.get_data(0)
for l in range(vid.count_frames()):
    img = vid.get_data(l)
    print("frame")
    print(l)
    for i in range(len(img)):
        for j in range(len(img[1])):
            r, g, b = img[i][j]
            totalNew = (int(r)+int(g)+int(b))/3
            r2, g2, b2 = base_img[i][j]
            totalOld = (int(r2)+int(g2)+int(b2))/3
            if(totalNew < totalOld):
                base_img[i][j] = img[i][j]

print ("DONE! Ignore errors after this.")
imageio.imwrite(sys.argv[2], base_img)
