import pandas as pd
import os

import sys
f = open("test.out", 'w', encoding="utf-8")
sys.stdout = f

df_ = pd.read_excel('bios.xlsx')
images_ = [i.split('.')[0] for i in os.listdir('images/team/')]
images_link = os.listdir('images/team/')
for person_ in df_.iloc:
  name = person_['Name']
  first_name = person_['First Name']
  last_name = person_['Last Name']
  if last_name in images_:
    picture_link = images_link[images_.index(last_name)]
  else:
    picture_link = "you_.png"
  title = "" if pd.isna(person_['Title']) else person_['Title']
  profession = "" if person_["What do you do (?)"] else person_["What do you do (?)"]
  institution = "" if person_["Institution, city, country"] else person_["Institution, city, country"]
  

  person_card = f"""
    <div class="col-lg-3">
      <div class="card border-0 card-hover" data-bs-toggle="modal" data-bs-target="#modal-{last_name}">
        <div class="position-relative rounded-circle overflow-hidden mx-auto custom-circle-image">
          <img class="w-100 h-100" src="../images/team/{picture_link}" alt="{first_name}">
        </div>
        <div class="card-body text-center">
          <div class="card-title">{title} {name}</div>
          <p class="card-text"> {profession} <br> {institution} </p>
        </div>
      </div>
    </div>"""
  #print(person_card)

for person_ in df_.iloc:
  name = person_['Name']
  first_name = person_['First Name']
  last_name = person_['Last Name']
  if last_name in images_:
    picture_link = images_link[images_.index(last_name)]
  else:
    picture_link = "you_.png"
  title = "" if pd.isna(person_['Title']) else person_['Title']
  profession = "" if person_["What do you do (?)"] else person_["What do you do (?)"]
  institution = "" if person_["Institution, city, country"] else person_["Institution, city, country"]
  facebook = person_['facebook?']
  twitter = person_['twitter ID']
  if not pd.isna(twitter):
    twitter = twitter[1:]
  instagram = person_['instagram ID']
  if not pd.isna(instagram):
    instagram = instagram[1:]
  linkedin = person_['LinkedIn']
  website = person_['website?']

  facebook_a = f"""
  <a class="me-2" href = "{facebook}"><i class="bi-facebook footer-icons"></i></a>
  """
  facebook_link = "" if pd.isna(facebook) else facebook_a

  twitter_a = f"""
  <a class="me-2" href = "https://twitter.com/{twitter}"><i class="bi-twitter footer-icons"></i></a>
  """
  twitter_link = "" if pd.isna(twitter) else twitter_a

  instagram_a = f"""
  <a class="me-2" href = "https://www.instagram.com/{instagram}"><i class="bi-instagram footer-icons"></i></a>
  """
  instagram_link = "" if pd.isna(instagram) else instagram_a

  linkedin_a = f"""
  <a class="me-2" href = "{linkedin}"><i class="bi-linkedin footer-icons"></i></a>
  """
  linkedin_link = "" if pd.isna(linkedin) else linkedin_a

  website_a = f"""
  <a class="me-2" href = "{website}"><i class="bi-globe footer-icons"></i></a>
  """
  website_link = "" if pd.isna(website) else website_a

  bio = person_['Bio (max 300 characters, excluding spaces)']


  person_modal = f"""
  <div class="modal fade" id="modal-{last_name}" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-xl modal-dialog-scrollable">
      <div class="modal-content">
        <div class="modal-body">
          <div class = "row justify-content-evenly align-items-center">
            <div class = "col-sm-5">
              <div class="card border-0">
                <div class="position-relative rounded-circle overflow-hidden mx-auto custom-circle-image">
                  <img class="w-100 h-100" src="../images/team/{picture_link}" alt="{first_name}">
                </div>
                <div class="card-body text-center">
                  <div class="card-title">{title} {name}</div>
                  <p class="card-text"> {profession} <br> {institution} </p>
                  <div style="font-size: 1rem;">
                    {facebook_link}
                    {twitter_link}
                    {instagram_link}
                    {linkedin_link}
                    {website_link}
                  </div>
                </div>
              </div>
            </div>
            <div class = "col-sm-7">
              <h3> {name} </h3>
              {bio}
            </div>
        </div>
      </div>
    </div>
  </div>
  </div>
  """
  print(person_modal)

f.close()