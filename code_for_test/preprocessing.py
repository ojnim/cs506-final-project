import pandas as pd


#fMRI data

data_fMRI = pd.read_csv("./data_for_test/fMRI_data_sample.csv")
data_fMRI.head(5)

lang_data = data_fMRI[data_fMRI['Task'] == ("LanguageControl")]
cog_data = data_fMRI[data_fMRI['Task'] == ("CognitiveControl")]

voxel_avg_lang = (
    lang_data.groupby(['X', 'Y', 'Z'])['Voxel Value']
    .mean()
    .reset_index()
    .rename(columns={'Voxel Value': 'voxel_avg'})
)

voxel_avg_cog = (
    cog_data.groupby(['X', 'Y', 'Z'])['Voxel Value']
    .mean()
    .reset_index()
    .rename(columns={'Voxel Value': 'voxel_avg'})
)

voxel_avgs = pd.merge(
    voxel_avg_lang,
    voxel_avg_cog,
    on=['X', 'Y', 'Z'],
    suffixes=('_lang', '_cog')
)

voxel_avgs["voxel_diff"] = voxel_avgs["voxel_avg_cog"] - voxel_avgs["voxel_avg_lang"]

lang_voxel = voxel_avgs[voxel_avgs["voxel_avg_lang"] > voxel_avgs["voxel_avg_cog"]]
cog_voxel = voxel_avgs[voxel_avgs["voxel_avg_lang"] < voxel_avgs["voxel_avg_cog"]]

data_sub = data_fMRI.rename(columns={'Subject':"participant_id"})



#participants & behavioral data

data_participants = pd.read_csv("./data_for_analysis/participants.tsv" , sep='\t')
data_participants = pd.DataFrame(data_participants)

Language_RT = ["RT_L1S","RT_L1NS","RT_L2S","RT_L2NS"]
Language_ER = ["ER_L1S","ER_L1NS","ER_L2S","ER_L2NS"]


participants_lang = data_participants[ ['participant_id', 'age', 'AoA',"CET_4_score"]+Language_RT+Language_ER]
participants_cog = data_participants[ ['participant_id', 'age', 'AoA', "raven_score"]+Language_RT+Language_ER]



#merge

lang = pd.merge(
    participants_lang,
    data_sub,
    on=["participant_id"],
)

lang = lang[lang['Task'] == 'LanguageControl'].drop(columns=['Task'])

lang_d = pd.merge(
    lang,
    lang_voxel,
    on=["X","Y","Z"],
)

cog = pd.merge(
    participants_cog,
    data_sub,
    on=["participant_id"],
)

cog = cog[cog['Task'] == 'CognitiveControl'].drop(columns=['Task'])

cog_d = pd.merge(
    cog,
    cog_voxel,
    on=["X","Y","Z"],
)



#convert to data file for training
lang_d.to_csv('./data_for_test/LanguageControl_data.csv', index=False)
cog_d.to_csv('./data_for_test/CognitiveControl_data.csv', index=False)