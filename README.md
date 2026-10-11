# Predictive Vehicle Maintenance and Failure Detection

A machine-learning project that estimates whether a vehicle may need maintenance using vehicle usage, service history, and component-condition features. It includes a Streamlit demo, preprocessing and EDA scripts, model-training code, saved model artifacts, and example visualizations.

> **Important:** This is an educational demonstration built with the included dataset. Predictions are not a substitute for inspection by a qualified mechanic.

## Features

- Data preprocessing and feature engineering
- Exploratory data analysis (EDA) with saved charts
- Model training and comparison using XGBoost, LightGBM, and Random Forest
- Evaluation with classification reports, ROC-AUC, and confusion matrices printed during training
- Streamlit interface for entering vehicle details and viewing a maintenance-risk prediction
- SHAP-based feature explanation in the demo

## Project structure

```text
predictive-vehicle-maintenance/
├── app.py
├── data/
│   ├── feature_names.csv
│   ├── vehicle_maintenance_data.csv
│   └── vehicle_maintenance_processed.csv
├── models/
│   ├── scaler.pkl
│   └── xgboost_best.pkl
├── notebooks/
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── data_loader.py
│   └── preprocess.py
├── run_eda.py
├── run_preprocess.py
├── run_training.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

- Python 3.10 or newer recommended
- pip

## Setup (Windows PowerShell)

Run these commands from the project root:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks activation, you can install packages with `.venv\Scripts\python.exe -m pip install -r requirements.txt` and run commands using `.venv\Scripts\python.exe`.

## Run the Streamlit demo

```powershell
streamlit run app.py
```

The app uses the saved model and scaler under `models/` and feature names under `data/feature_names.csv`.

## Rebuild the data and model

Run these in order from the project root:

```powershell
python run_preprocess.py
python run_eda.py
python run_training.py
```

Training prints model evaluation reports, ROC-AUC values, and confusion matrices. The model selected by the training script is saved to the configured model path in `src/config.py`.

## Dataset and artifacts

The repository includes the CSV data and pre-trained artifacts used by the demo. Check the dataset's original license and redistribution terms before making the repository public. If you cannot redistribute it, remove the CSVs and document how to obtain the dataset instead.

Pickle (`.pkl`) model files should only be loaded from sources you trust. Re-training the models may produce different results depending on the installed package versions and environment.

## Limitations

- The app uses fixed/default values for some fields that are not collected in the form; predictions should be treated as a prototype.
- The selected model filename is retained for compatibility with the included demo; the training script selects the model based on class-1 recall.
- No performance figures are claimed here. Run `python run_training.py` to generate evaluation results for your environment.

## License

Add a license only after confirming that you have the right to license both the code and any included data.
