# LLM Classification Finetuning

This repository contains a small notebook-based workflow for exploring and visualizing the Kaggle LLM classification finetuning dataset.

## Project Structure

- data/ - contains the competition datasets
- notebooks/playground/ - Jupyter notebooks for analysis and visualization

## Requirements

Make sure you have:

- Python 3.9+ 
- pip
- A Kaggle account with access to the competition

## Setup

1. Clone the repository

```bash
git clone <your-repo-url>
cd LLM Classification Finetuning
```

2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install the required Python packages

```bash
pip install pandas matplotlib seaborn jupyter
```

4. Install the Kaggle CLI

```bash
pip install kaggle
```

5. Configure Kaggle API access

- Sign in to Kaggle
- Go to your account settings
- Download the API token file named kaggle.json
- Move it to:

```bash
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json
```

6. Download the competition data

```bash
mkdir -p data
kaggle competitions download -c llm-classification-finetuning -p data
```

7. Unzip the downloaded file

```bash
cd data
unzip llm-classification-finetuning.zip
cd ..
```

After this step, you should have files such as:

- data/train.csv
- data/test.csv

## Run the Notebook

Start Jupyter Notebook:

```bash
jupyter notebook
```

Then open the notebook in:

- notebooks/playground/jd.ipynb

## Notes

- The notebook expects the dataset files to be available under the data folder relative to the notebook location.
- If you want to keep the project reproducible, you can later add a requirements.txt file with the installed packages.

## Troubleshooting

If Kaggle download fails:

- Make sure you have accepted the competition rules on Kaggle
- Confirm that your kaggle.json file is in the correct location
- Verify that the competition name is exactly: llm-classification-finetuning
