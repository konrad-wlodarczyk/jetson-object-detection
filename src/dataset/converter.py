from pathlib import Path
from PIL import Image
import pillow_heif
from tqdm import tqdm

pillow_heif.register_heif_opener()

RAW_DIR = Path("data/raw")
OUTPUT_DIR = Path("data/images/train")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def convert_class(class_dir: Path, class_name: str):
    images = list(class_dir.glob("*.HEIC")) + list(class_dir.glob("*.HEIC"))
    
    output_class_dir = OUTPUT_DIR / class_name
    output_class_dir.mkdir(parents=True, exist_ok=True)
    
    for idx, img_path in enumerate(tqdm(images, desc=class_name)):
        try:
            img = Image.open(img_path)
            
            output_name = f"{class_name}_{idx:04}.jpg"
            output_path = output_class_dir / output_name

            img.convert("RGB").save(output_path, "JPEG", quality=95)

        except Exception as e:
            print(f"Error with {img_path}: {e}")


def main():
    for class_dir in RAW_DIR.iterdir():
        if class_dir.is_dir():
            print(f"Processing class: {class_dir.name}")
            convert_class(class_dir, class_dir.name)

    print("\nDONE: conversion finished")


if __name__ == "__main__":
    main()