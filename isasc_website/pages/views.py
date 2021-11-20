from django.shortcuts import render
import pandas as pd
import os
import re
from django.contrib.staticfiles.storage import staticfiles_storage

def formaturl(url):
    if not re.match('(?:http|ftp|https)://', url):
        return f'http://{url}'
    return url

def index1(request):
    return render(request, 'index1.html', {})

def our_story(request):
    return render(request, 'our_story.html', {})

def about_us(request):
    return render(request, 'about_us.html', {})

def team(request):
    df_ = pd.read_excel('static/bios.xlsx')
    images_ = [i.split('.')[0] for i in os.listdir('static/images/team/')]
    images_link = os.listdir('static/images/team/')
    team_list = []
    for person_ in df_.iloc:
        member = {}
        name = person_['Name']
        first_name = person_['First Name']
        last_name = person_['Last Name']
        if last_name in images_:
            picture_link = images_link[images_.index(last_name)]
        else:
            picture_link = "you_.png"
        picture_link = f'/static/images/team/{picture_link}'
        title = "" if pd.isna(person_['Title']) else person_['Title']
        profession = "" if pd.isna(person_["What do you do (?)"]) else person_["What do you do (?)"]
        institution = "" if pd.isna(person_["Institution, city, country"]) else person_["Institution, city, country"]

        # Social Media Handles
        twitter = person_['twitter ID']
        if not pd.isna(twitter):
            twitter = twitter[1:]   # Twitter Handle is input as '@twitter_id'. We need 'twitter_id'
        else:
            twitter = False

        instagram = person_['instagram ID']
        if not pd.isna(instagram):
            instagram = instagram[1:]
        else:
            instagram = False

        linkedin = person_['LinkedIn']
        if not pd.isna(linkedin):
            linkedin = formaturl(linkedin)
        else:
            linkedin = False

        website = person_['website?']
        if not pd.isna(website):
            website = formaturl(website) #Add http:// if not already present
        else:
            website = False
        
        bio = person_['Bio (max 300 characters, excluding spaces)']

        member['name'] = name
        member['first_name'] = first_name
        member['last_name'] = last_name
        member['file_name'] = picture_link
        member['title'] = title
        member['profession'] = profession
        member['institution'] = institution
        member['twitter'] = twitter
        member['instagram'] = instagram
        member['linkedin'] = linkedin
        member['website'] = website
        member['bio'] = bio
        team_list.append(member)
    context = {"team_list" : team_list}
    return render(request, 'team.html', context)