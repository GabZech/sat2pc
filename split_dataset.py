data_dir = "datasets/300_saddle_unclean"

import os
import shutil
import random

# create a function to split the dataset into train, validation and test according to the ratio
def split_dataset_into_train_val_test(data_dir, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15):

    train_path = os.path.join(data_dir, "train")
    val_path = os.path.join(data_dir, "val")
    test_path = os.path.join(data_dir, "test")
    # create the directories
    # os.makedirs(train_path, exist_ok=True)
    # os.makedirs(val_path, exist_ok=True)
    # os.makedirs(test_path, exist_ok=True)
    # get the list of files
    files = [os.path.splitext(f)[0] for f in os.listdir(data_dir) if f.endswith(".png") or f.endswith(".json")]
    files = [*set(files)] # remove duplicates
    # shuffle the files
    random.shuffle(files)
    # get the number of files
    num_files = len(files)
    # get the number of files for each split
    train_num_files = int(num_files * train_ratio)
    val_num_files = int(num_files * val_ratio)
    test_num_files = int(num_files * test_ratio)
    # split the files into train, val and test
    train_files = files[:train_num_files]
    val_files = files[train_num_files:train_num_files+val_num_files]
    test_files = files[train_num_files+val_num_files:]
    # move the files to their corresponding directories
    for file in train_files:
        shutil.move(os.path.join(data_dir, file + ".png"), os.path.join(train_path, "image_filtered", file + ".png"))
        shutil.move(os.path.join(data_dir, file + ".json"), os.path.join(train_path, "annotation", file + ".json"))
    for file in val_files:
        shutil.move(os.path.join(data_dir, file + ".png"), os.path.join(val_path, "image_filtered", file + ".png"))
        shutil.move(os.path.join(data_dir, file + ".json"), os.path.join(val_path, "annotation", file + ".json"))
    for file in test_files:
        shutil.move(os.path.join(data_dir, file + ".png"), os.path.join(test_path, "image_filtered", file + ".png"))
        shutil.move(os.path.join(data_dir, file + ".json"), os.path.join(test_path, "annotation", file + ".json"))


split_dataset_into_train_val_test(data_dir)
print("done")