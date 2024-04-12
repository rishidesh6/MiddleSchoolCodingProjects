import requests
import json

url = "https://api-basketball.p.rapidapi.com/games"

print("Hello, my project will show you all the scores for any NBA games you choose!")
print("\n")
season = input("Which season would you like to see the games of? Please enter in yyyy-yyyy and in quotation marks: ")
print("\n")
date = input("What date would you like to see the scores of? Enter here in yyyy-mm-dd and in quotation marks: ")
#print("you entered " + str(date))

querystring = {"timezone":"PST","season": season,"league":"12","date": date}
#print(querystring)

headers = {
	"X-RapidAPI-Key": "6d2896a171msha9a638945c45dd3p18efe5jsnee3e37471265",
	"X-RapidAPI-Host": "api-basketball.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
responseJson = json.dumps(response.json())
decoded_array = responseJson.decode('utf-8', 'ignore')
arrayOfScores = json.loads(decoded_array)
arrayOfTeams = json.loads(decoded_array)

arrayOfResponse = []
for key, value in arrayOfScores.items():
    decoded_k = key.decode('utf-8', 'ignore')
    if decoded_k == "response":
          arrayOfResponse = value

    
print("These are the scores for all games on the day you chose: ")
for entry in arrayOfResponse:
    gStatus = ""
    for k, v in entry.items():
        decoded_k = k.decode('utf-8', 'ignore')
        #print (decoded_k)
        # TEAMS
        if decoded_k == "teams":
            
            for k, v in v.items():
                teamNames = "{} vs {}"
                
                decoded_k2 = k.decode('utf-8', 'ignore')
                if decoded_k2 == "home":
                    for k, v in v.items():
                        decoded_k2 = k.decode('utf-8', 'ignore')
                        if decoded_k2 == "name":
                            hteam = v
                            
                if decoded_k2 == "away":
                    for k, v in v.items():
                        decoded_k2 = k.decode('utf-8', 'ignore')
                        if decoded_k2 == "name":
                            ateam = v
                            print(teamNames.format(hteam.rstrip(), ateam.rstrip()))
                            hteam = ""
                            ateam = ""


        #SCORES
        if decoded_k == "scores":
            teamScores = "{} : {}"
            for k, v in v.items():
                decoded_k2 = k.decode('utf-8', 'ignore')
                if decoded_k2 == "home":
                    for k, v in v.items():
                        decoded_k2 = k.decode('utf-8', 'ignore')
                        if decoded_k2 == "total":
                            hteam = v
                
                if decoded_k2 == "away":
                    for k, v in v.items():
                        decoded_k2 = k.decode('utf-8', 'ignore')
                        if decoded_k2 == "total":
                            ateam = v
                            print(teamScores.format(hteam, ateam))
                            print(gameStatus.format(gStatus))
                            hteam = ""
                            ateam = ""
                
                            

        if decoded_k == "status":
            for k, v, in v.items():
                gameStatus = "Game Status: {}"
                decoded_k2 = k.decode('utf-8', 'ignore')
                if decoded_k2 == "long":
                    gStatus = v 
                    print("======================================")
