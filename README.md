## Credit Risk Analytics

End-to-end credit risk modeling with data download, cleaning, and baseline modeling in a Jupyter notebook. Utilities included for logging, Kaggle dataset access, and batch loading of compressed files.

### Features
- **Data access**: Download Kaggle datasets via `kagglehub`
- **Config**: Simple `.env`-based Kaggle credential management
- **Utilities**: Load multiple `.gz`/`.gzip` files into DataFrames
- **Modeling**: Baseline model in `main.ipynb` (Random Forest) with metrics (ROC AUC, classification report, confusion matrix)

### Project structure
- `main.ipynb` — exploratory analysis and modeling workflow
- `config.py` — `setup_kaggle_credentials(logger)` reads `KAGGLE_USERNAME`, `KAGGLE_KEY` from `.env`
- `data_utils.py` — `download_dataset(logger, dataset_name)`, `load_data_files_to_dataframes(logger, dataset_path)`
- `logger.py` — `setup_logger()` for unified logging
- `pyproject.toml` — dependencies and tooling (supports `uv`)
- `uv.lock` — locked dependency versions

### Getting started

#### Prerequisites
- Python ≥ 3.8
- macOS/Linux/Windows shell
- Kaggle account and API key

#### Clone
```bash
git clone https://github.com/<username>/credit-risk-analytics.git
cd credit-risk-analytics
```

#### Environment setup

- Using `uv`:
```bash
uv sync
uv run python -V
```

### Configure Kaggle credentials
Create a `.env` in the project root:
```bash
cat > .env << 'EOF'
KAGGLE_USERNAME=kaggle_username
KAGGLE_KEY=kaggle_api_key
EOF
```

### Usage

#### Launch Jupyter
- With `uv`:
```bash
uv run jupyter lab
```
- With `pip`/venv:
```bash
jupyter lab
```
Open `main.ipynb` and run cells top-to-bottom.

#### Programmatic example (Python)
```python
from logger import setup_logger
from config import setup_kaggle_credentials
from data_utils import download_dataset, load_data_files_to_dataframes

logger = setup_logger()
username, key = setup_kaggle_credentials(logger)

# Example Kaggle dataset slug 
dataset = "owner/dataset-name"  
dataset_path = download_dataset(logger, dataset)

dfs = load_data_files_to_dataframes(logger, dataset_path)
for name, df in dfs.items():
    logger.info(f"{name}: {df.shape}")
```

### Modeling notes
- Model in `main.ipynb`: Random Forest.
- Evaluate with ROC AUC, classification report, confusion matrix.
- For imbalanced data, considering:
  - Class weights (`class_weight='balanced'` for Random Forest)

### Development
- Formatting/linting (if installed):
```bash
uv run black .
uv run flake8
```
- Tests (placeholder):
```bash
uv run pytest -q
```

### Environment variables
- `KAGGLE_USERNAME`: Kaggle username
- `KAGGLE_KEY`: Kaggle API key

### Troubleshooting
- “Kaggle credentials not found”: ensure `.env` exists and values are correct, then restart the kernel.
- Notebook cannot find modules: ensure you launched Jupyter from the project’s environment.
- Missing packages: run `uv sync` (or `pip install -e .`).
