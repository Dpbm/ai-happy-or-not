import os

def get_dataset(dataset):
    dataset_name = dataset.split('/')[-1]
    dataset_path = f'./{dataset_name}'
    if(not os.path.exists(dataset_path)):
        os.mkdir(dataset_path)
    os.system(f"kaggle datasets download {dataset} --path {dataset_path} --unzip")

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
