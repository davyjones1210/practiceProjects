#pip install nba_api
#pip install pandas
#pip install requests
#Youtube tutorial: https://www.youtube.com/watch?v=odCb5jczq9Y&ab_channel=LearnWithJabe

headers  = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-token': 'true',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'x-nba-stats-origin': 'stats',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

#Importing the packages

import pandas as pd
import requests
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo

#Now getting full list of players
nba_players = players.get_players()
df = pd.DataFrame(nba_players)
#print(df.sample(5))

#get full list of player_ids that are active

#active_player_ids = df.loc[(df['is_active'] == True), 'id'].to_list()
#print(active_player_ids)
active_players = players.get_active_players()
#print(type(active_players))
# for person in active_players:
#     print(person)

# nba_player_id = '1628389'
# player_info = commonplayerinfo.CommonPlayerInfo(player_id=nba_player_id, headers=headers, timeout=100)
# df = player_info.common_player_info.get_data_frame()
# print(df)


# create function that gets player info data
def get_player_data(nba_player_id):
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=nba_player_id, headers=headers,timeout=100)
    df = player_info.common_player_info.get_data_frame()
    return df

sample_player_ids = [
    '203500',
    '1628389',
    '200746',
    '1629734',
    '1629638',
    '1628960',
    '1628386',
    '1628443',
    '202329',
    '1626147',
    '203937',
    '201583',
    '203507',
    '1628961',
    '203648',
    '2546',
    '1628384',
    '1627853',
    '2772',
    '201571',
]

player_data = []
# for nba_player_id in sample_player_ids:
# # for nba_player_id in active_player_ids: # remove this when ready to run for full season
#     #print(nba_player_id)
#     player_info = get_player_data(nba_player_id)
#     player_data.append(player_info)
    #time.sleep(3)

#final_df = pd.concat(player_data, ignore_index=True)

#print(final_df.sample(20))

from nba_api.stats.static import teams

# Get all teams.
nba_teams = teams.get_teams()
df = pd.DataFrame(nba_teams)
#print(df)

from nba_api.stats.endpoints import playercareerstats
# Bam Adebayo
career = playercareerstats.PlayerCareerStats(player_id='1628389')
df = career.get_data_frames()[0]
#print(df)

from nba_api.stats.endpoints import leaguegamefinder
# get game logs from the reg season
gamefinder = leaguegamefinder.LeagueGameFinder(season_nullable='2020-21',
                                              league_id_nullable='00',
                                              season_type_nullable='Regular Season')
games = gamefinder.get_data_frames()[0]
#print(games.head())
#print(games)

# get a list of the distinct game_ids
game_ids = games['GAME_ID'].unique().tolist()
#print(game_ids)

game_id = '0022000776'
from nba_api.stats.endpoints import playbyplayv2
pbp = playbyplayv2.PlayByPlayV2(game_id)
pbp = pbp.get_data_frames()[0]
#print(pbp.head())
#print(pbp.tail(10))

from nba_api.stats.endpoints import boxscoretraditionalv2

player_stat_data = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id=game_id)
stats_df = player_stat_data.get_data_frames()[0]
#print(stats_df.tail())

# create function that gets box score data based on game_ids
def get_box_score_data(game_id):
    player_stat_data = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id=game_id, headers=headers, timeout=100)
    df = player_stat_data.player_stats.get_data_frame()
    return df
# using this for testing purposes only
sample_game_ids = [
    '0022001070',
    '0022001077',
    '0022001068',
    '0022001074']

boxscores = []
#for game_id in game_ids: # remove this when ready to run for full season
for game_id in sample_game_ids:
    boxscore_data = get_box_score_data(game_id)
    boxscores.append(boxscore_data)

final_df = pd.concat(boxscores, ignore_index=True)
#print(final_df.sample(10))

# create function that gets pbp logs from the 2020-21 season
def get_data(game_id):
    play_by_play_url = "https://cdn.nba.com/static/json/liveData/playbyplay/playbyplay_"+game_id+".json"
    response = requests.get(url=play_by_play_url, headers=headers).json()
    play_by_play = response['game']['actions']
    df = pd.DataFrame(play_by_play)
    df['gameid'] = game_id
    return df
# using this for testing purposes only
sample_game_ids = [
    '0022001070',
    '0022001077',
    '0022001068',
    '0022001074']
pbpdata = []
#for game_id in game_ids: # remove this when ready to run for full season
for game_id in sample_game_ids:
    game_data = get_data(game_id)
    pbpdata.append(game_data)

final_df = pd.concat(pbpdata, ignore_index=True)
print(final_df.sample(10))


