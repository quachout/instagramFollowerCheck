import json

#open followers.json
with open('followers.json') as file:
  followers_json = json.load(file)

#open following.json
with open('following.json') as file:
  following_json = json.load(file)

followersLst = []
followingLst = []

#get each follower and add it to followersLst
for followers in followers_json["relationships_followers"]:
  followersLst.append(followers['string_list_data'][0]['value'])

#get each following and add it to followingLst
for following in following_json["relationships_following"]:
  followingLst.append(following["string_list_data"][0]['value'])

#list of people not following me back
people_not_following_me_back = [i for i in followingLst if i not in followersLst]

#print name of people not following me back
for i, people in enumerate(people_not_following_me_back):
  print("{num}. {name}".format(num=i,name=people))