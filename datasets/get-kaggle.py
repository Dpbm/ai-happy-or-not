import os

def get_dataset(dataset):
    os.system(f"kaggle datasets download {dataset} --unzip")

if __name__ == '__main__':
    print("---Getting data from kaggle---")
    
    kaggle_datasets = 'kaggle.txt'

    with open(kaggle_datasets, "r") as file:
        datasets = [dataset.strip() for dataset in file.readlines()]
        total = len(datasets)

        for i, dataset in enumerate(datasets):
            print(f"({i+1}/{total}) {dataset}")
            get_dataset(dataset)
