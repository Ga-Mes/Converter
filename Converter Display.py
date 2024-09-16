import os.path
import cv2

width, height = 48, 64

while True:
    path = input('File: ').replace('"', '')

    if path == '!':
        break

    try:
        video = cv2.VideoCapture(path)
    except Exception as e:
        print(e)
        continue

    if video is None:
        continue

    try:
        f = open(f'Turing Complete//tcvd//{os.path.basename(path).split(".")[0]} ({width}-{height}).data', 'xb')
    except Exception as e:
        print(e)
        continue

    while True:
        success, image = video.read()
        if not success:
            break
        image = cv2.resize(image, (width, height))
        for gy in range(0, height, 8):
            for x in range(0, 6):
                for y in range(0, 8):
                    for gx in range(width // 6):
                        f.write(bytes(tuple(image[y + gy, x + 6 * gx])))
    f.close()

    print(f'Recommended tick/sec: {round(width * height * video.get(cv2.CAP_PROP_FPS) / (width / 6))}')
    
