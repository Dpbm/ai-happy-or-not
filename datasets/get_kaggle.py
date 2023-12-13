import os
import sys

DEFAULT_FOLDER = os.getcwd() 

def get_dataset(dataset, folder=DEFAULT_FOLDER):
    dataset_name = dataset.split('/')[-1]
    dataset_path = os.path.join(folder, dataset_name)

    if(not os.path.exists(dataset_path)):
        os.mkdir(dataset_path)
    
    os.system(f"kaggle datasets download {dataset} --path {dataset_path} --unzip")

def get_datasets(datasets_file, folder=DEFAULT_FOLDER):
    print("---Getting data from kaggle---")    
    print("file: ",datasets_file)    
    print("folder: ",folder)    
    with open(datasets_file, "r") as file:
        datasets = [dataset.strip() for dataset in file.readlines()]
        total = len(datasets)

        for i, dataset in enumerate(datasets):
            print(f"({i+1}/{total}) {dataset}")
            get_dataset(dataset, folder=folder)

if __name__ == '__main__':
    arguments = sys.argv
    total_arguments = len(arguments)
    
    if(total_arguments < 2 or total_arguments > 3):
        print("Usage: python get_kaggle.py ./datasets.txt [/target_folder/]")
        sys.exit(1)
    
    kaggle_datasets = arguments[1]
    
    target_folder = DEFAULT_FOLDER
    if(total_arguments==3):
        target_folder = arguments[-1] 

    get_datasets(kaggle_datasets, folder=target_folder)
