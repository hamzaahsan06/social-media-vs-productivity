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