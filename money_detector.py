import os
import torch
from pathlib import Path
from shutil import make_archive

def money_detector(img):
    repo_or_dir = ''
    model_path = Path('yolov5s_41_640p_mAP5_85.pt')
    save_dir = Path('runs', 'detect', 'exp')

    # Model
    model = torch.hub.load(repo_or_dir, 'custom', path=model_path, source='local')  # or yolov5n - yolov5x6, custom

    # Images
    # img = 'H:/Workspace/dataset1/images/valid/photo_2022-07-02_10-12-37.jpg'  # or file, Path, PIL, OpenCV, numpy, list

    # Inference
    results = model(img)

    # Increment path
    save_dir = increment_path(save_dir)

    # Results
    results.crop(save_dir=save_dir)
    results.save(save_dir=save_dir)

    # Creating an archive
    archive = Path('archive', save_dir.name)
    make_archive(
        str(archive),
        'zip',  # the archive format - or tar, bztar, gztar
        root_dir=save_dir.joinpath('crops'),  # root for archive - current working dir if None
        base_dir=None)  # start archiving from here - cwd if None too

    return open(Path(save_dir, Path(img).name), 'rb'), calculate_the_amount(results), archive # Photo, amount, archive


def increment_path(path, exist_ok=False, sep='', mkdir=False):
    # Increment file or directory path, i.e. runs/exp --> runs/exp{sep}2, runs/exp{sep}3, ... etc.
    path = Path(path)  # os-agnostic
    if path.exists() and not exist_ok:
        path, suffix = (path.with_suffix(''), path.suffix) if path.is_file() else (path, '')
        for n in range(2, 9999):
            p = f'{path}{sep}{n}{suffix}'  # increment path
            if not os.path.exists(p):  #
                break
        path = Path(p)
    return path

def calculate_the_amount(results):
    s = ''
    for i, (im, pred) in enumerate(zip(results.imgs, results.pred)):
        sum = 0
        kopeck = 0
        count = 0
        if pred.shape[0]:
            for c in pred[:, -1].unique():
                n = (pred[:, -1] == c).sum()  # detections per class
                count += n
                class_name = results.names[int(c)].split(' ', 1)
                if class_name[1] == 'копейка' or class_name[1] == 'копеек':
                    kopeck += n * int(class_name[0])
                else:
                    sum += n * int(class_name[0])
            kopecks_in_rubles = torch.div(kopeck, 100, rounding_mode='trunc')
            sum += kopecks_in_rubles
            kopeck -= int(kopecks_in_rubles) * 100
            s += f"Объектов: {count}\n"
            s += f"Сумма: {sum} рублей {(str(int(kopeck)) + ' копеек') * (kopeck > 0)}\n"
        else:
            s += 'Объекты не обнаружены'
    return s

if __name__ == '__main__':
    money_detector('H:/Workspace/dataset1/images/valid/photo_2022-07-02_10-12-37.jpg')