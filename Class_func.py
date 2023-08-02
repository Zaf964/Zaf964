import requests
import json
import csv
import config
from datetime import datetime
"""ho to use my class:
    1- i need to define the match_id variable value
    2- Create an instance of the FootyStats class by passing the match_id to its constructor.
    - footy_stats = FootyStats(match_id)
    3- Call the get_everything() method on the footy_stats instance.
        This will fetch the data, process it, and store the statistics in JSON and CSV files.
     - footy_stats.get_everything()
    
"""
# match_id = "your_match_id_here"  # Replace "your_match_id_here" with the actual match ID
# footy_stats = FootyStats(match_id)
# footy_stats.get_everything()
id = config.ST
class FootyStats:
    referee_stats_found = False
    def __init__(self, match_id):
        self.match_id = match_id
        

    def get_everything(self):
        self.stats_url()
        self.get_stats()
        self.get_referee()

    def stats_url(self):
        url = f"https://app.footystats.org/{id}match_id={self.match_id}&dimension=season&include=stats"
        headers = {
            'user-agent': 'Dart/2.19 (dart:io)',
            'accept-encoding': 'gzip',
            'host': 'app.footystats.org'
            }
        response = requests.get(url, headers=headers, proxies=None)
        data = response.json()['data']
        with open("./file_store/stats.json", "w", encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def get_stats(self):
        with open("./file_store/stats.json", "r", encoding='utf-8') as file:
            data = json.load(file)
            Home_Team_list = [] 
            Away_Team_list = [] 
            team_a = data['team_a_stats']
            team_a_s = team_a['stats']
            team_a_ad = team_a_s['additional_info']
            team_b = data['team_b_stats']
            team_b_s = team_b['stats']
            team_b_ad = team_b_s['additional_info']
            home_a = data["home_name"]
            away_b = data["away_name"]
            
            H_Team_list = [
                {   
                    "Location": data["stadium_name"],
                    "Team": home_a,
                    "Team_Rrank": team_a.get("table_position"),
                    "Team_MP_at_Home": team_a_s.get("seasonMatchesPlayed_home"),
                    "Team_GF_at_Home": team_a_s.get("seasonScoredNum_home"),
                    "Team_GA_at_Home": team_a_s.get("seasonConcededNum_home"),
                    "Team_goals_mins_at_Home": team_a_s.get("seasonGoalsMin_home"),
                    "Team_GC_mins_at_Home": team_a_s.get("seasonConcededMin_home"),
                    "Team_goal_diff_at_Home": team_a_s.get("seasonGoalDifference_home"),
                    "Team_wins_at_Home": team_a_s.get("seasonWinsNum_home"),
                    "Team_draws_at_Home": team_a_s.get("seasonDrawsNum_home"),
                    "Team_losses_at_Home": team_a_s.get("seasonLossesNum_home"),
                    "Team_form_at_Home": team_a_ad.get("formRun_home"),
                    "Team_CS_at_Home": team_a_s.get("seasonCS_home"),
                    "Team_ScoredAVG_Home": team_a_s.get("seasonScoredAVG_home"),
                    "Team_Conceded_AVG_H": team_a_s.get("seasonConcededAVG_home"),
                    "Team_firstGoalScored_at_Home": team_a_s.get("firstGoalScored_home"),
                    "Team_FTS_at_Home": team_a_s.get("seasonFTSHT_home"),
                    "Team_FTS_HT_at_Home": team_a_s.get("seasonFTS_home"),
                    "Team_PPG_at_Home": team_a_s.get("seasonPPG_home"),
                    "Team_leadingAtHT_at_Home": team_a_s.get("leadingAtHT_home"),
                    "Team_drawingAtHT_at_Home": team_a_s.get("drawingAtHT_home"),
                    "Team_trailingAtHT_at_Home": team_a_s.get("trailingAtHT_home"),
                    "Team_GS_HT_at_Home": team_a_s.get("scoredGoalsHT_home"),
                    "Team_GC_HT_at_Home": team_a_s.get("concededGoalsHT_home"),
                    "Team_CS_HT_at_Home": team_a_s.get("seasonCSHT_home"),
                    "Team_GoalDiffHT_at_Home": team_a_s.get("GoalDifferenceHT_home"),
                    "Team_shotsTotal_at_Home": team_a_s.get("shotsTotal_home"),
                    "Team_shotsAVG_at_Home": team_a_s.get("shotsAVG_home"),
                    "Team_SoT_Total_at_Home": team_a_s.get("shotsOnTargetTotal_home"),
                    "Team_shotsOffTargetTotal_at_Home": team_a_s.get("shotsOffTargetTotal_home"),
                    "Team_SoT_AVG_at_Home": team_a_s.get("shotsOnTargetAVG_home"),
                    "Team_PossAVG_at_Home": team_a_s.get("possessionAVG_home"),
                    "Team_attacks_avg_at_Home": team_a_s.get("attacks_avg_home"),
                    "Team_dangerous_attacks_avg_at_Home": team_a_s.get("dangerous_attacks_avg_home"),
                    "Team_xg_for_avg_at_Home": team_a_s.get("xg_for_avg_home"),
                    "Team_xg_against_avg_at_Home": team_a_s.get("xg_against_avg_home"),
                    "Team_foulsAVG_at_Home": team_a_s.get("foulsAVG_home"),
                    "Team_offsidesAVG_at_Home": team_a_s.get("offsidesAVG_home"),
                    "Team_goal_kicks_team_avg_at_Home": team_a_ad.get("goal_kicks_team_avg_home"),
                    "Team_throwins_team_avg_at_Home": team_a_ad.get("throwins_team_avg_home"),
                    "Team_GF_at_Away": team_a_s.get("seasonScoredNum_away"),
                    "Team_GA_at_Away": team_a_s.get("seasonConcededNum_away"),
                    "Team_goals_minutes_at_Away": team_a_s.get("seasonGoalsMin_away"),
                    "Team_away_conceded_minutes_at_Away": team_a_s.get("seasonConcededMin_away"),
                    "Team_goal_difference_at_Away": team_a_s.get("seasonGoalDifference_away"),
                    "Team_wins_at_Away": team_a_s.get("seasonWinsNum_away"),
                    "Team_draws_at_Away": team_a_s.get("seasonDrawsNum_away"),
                    "Team_losses_at_Away": team_a_s.get("seasonLossesNum_away"),
                    "Team_form_at_Away": team_a_ad.get("formRun_away"),
                    "Team_CS_A": team_a_s.get("seasonCS_away"),
                    "Team_ScoredAVG_A": team_a_s.get("seasonScoredAVG_away"),
                    "Team_GA_AVG_A": team_a_s.get("seasonConcededAVG_away"),
                    "Team_firstGoalScored_at_Away": team_a_s.get("firstGoalScored_away"),
                    "Team_FTS_at_Away": team_a_s.get("seasonFTSHT_away"),
                    "Team_FTS_HT_at_Away": team_a_s.get("seasonFTS_away"),
                    "Team_PPG_at_Away": team_a_s.get("seasonPPG_away"),
                    "Team_leadingAtHT_at_Away": team_a_s.get("leadingAtHT_away"),
                    "Team_drawingAtHT_at_Away": team_a_s.get("drawingAtHT_away"),
                    "Team_trailingAtHT_at_Away": team_a_s.get("trailingAtHT_away"),
                    "Team_GF_HT_at_Away": team_a_s.get("scoredGoalsHT_away"),
                    "Team_GA_HT_at_Away": team_a_s.get("concededGoalsHT_away"),
                    "Team_CS_HT_at_Away": team_a_s.get("seasonCSHT_home"),
                    "Team_GD_HT_at_Away": team_a_s.get("GoalDifferenceHT_away"),
                    "Team_shotsTotal_at_Away": team_a_s.get("shotsTotal_away"),
                    "Team_shotsAVG_at_Away": team_a_s.get("shotsAVG_away"),
                    "Team_SoT_Total_at_Away": team_a_s.get("shotsOnTargetTotal_away"),
                    "Team_shotsOffTargetTotal_at_Away": team_a_s.get("shotsOffTargetTotal_away"),
                    "Team_SoT_AVG_at_Away": team_a_s.get("shotsOnTargetAVG_away"),
                    "Team_PossAVG_at_Away": team_a_s.get("possessionAVG_away"),
                    "Team_attacks_avg_at_Away": team_a_s.get("attacks_avg_away"),
                    "Team_dangerous_attacks_avg_at_Away": team_a_s.get("dangerous_attacks_avg_away"),
                    "Team_xg_for_avg_at_Away": team_a_s.get("xg_for_avg_away"),
                    "Team_xg_against_avg_at_Away": team_a_s.get("xg_against_avg_away"),
                    "Team_foulsAVG_at_Away": team_a_s.get("foulsAVG_away"),
                    "Team_offsidesAVG_at_Away": team_a_s.get("offsidesAVG_away"),
                    "Team_goal_kicks_team_avg_at_Away": team_a_ad.get("goal_kicks_team_avg_away"),
                    "Team_throwins_team_avg_at_Away": team_a_ad.get("throwins_team_avg_away")
                }
            ]
            
            A_Team_list = [
                    {   
                        "Location": data["stadium_name"],
                        "Team": away_b,
                        "Team_position": team_b.get("table_position"),
                        "Team_MP_at_Home": team_b_s.get("seasonMatchesPlayed_home"),
                        "Team_GF_at_Home": team_b_s.get("seasonScoredNum_home"),
                        "Team_GA_at_Home": team_b_s.get("seasonConcededNum_home"),
                        "Team_goals_mins_at_Home": team_b_s.get("seasonGoalsMin_home"),
                        "Team_GC_mins_at_Home": team_b_s.get("seasonConcededMin_home"),
                        "Team_goal_diff_at_Home": team_b_s.get("seasonGoalDifference_home"),
                        "Team_wins_at_Home": team_b_s.get("seasonWinsNum_home"),
                        "Team_draws_at_Home": team_b_s.get("seasonDrawsNum_home"),
                        "Team_losses_at_Home": team_b_s.get("seasonLossesNum_home"),
                        "Team_form_at_Home": team_b_ad.get("formRun_home"),
                        "Team_CS_at_Home": team_b_s.get("seasonCS_home"),
                        "Team_ScoredAVG_Home": team_b_s.get("seasonScoredAVG_home"),
                        "Team_Conceded_AVG_Home": team_b_s.get("seasonConcededAVG_home"),
                        "Team_firstGoalScored_at_Home": team_b_s.get("firstGoalScored_home"),
                        "Team_FTS_at_Home": team_b_s.get("seasonFTSHT_home"),
                        "Team_FTS_HT_at_Home": team_b_s.get("seasonFTS_home"),
                        "Team_PPG_at_Home": team_b_s.get("seasonPPG_home"),
                        "Team_leadingAtHT_at_Home": team_b_s.get("leadingAtHT_home"),
                        "Team_drawingAtHT_at_Home": team_b_s.get("drawingAtHT_home"),
                        "Team_trailingAtHT_at_Home": team_b_s.get("trailingAtHT_home"),
                        "Team_GS_HT_at_Home": team_b_s.get("scoredGoalsHT_home"),
                        "Team_GC_HT_at_Home": team_b_s.get("concededGoalsHT_home"),
                        "Team_CS_HT_at_Home": team_b_s.get("seasonCSHT_home"),
                        "Team_GoalDiffHT_at_Home": team_b_s.get("GoalDifferenceHT_home"),
                        "Team_shotsTotal_at_Home": team_b_s.get("shotsTotal_home"),
                        "Team_shotsAVG_at_Home": team_b_s.get("shotsAVG_home"),
                        "Team_SoT_Total_at_Home": team_b_s.get("shotsOnTargetTotal_home"),
                        "Team_shotsOffTargetTotal_at_Home": team_b_s.get("shotsOffTargetTotal_home"),
                        "Team_SoT_AVG_at_Home": team_b_s.get("shotsOnTargetAVG_home"),
                        "Team_PossAVG_at_Home": team_b_s.get("possessionAVG_home"),
                        "Team_attacks_avg_at_Home": team_b_s.get("attacks_avg_home"),
                        "Team_dangerous_attacks_avg_at_Home": team_b_s.get("dangerous_attacks_avg_home"),
                        "Team_xg_for_avg_at_Home": team_b_s.get("xg_for_avg_home"),
                        "Team_xg_against_avg_at_Home": team_b_s.get("xg_against_avg_home"),
                        "Team_foulsAVG_at_Home": team_b_s.get("foulsAVG_home"),
                        "Team_offsidesAVG_at_Home": team_b_s.get("offsidesAVG_home"),
                        "Team_goal_kicks_team_avg_at_Home": team_b_ad.get("goal_kicks_team_avg_home"),
                        "Team_throwins_team_avg_at_Home": team_b_ad.get("throwins_team_avg_home"),
                        "Team_GF_at_Away": team_b_s.get("seasonScoredNum_away"),
                        "Team_GA_at_Away": team_b_s.get("seasonConcededNum_away"),
                        "Team_goals_minutes_at_Away": team_b_s.get("seasonGoalsMin_away"),
                        "Team_away_conceded_minutes_at_Away": team_b_s.get("seasonConcededMin_away"),
                        "Team_goal_difference_at_Away": team_b_s.get("seasonGoalDifference_away"),
                        "Team_wins_at_Away": team_b_s.get("seasonWinsNum_away"),
                        "Team_draws_at_Away": team_b_s.get("seasonDrawsNum_away"),
                        "Team_losses_at_Away": team_b_s.get("seasonLossesNum_away"),
                        "Team_form_at_Away": team_b_ad.get("formRun_away"),
                        "Team_CS_A": team_b_s.get("seasonCS_away"),
                        "Team_ScoredAVG_A": team_b_s.get("seasonScoredAVG_away"),
                        "Team_GA_AVG_A": team_b_s.get("seasonConcededAVG_away"),
                        "Team_firstGoalScored_at_Away": team_b_s.get("firstGoalScored_away"),
                        "Team_FTS_at_Away": team_b_s.get("seasonFTSHT_away"),
                        "Team_FTS_HT_at_Away": team_b_s.get("seasonFTS_away"),
                        "Team_PPG_at_Away": team_b_s.get("seasonPPG_away"),
                        "Team_leadingAtHT_at_Away": team_b_s.get("leadingAtHT_away"),
                        "Team_drawingAtHT_at_Away": team_b_s.get("drawingAtHT_away"),
                        "Team_trailingAtHT_at_Away": team_b_s.get("trailingAtHT_away"),
                        "Team_GF_HT_at_Away": team_b_s.get("scoredGoalsHT_away"),
                        "Team_GA_HT_at_Away": team_b_s.get("concededGoalsHT_away"),
                        "Team_CS_HT_at_Away": team_b_s.get("seasonCSHT_home"),
                        "Team_GD_HT_at_Away": team_b_s.get("GoalDifferenceHT_away"),
                        "Team_shotsTotal_at_Away": team_b_s.get("shotsTotal_away"),
                        "Team_shotsAVG_at_Away": team_b_s.get("shotsAVG_away"),
                        "Team_SoT_Total_at_Away": team_b_s.get("shotsOnTargetTotal_away"),
                        "Team_shotsOffTargetTotal_at_Away": team_b_s.get("shotsOffTargetTotal_away"),
                        "Team_SoT_AVG_at_Away": team_b_s.get("shotsOnTargetAVG_away"),
                        "Team_PossAVG_at_Away": team_b_s.get("possessionAVG_away"),
                        "Team_attacks_avg_at_Away": team_b_s.get("attacks_avg_away"),
                        "Team_dangerous_attacks_avg_at_Away": team_b_s.get("dangerous_attacks_avg_away"),
                        "Team_xg_for_avg_at_Away": team_b_s.get("xg_for_avg_away"),
                        "Team_xg_against_avg_at_Away": team_b_s.get("xg_against_avg_away"),
                        "Team_foulsAVG_at_Away": team_b_s.get("foulsAVG_away"),
                        "Team_Team_offsidesAVG_at_Away": team_b_s.get("offsidesAVG_away"),
                        "Team_goal_kicks_team_avg_at_Away": team_b_ad.get("goal_kicks_team_avg_away"),
                        "Team_throwins_team_avg_at_Away": team_b_ad.get("throwins_team_avg_away")
                    }
                ]    
            
            Home_Team_list.append(H_Team_list)
            Away_Team_list.append(A_Team_list)
            
            home_f = json.dumps(H_Team_list, indent=4, ensure_ascii=False)
            away_f = json.dumps(A_Team_list, indent=4, ensure_ascii=False)
            with open(f"./file_store/{home_a}.json", "w", encoding='utf-8') as file:
                file.write(home_f)
            with open(f"./file_store/{away_b}.json", "w", encoding='utf-8') as file:
                file.write(away_f)
            home_stats_data = json.loads(home_f)
            away_stats_data = json.loads(away_f)
            home_file = f"./file_store/{home_a}.csv"
            away_file = f"./file_store/{away_b}.csv"
            self.write_to_csv(home_stats_data, home_file)
            self.write_to_csv(away_stats_data, away_file)

    def write_to_csv(self, data, filename):
        keys = data[0].keys()
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)

    def get_referee(self):
        with open("./file_store/stats.json", "r", encoding='utf-8') as file:
            data = json.load(file)
        var = data['refereeID']
        """Setting a boolean to check if i got 'refereeID' or not"""
        if var is None:
            FootyStats.referee_stats_found = False
        else:
            FootyStats.referee_stats_found = True
        url = f"https://api.football-data-api.com/referee?key=example&referee_id={var}"
        headers = {
            'user-agent': 'Dart/2.19 (dart:io)',
            'accept-encoding': 'gzip',
            'host': 'app.footystats.org'
            }

        response = requests.get(url, headers=headers, proxies=None)
        data = response.json()['data']

        """Filter data for the last three seasons"""
        last_three_seasons_data = []
        for item in data:
            if item["season"] in ["2020/2021", "2021/2022", "2022/2023"]:
                last_three_seasons_data.append(item)

        # Define the CSV file path
        csv_file_path = "./file_store/referee.csv"

        # Define the keys to extract
        keys_to_extract = [
            "season",
            "appearances_overall",
            "wins_home",
            "wins_away",
            "draws_overall",
            "wins_per_home",
            "wins_per_away",
            "draws_per",
            "btts_overall",
            "btts_percentage",
            "goals_overall",
            "goals_home",
            "goals_away",
            "goals_per_match_overall",
            "goals_per_match_home",
            "goals_per_match_away",
            "penalties_given_overall",
            "penalties_given_home",
            "penalties_given_away",
            "penalties_given_per_match_overall",
            "penalties_given_per_match_home",
            "penalties_given_per_match_away",
            "penalties_given_percentage_overall",
            "penalties_given_percentage_home",
            "penalties_given_percentage_away",
            "cards_overall",
            "cards_home",
            "cards_away",
            "cards_per_match_overall",
            "cards_per_match_home",
            "cards_per_match_away",
            "over05_cards_overall",
            "over15_cards_overall",
            "over25_cards_overall",
            "over35_cards_overall",
            "over45_cards_overall",
            "over55_cards_overall",
            "over65_cards_overall",
            "over05_cards_per_match_overall",
            "over15_cards_per_match_overall",
            "over25_cards_per_match_overall",
            "over35_cards_per_match_overall",
            "over45_cards_per_match_overall",
            "over55_cards_per_match_overall",
            "over65_cards_per_match_overall",
            "over05_cards_percentage_overall",
            "over15_cards_percentage_overall",
            "over25_cards_percentage_overall",
            "over35_cards_percentage_overall",
            "over45_cards_percentage_overall",
            "over55_cards_percentage_overall",
            "over65_cards_percentage_overall",
            "yellow_cards_overall",
            "red_cards_overall",
            "min_per_goal_overall",
            "min_per_card_overall"
        ]

        # Write data to CSV file
        with open(csv_file_path, mode="w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys_to_extract)
            writer.writeheader()
            for item in last_three_seasons_data:
                filtered_item = {key: item[key] for key in keys_to_extract}
                writer.writerow(filtered_item)

