import pandas as pd


title_akas = 'https://datasets.imdbws.com/title.akas.tsv.gz'

title_basics = 'https://datasets.imdbws.com/title.basics.tsv.gz'

title_crew = 'https://datasets.imdbws.com/title.crew.tsv.gz'

title_episode = 'https://datasets.imdbws.com/title.episode.tsv.gz'

title_principals = 'https://datasets.imdbws.com/title.principals.tsv.gz'

title_ratings = 'https://datasets.imdbws.com/title.ratings.tsv.gz'

name_basics = 'https://datasets.imdbws.com/name.basics.tsv.gz'
#Contient : primaryname, knownfortitles

dt1 = pd.read_csv(name_basics, sep='\t')
dt2 = pd.read_csv(title_basics, sep='\t')
print(dt2.iloc[0:3])
