import os.path
import cv2

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
        f = open(f'{os.path.basename(path).split(".")[0]}.data', 'xb')
    except Exception as e:
        print(e)
        continue

    while True:
        success, image = video.read()
        if not success:
            break
        image = cv2.resize(image, (80, 24))
        for y in range(24):
            for x in range(0, 80, 2):
                f.write(bytes((*tuple(image[y, x]), *tuple(image[y, x + 1]))))
    f.close()

    print(f'Recommended tick/sec: {round(960 * video.get(cv2.CAP_PROP_FPS))}')
