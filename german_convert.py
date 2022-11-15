# from asyncio.windows_events import NULL
import os
import json
import csv
PATH = './data/contextual_2022_train/Train/'  #initial path to training data directory
LAN = 'German'         #type of language name
list1 = os.listdir(PATH+LAN)

def retRowGerman(data,label):
    id = data["tweet_id"]
    row1 = {
        "tweet_id": id,
        "tweet": data["tweet"],
        "label": label[id],
    }
    # row1 = [id, data["tweet"], label[id]]
    return row1

with open(LAN+".json", 'w') as csvfile:    #open the csv file to write into it
    # creating a csv writer object 
    # writer = csv.writer(csvfile)
    # writer.writerow(["tweet_id", "tweet", "label"])
    result = {"data": []} 
    for category in list1:
        list2 = os.listdir(PATH+LAN+"/"+category)
        for a in list2:
            try:
                data = json.load(open(PATH+LAN+"/"+category+"/"+a+"/data.json", encoding="utf8"))
                labels = json.load(open(PATH+LAN+"/"+category+"/"+a+"/labels.json"))
                main_tweet_text = retRowGerman(data,labels)["tweet"]
                result["data"].append(retRowGerman(data,labels))
                for comment in data["comments"]:
                    row_for_comment = retRowGerman(comment,labels)
                    row_for_comment["tweet"] = main_tweet_text + row_for_comment["tweet"]
                    result["data"].append(row_for_comment)
                    try:
                        for reply in comment["replies"]:
                            row_for_reply = retRowGerman(reply,labels)
                            row_for_reply["tweet"] = row_for_comment["tweet"] + row_for_reply["tweet"]
                            result["data"].append(row_for_reply)
                    except:
                        print("no reply")
            except:
                print("empty directory")
            

    print(len(result["data"]))              
    csvfile.write(json.dumps(result, indent=3))
    # # writing the fields 
    # csvwriter.writerow(fields) 
        
    # # writing the data rows 
    # csvwriter.writerows(rows)


    
#json.load(file object)


