import json

with open('followers.json') as file:
  followers_json = json.load(file)

with open('following.json') as file:
  following_json = json.load(file)

followersLst = []
followingLst = []
# print(followers_json["relationships_followers"][0]['string_list_data'][0]['value'])
for followers in followers_json["relationships_followers"]:
  followersLst.append(followers['string_list_data'][0]['value'])

# print(followersLst)

for following in following_json["relationships_following"]:
  followingLst.append(following["string_list_data"][0]['value'])
# print(followingLst)

people_not_following_me_back = [i for i in followingLst if i not in followersLst]
for i, people in enumerate(people_not_following_me_back):
  print("{num}. {name}".format(num=i,name=people))