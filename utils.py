import numpy as np
import pandas as pd


def add_engineered_features(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    screen_minutes = df['daily_screen_time_hours'] * 60

    # % of daily screen time that happens right before sleep
    df['night_screen_ratio'] = np.where(
        screen_minutes > 0,
        df['phone_usage_before_sleep_minutes'] / screen_minutes,
        0
    )

    # sleep duration relative to total screen exposure
    df['rest_to_screen_ratio'] = df['sleep_duration_hours'] / (df['daily_screen_time_hours'] + 1)

    return df


STRESS_MIN, STRESS_MAX = 1, 10
FATIGUE_MIN, FATIGUE_MAX = 1, 10

PRODUCTIVITY_MIN = 11 - FATIGUE_MAX
PRODUCTIVITY_MAX = 11 - FATIGUE_MIN

def compute_derived_productivity(mental_fatigue_score):
    """Higher fatigue -> lower productivity. Inverse relationship."""
    return 11 - mental_fatigue_score


def to_percentage(value, min_val, max_val):
    """Min-max normalize a raw score to a 0-100% scale."""
    return round((value - min_val) / (max_val - min_val) * 100, 2)



def assign_age_group(age):
    """Bucket age into 15-year benchmark brackets (dataset spans 18-59)."""
    if age < 18:
        return '18-32'
    elif 18 <= age <= 32:
        return '18-32'   # 15-year span (18 to 32 inclusive)
    elif 33 <= age <= 47:
        return '33-47'   # 15-year span (33 to 47 inclusive)
    else:
        return '48-59'   # Safely targets the remaining 48-59 cohort and fallbacks

