import os
import random
import shutil

# Paths
base_path = r"C:\Users\varsh\OneDrive\Desktop\trypanosoma_images"
images_path = os.path.join(base_path, "images")
labels_path = os.path.join(base_path, "labels")

output_path = os.path.join(base_path, "dataset")

train_img = os.path.join(output_path, "images/train")
val_img = os.path.join(output_path, "images/val")
train_lbl = os.path.join(output_path, "labels/train")
val_lbl = os.path.join(output_path, "labels/val")

# Create folders
for path in [train_img, val_img, train_lbl, val_lbl]:
    os.makedirs(path, exist_ok=True)

# Get all images
images = [f for f in os.listdir(images_path) if f.endswith(".jpg")]

# Shuffle
random.shuffle(images)

# Split 80/20
split_idx = int(0.8 * len(images))
train_files = images[:split_idx]
val_files = images[split_idx:]

def move_files(file_list, img_dest, lbl_dest):
    for file in file_list:
        img_src = os.path.join(images_path, file)
        lbl_src = os.path.join(labels_path, file.replace(".jpg", ".txt"))

        if os.path.exists(lbl_src):  # only move if label exists
            shutil.copy(img_src, img_dest)
            shutil.copy(lbl_src, lbl_dest)
        else:
            print(f"⚠️ Missing label for {file}")

# Move files
move_files(train_files, train_img, train_lbl)
move_files(val_files, val_img, val_lbl)

print("✅ Dataset split complete!")