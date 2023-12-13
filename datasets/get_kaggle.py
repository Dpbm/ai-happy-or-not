import os

def get_dataset(dataset):
    os.system(f"kaggle datasets download {dataset} --unzip")

def get_datasets(datasets_file):
    print("---Getting data from kaggle---")    
    with open(datasets_file, "r") as file:
        datasets = [dataset.strip() for dataset in file.readlines()]
        total = len(datasets)

        for i, dataset in enumerate(datasets):
            print(f"({i+1}/{total}) {dataset}")
            get_dataset(dataset)

if __name__ == '__main__':
    kaggle_datasets = 'kaggle.txt'
    get_datasets(kaggle_datasets)
