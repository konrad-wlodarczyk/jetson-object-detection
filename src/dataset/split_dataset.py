import os
import random
import shutil

BASE = "data/dataset"

TRAIN_IMG = os.path.join(BASE, "train/images")
TRAIN_LBL = os.path.join(BASE, "train/labels")

VAL_IMG = os.path.join(BASE, "val/images")
VAL_LBL = os.path.join(BASE, "val/labels")

os.makedirs(VAL_IMG, exist_ok=True)
os.makedirs(VAL_LBL, exist_ok=True)

images = [f for f in os.listdir(TRAIN_IMG)
          if f.endswith(".jpg") or f.endswith(".png")]

random.shuffle(images)

val_size = int(len(images) * 0.2)
val_images = images[:val_size]

print(f"Total images: {len(images)}")
print(f"Moving to val: {len(val_images)}")

for img in val_images:
    img_path = os.path.join(TRAIN_IMG, img)
    lbl_path = os.path.join(TRAIN_LBL, img.replace(".jpg", ".txt").replace(".png", ".txt"))

    shutil.move(img_path, os.path.join(VAL_IMG, img))

    if os.path.exists(lbl_path):
        shutil.move(lbl_path, os.path.join(VAL_LBL, os.path.basename(lbl_path)))

print("Dataset split completed.")