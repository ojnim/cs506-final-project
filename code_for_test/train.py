import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import root_mean_squared_error, r2_score

tasks = ["LanguageControl","CognitiveControl"]

lang = pd.read_csv('./data_for_analysis/LanguageControl_data.csv')
cog = pd.read_csv('./data_for_analysis/CognitiveControl_data.csv')

participants_pool = cog['participant_id'].unique().tolist()

train_participants, test_participants = train_test_split(
    participants_pool, test_size=0.2, random_state=42
)

#Brain Region Analysis