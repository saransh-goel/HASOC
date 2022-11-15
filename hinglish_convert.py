# from asyncio.windows_events import NULL
import os
import json
import csv
PATH = './data/contextual_2022_train/Train/'  #initial path to training data directory
LAN = 'Hinglish'
list1 = os.listdir(PATH+LAN)
def retRowHinglish(data,context_label,binary_label):
    id = data["tweet_id"]
    row1 = {
        "tweet_id": id,
        "tweet": data["tweet"],
        "context_label": context_label[id],
        "binary_label": binary_label[id]
    }
    return row1


with open(LAN+".json", 'w') as csvfile:    #open the csv file to write into it
    result = {"data": []} 
    for category in list1:
        list2 = os.listdir(PATH+LAN+"/"+category)
        for a in list2:
            try:
                data = json.load(open(PATH+LAN+"/"+category+"/"+a+"/data.json", encoding="utf8"))
                context_labels = json.load(open(PATH+LAN+"/"+category+"/"+a+"/contextual_labels.json"))
                binary_labels = json.load(open(PATH+LAN+"/"+category+"/"+a+"/binary_labels.json"))
                main_tweet_text = retRowHinglish(data,context_labels, binary_labels)["tweet"]
                result["data"].append(retRowHinglish(data,context_labels, binary_labels))
                for comment in data["comments"]:
                    row_for_comment = retRowHinglish(comment,context_labels, binary_labels)
                    row_for_comment["tweet"] = main_tweet_text + row_for_comment["tweet"]
                    result["data"].append(row_for_comment)
                    try:
                        for reply in comment["replies"]:
                            row_for_reply = retRowHinglish(reply,context_labels, binary_labels)
                            row_for_reply["tweet"] = row_for_comment["tweet"] + row_for_reply["tweet"]
                            result["data"].append(row_for_reply)
                    except:
                        print("no reply")
            except:
                print("empty directory")
            

    print(len(result["data"]))              
    csvfile.write(json.dumps(result, indent=4))
    # # writing the fields 
    # csvwriter.writerow(fields) 
        
    # # writing the data rows 
    # csvwriter.writerows(rows)


    
#json.load(file object)


