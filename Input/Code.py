#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 22:04:50 2020
@author: alexislacabane

This work aims at flagging overpriced ads in order to report them 
"""

import os
import numpy as np
import pandas as pd
import requests as r
from bs4 import BeautifulSoup
import time
import re
import webbrowser

headers= {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding':'gzip, deflate, br',
'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
'cache-control': 'no-cache',
'cookie': 'realytics=1; __uzma=321c5d66-2d07-7f7f-aea7-732c8ed886c0; __uzmb=1579787564; visitId=1579787566635-1253934218; atuserid=%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%229e4506e1-117c-4d44-a000-95673428ed2e%22%2C%22options%22%3A%7B%22end%22%3A%222021-02-23T13%3A52%3A46.674Z%22%2C%22path%22%3A%22%2F%22%7D%7D; theshield_cmp_consent={%22consentString%22:%22eyJhdWRpZW5jZSI6WyIqIl0sInNvY2lhbCI6WyIqIl0sImFuYWx5dGljcyI6WyIqIl0sImlhYiI6W3siaWQiOjEsInZlbmRvcnMiOlsiKiJdfSx7ImlkIjoyLCJ2ZW5kb3JzIjpbIioiXX0seyJpZCI6MywidmVuZG9ycyI6WyIqIl19LHsiaWQiOjQsInZlbmRvcnMiOlsiKiJdfSx7ImlkIjo1LCJ2ZW5kb3JzIjpbIioiXX1dLCJhZHMiOlsiKiJdfQ%253D%253D%22}; theshield_consent={%22consentString%22:%22BOtoHPoOtoHPoCyABBFRAk-AAAAXyABgACAvgA%22}; _gcl_au=1.1.1438154564.1579787569; bannerCookie=1; AMCVS_366134FA53DB27860A490D44%40AdobeOrg=1; _ga=GA1.2.32670881.1579787567; _gid=GA1.2.313422867.1579787570; s_ecid=MCMID%7C12049691462856099050997333144816585256; c_m=undefinedwww.google.comNatural%20Search; stack_ch=%5B%5B%27SEO%2520Non%2520Branded%27%2C%271579787569751%27%5D%5D; s_cc=true; _hjid=235ec1fe-5f66-4282-b707-98912e022f29; mics_uaid=web:1056:3281d44e-0309-4b6a-8834-182274e1823e; uid=3281d44e-0309-4b6a-8834-182274e1823e; mics_vid=8190383032; mics_lts=1579787570370; mics_vid=8190383032; mics_lts=1579787570370; __gads=ID=189ceb9e21b92917:T=1579787582:S=ALNI_MazKPGamwVlZrJHbkfs6KDOdVt1HQ; ry_ry-s3oa268o_realytics=eyJpZCI6InJ5XzY3MjFDQjBGLTRGNTQtNDEzMi05NzZDLTUwMjUxQjA3NDdDRCIsImNpZCI6bnVsbCwiZXhwIjoxNjExMzIzNTY5ODAzLCJjcyI6MX0%3D; ASP.NET_SessionId=esm3ptbpawhhxbjrnpok5kvw; ABtestCreditImmo=ABtestCreditImmo_VersionB; SearchAnnDep=75; AA_Test_House=c; AA_Test_g=h; kameleoonVisitorCode=_js_ccvjcedigfn39ggr; s_visit=1; s_dl=1; realytics=1; AMCV_366134FA53DB27860A490D44%40AdobeOrg=1099438348%7CMCIDTS%7C18285%7CMCMID%7C12049691462856099050997333144816585256%7CMCAAMLH-1580392369%7C6%7CMCAAMB-1580466048%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1579868448s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C2.1.0; s_sq=%5B%5BB%5D%5D; s_getNewRepeat=1579862216527-Repeat; __uzmd=1579862217; ry_ry-s3oa268o_so_realytics=eyJpZCI6InJ5XzY3MjFDQjBGLTRGNTQtNDEzMi05NzZDLTUwMjUxQjA3NDdDRCIsImNpZCI6bnVsbCwib3JpZ2luIjp0cnVlLCJyZWYiOm51bGwsImNvbnQiOm51bGwsIm5zIjpmYWxzZX0%3D; __uzmc=1148720547727',
'pragma': 'no-cache',
'referer': 'http://validate.perfdrive.com/seloger/captcha?ssa=87e94bf2-c5d5-90bb-1225-ca0c5d530ddb&ssc=http%3A%2F%2Fwww.seloger.com%2Fimmobilier%2Flocations%2Fimmo-paris-75%2Fbien-appartement%2F%3FLISTING-LISTpg%3D1&ssi=39289786-88be-c2d0-53b6-3bf7d3ff1287&ssk=contactus@shieldsquare.com&ssm=351474372493704886105266107870079&ssn=0b2d818c06a6f52a29dd58628c570343ec73321c5d66-2d07-7f7f-a2e5b7&sso=baff5ea7-732c8ed886c0a14d5aa5418ca952d3ae5b130faf71d151b2&ssp=63177274541579768292157997026130432&ssq=51986639176095508048487564572338514798802&ssr=ODkuMi42OS41MA==&sst=Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_13_6)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/79.0.3945.130%20Safari/537.36&ssw=',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'cross-site',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
'x-client-data': 'CJW2yQEIorbJAQjEtskBCKmdygEIy67KAQi9sMoBCJa1ygEI7LXKAQiOusoBGKukygE='
}

def rent_regulation():
    regulation=pd.read_excel('Regulation.xlsx', columns={'Area':np.int32,'N_rooms':np.int32,'Limit_rent':np.float64})
    return regulation

def SeLoger_pages(headers=headers):
    list_links = []
    for k in range (2):
        print('Retriving data for page: ', k+1)
        
        url = f'https://www.seloger.com/immobilier/locations/immo-paris-75/bien-appartement/?LISTING-LISTpg={k+1}'
        html = r.get(url,headers=headers).content
        soup = BeautifulSoup(html, 'lxml')
        
        links = [i for i in [i.get('href') for i in soup.select('div.Card__ContentZone-sc-7insep-3>a.CoveringLink-a3s3kt-0')] if i.startswith('https://www.seloger.com/')]
        if k%4==0:
            time.sleep(4)
        list_links.extend(links)
    print('All done!')
    return list_links
    
def SeLoger_appartments(list_links,headers=headers):
    rows=[]
    for i in list_links:
        html = r.get(i,headers=headers).content
        soup = BeautifulSoup(html, 'lxml')
        row=[]

        row.append(i)

        district = int([i.strip('ème').replace(',','.') for i in soup.select('h1.Title__ShowcaseTitleContainer-sc-4479bn-0')[0].text.split() if i.endswith('ème')==True][0])
        row.append(district)

        rent = int(''.join([i.text.split() for i in soup.select('div.Summary__Text-sc-1wkzvu-6>span')][0]).rstrip('C€'))
        m2 = float([i.strip('m²').replace(',','.') for i in soup.select('h1.Title__ShowcaseTitleContainer-sc-4479bn-0')[0].text.split() if i.endswith('m²')==True][0])
        rent_m2 = round(rent/m2,2)
        row.append(rent_m2)

        nb_rooms_test = int(re.findall('nb_pieces.+?:(\d)', str([i for i in soup.select("script:contains('nb_pieces')")]))[0])
        if nb_rooms_test<5:
            nb_rooms = nb_rooms_test
            row.append(nb_rooms)
        else:
            nb_rooms = 4
            row.append(nb_rooms)      
        
        rows.append(row)
    df=pd.DataFrame(rows, columns=['Link','District','Rent_m2','Nb_rooms'])
    return df

def report(df,regulation):
    watch_list=[]
    for i in df.index:
        limit = np.ndarray.item(regulation[(regulation['Area']==df.District[i])&(regulation['N_rooms']==df.Nb_rooms[i])]['Limit_rent'].values)
        if df['Rent_m2'][i]>limit:
            watch_list.append(df.Link[i])

    if len(watch_list)==0:
        print('Everything in order')
    else:
        print(f'I have found {len(watch_list)} suspicious ads out of {len(list_links)} ')
        answer1 = input('Would you like me to save those ads in a file ? Y/N ?')
        while answer1.capitalize() not in ['Y','N']:
            raise ValueError ('Please select between Y or N')
        if answer1=='Y':
            dff = pd.DataFrame(data={"watch_list": watch_list})
            dff.to_csv("Watch_list.csv", sep='\n',index=False)
            print('Done!')
        answer2 = input('Would you like to see those ads ? Y/N ?')
        while answer1.capitalize() not in ['Y','N']:
            raise ValueError ('Please select between Y or N')
        if answer2=='Y':
            for i in watch_list:
                webbrowser.open_new(i)
        
if __name__=='__main__':
    regulation=rent_regulation()
    list_links=SeLoger_pages()
    df=SeLoger_appartments(list_links)
    report(df,regulation)
