# src/config.py
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DATA_PATH = os.path.join(DATA_DIR, "vehicle_maintenance_data.csv")
PROCESSED_DATA_PATH = os.path.join(DATA_DIR, "vehicle_maintenance_processed.csv")

MODEL_DIR = os.path.join(BASE_DIR, "models")
os.makedirs(MODEL_DIR, exist_ok=True)

MODEL_PATH = os.path.join(MODEL_DIR, "xgboost_best.pkl")
SCALER_PATH = os.path.join(MODEL_DIR, "scaler.pkl")

# Constants
RANDOM_STATE = 42
TEST_SIZE = 0.20
REFERENCE_DATE = "2025-07-01"  # You can change this to today's date if you want

NUMERIC_FEATURES = [
    'Mileage', 'Reported_Issues', 'Vehicle_Age', 'Engine_Size',
    'Odometer_Reading', 'Insurance_Premium', 'Service_History',
    'Accident_History', 'Fuel_Efficiency', 'days_since_last_service',
    'days_to_warranty_end', 'condition_score'
]