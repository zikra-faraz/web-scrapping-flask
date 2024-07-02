# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 12:25:41 2021

@author: win10
"""

from autoscraper import AutoScraper
github_url="https://github.com/topics/3d"

wanted_list=["mrdoob","three.js"]

scraper=AutoScraper()
result=scraper.build(github_url,wanted_list)

grouped_results=scraper.get_result_similar(github_url,grouped=True)

rule_username = list(grouped_results.keys())[0]  # Assuming the first rule is for the username
rule_repository = list(grouped_results.keys())[1]
# scraper.set_rule_aliases({'rule_i70w':'Username','rule_a7ra':'Repository'})
# scraper.keep_rules(['rule_i70w','rule_a7ra'])
# scraper.save('github_topics')
scraper.set_rule_aliases({rule_username:'Username',rule_repository:'Repository'})
scraper.keep_rules([rule_username,rule_repository])
scraper.save('github')
