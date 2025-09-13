# AI28 Project: Topic 3 - Income Level Prediction

The goal of this group project (team of three) is to address a machine learning problem using a real-world dataset.

## Project Architecture

### Jupyter Notebooks

The project contains two Jupyter notebooks:

- **`AED.ipynb`**: contains all code related to exploratory data analysis.  
- **`entrainement.ipynb`**: contains all code related to preprocessing, training, and evaluation of machine learning models.  

**Note**: Running the notebook `entrainement.ipynb` may take a significant amount of time, especially for models such as AdaBoosting, Stacking, and SVM. Execution time on a MacBook Air M1: ~62 minutes.  

### Python File

A Python file `AED_utils.py` contains code required for executing the notebook `AED.ipynb`. Keep this file at the project root.  

### Other Files

- **`requirements.txt`**: to install dependencies.  
- **`/figures`**: folder containing all generated figures in `.png` format.  
- **`ai28-rapport-bcv.pdf`**: the written report in `.pdf` format.  

---

## Installation

This project is a Jupyter Notebook containing analyses and Python code.  
All required dependencies are listed in `requirements.txt`.

1. **Clone the repository:**
   ```bash
   git clone https://gitlab.utc.fr/ai28_tp_projet/ai28-projet.git
   cd your-project
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies:**
   Run the following at the project root:
   ```bash
   # Ensure you are inside the virtual environment
   pip install -r requirements.txt
   ```

4. **Launch Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

### Requirements

- Python 3.7 or higher  
- pip  
- Jupyter Notebook  
- (optional) virtualenv  

---

## Group Members

| Group  -  
BCV    |
| ---------------- |
| Alexandre Bidaux |
| Julie Chartier   |
| Quentin Valakou  |

---

## Data Retrieval

There are two ways to retrieve the dataset used in this project:  
- Download it from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/2/adult)  
- Or load it directly via the Python library:

```python
from ucimlrepo import fetch_ucirepo

# fetch dataset
adult = fetch_ucirepo(id=2)

# data (as pandas dataframes)
X = adult.data.features
y = adult.data.targets

# metadata
print(adult.metadata)

# variable information
print(adult.variables)
```

In this project, we chose to download the dataset from the UCI website.  

---

## Dataset Files

The dataset files are structured as follows:

```
.
├── adult.data        : training dataset in CSV format (comma-separated)
├── adult.names       : file providing context and descriptions of the dataset and preprocessing
├── adult.test        : test dataset in CSV format (comma-separated)
├── Index             : lists files, modification dates, and sizes
└── old.adult.names   : previous version of adult.names
```

---

## Sources

- [Adult Dataset - UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/2/adult)  
