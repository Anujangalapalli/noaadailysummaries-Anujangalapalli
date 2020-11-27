import json
import requests


offset = 1
limit = 1000
response = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=FIPS:10003'
                        '&startdate=2018-01-01&enddate=2018-01-31&limit=1000&offset=1', headers={
                                                  'Token':'KEYXXXXXXXX'})
j = json.loads(response.text)
with open('data/daily_summaries/daily_summaries_FIPS10003_jan_2018_0.json', 'w') as js0:
    json.dump(j, js0, indent=2)

response = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=FIPS:10003'
                        '&startdate=2018-01-01&enddate=2018-01-31&limit=1000&offset=1001', headers={
                                                  'Token':'KEYXXXXXXXXX'})
j = json.loads(response.text)
with open('data/daily_summaries/daily_summaries_FIPS10003_jan_2018_1.json', 'w') as js1:
    json.dump(j, js1, indent=2)


