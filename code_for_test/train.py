import pandas as pd

from sklearn.model_selection import train_test_split
import statsmodels.api as sm

tasks = ["LanguageControl","CognitiveControl"]

lang = pd.read_csv('./data_for_analysis/LanguageControl_data.csv')
cog = pd.read_csv('./data_for_analysis/CognitiveControl_data.csv')

participants_pool = cog['participant_id'].unique().tolist()

train_participants, test_participants = train_test_split(
    participants_pool, test_size=0.2, random_state=42
)

#Brain Region Analysis
# Group by spatial coordinates (voxel region)
voxel_groups = lang.groupby(['X', 'Y', 'Z'])

# Store region-level regression results
region_results = []

# Features to use
predictor_cols = ['age', 'AoA', 'CET_4_score','RT_L1S', 'RT_L1NS', 'RT_L2S', 'RT_L2NS','ER_L1S', 'ER_L1NS', 'ER_L2S', 'ER_L2NS']

train_df = lang[lang['participant_id'].isin(train_participants)].copy()
test_df = lang[lang['participant_id'].isin(test_participants)].copy()

# Loop over voxel regions
for (x, y, z), group in voxel_groups:
    if len(group) < 10:
        continue  # skip very small groups to avoid unstable models

    train_group = train_df[(train_df['X'] == x) & (train_df['Y'] == y) & (train_df['Z'] == z)]
    test_group = test_df[(test_df['X'] == x) & (test_df['Y'] == y) & (test_df['Z'] == z)]

    if train_group.empty or test_group.empty:
        print(f"Skipping empty group at ({x}, {y}, {z})")
        continue

     # Extract features and target variables for both train and test sets
    X_train = train_group[predictor_cols]
    X_test = test_group[predictor_cols]

    X_train, X_test = X_train.align(X_test, join='outer', axis=1, fill_value=0)

    y_train = train_group['Voxel Value']
    y_test = test_group['Voxel Value']

    if y_train.nunique() == 1:
        print(f"Skipping constant target at ({x}, {y}, {z})")
        continue


    # Fit model on the training data
    model = sm.OLS(y_train, X_train).fit()

    # Predict on the test set
    y_pred = model.predict(X_test)

    # Compute R^2 on test data
    r2_test = model.rsquared

    # Get p-value for 'AoA'
    p_AoA = model.pvalues.get('AoA', None)

    # Get p-value for 'CET_4_score'
    p_CET_4 = model.pvalues.get('CET_4_score', None)


    region_results.append({
        'X': x,
        'Y': y,
        'Z': z,
        'R^2': r2_test,
        'p_AoA': p_AoA,
        'p_CET_4_score': p_CET_4,
        'n_obs': len(group)
    })

# Create DataFrame with results
lang_region_df = pd.DataFrame(region_results)

lang_region_df.to_csv('lang_region_df.csv')

# Group by spatial coordinates (voxel region)
voxel_groups = cog.groupby(['X', 'Y', 'Z'])

# Store region-level regression results
region_results = []

# Features to use
predictor_cols = ['age','AoA', 'raven_score', 'RT_L1S', 'RT_L1NS', 'RT_L2S', 'RT_L2NS',
                  'ER_L1S', 'ER_L1NS', 'ER_L2S', 'ER_L2NS']

train_df = cog[cog['participant_id'].isin(train_participants)].copy()
test_df = cog[cog['participant_id'].isin(test_participants)].copy()

# Loop over voxel regions
for (x, y, z), group in voxel_groups:
    if len(group) < 10:
        continue  # skip very small groups to avoid unstable models

    train_group = train_df[(train_df['X'] == x) & (train_df['Y'] == y) & (train_df['Z'] == z)]
    test_group = test_df[(test_df['X'] == x) & (test_df['Y'] == y) & (test_df['Z'] == z)]

    if train_group.empty or test_group.empty:
        print(f"Skipping empty group at ({x}, {y}, {z})")
        continue

     # Extract features and target variables for both train and test sets
    X_train = train_group[predictor_cols]
    X_test = test_group[predictor_cols]

    X_train, X_test = X_train.align(X_test, join='outer', axis=1, fill_value=0)

    y_train = train_group['Voxel Value']
    y_test = test_group['Voxel Value']

    if y_train.nunique() == 1:
        print(f"Skipping constant target at ({x}, {y}, {z})")
        continue


    # Fit model on the training data
    model = sm.OLS(y_train, X_train).fit()

    # Predict on the test set
    y_pred = model.predict(X_test)

    # Compute R^2 on test data
    r2_test = model.rsquared

    # Get p-value for 'raven_score'
    p_raven = model.pvalues.get('raven_score', None)

    # Get p-value for 'AoA'
    p_AoA = model.pvalues.get('AoA', None)


    region_results.append({
        'X': x,
        'Y': y,
        'Z': z,
        'R^2': r2_test,
        'p_raven': p_raven,
        'p_AoA': p_AoA,
        'n_obs': len(group)
    })

# Create DataFrame with results
cog_region_df = pd.DataFrame(region_results)

cog_region_df.to_csv('cog_region_df.csv')
