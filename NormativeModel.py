import pandas as pd

# read in the files.
norm_demographics = pd.read_csv('data/camcan_demographics.csv',
                                sep= ",",
                                index_col = 0)
norm_features = pd.read_csv('data/camcan_features.csv',
                            sep=",",
                            index_col = 0)

# check columns through print [there are other better options]
print(norm_demographics)
print(norm_features)

# find overlap in terms of participants between norm_sample_features and
# norm_sample_demographics

norm_demographics_features = pd.concat([norm_demographics, norm_features],
                                       axis = 1,
                                       join = 'inner') # inner checks overlap
                                                       # outer combines
print(norm_demographics_features)

