import csv
import paralleldots

paralleldots.set_api_key("*insert_your_api_key*")

def get_similarity(text1, text2):
    return paralleldots.similarity(text1, text2)

def get_top_similar_texts( user_query):
    sim_list = []
    with open(r"../Data/californication.csv", encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print (row[0])
            if row[0].startswith("ID"):
                continue
            else:
                similarity = get_similarity(text1=user_query, text2=row[2])
                sim_list.append([row[2], similarity["similarity_score"]])

        sim_list= sorted(sim_list, key= lambda x : x[1], reverse=True)
        for i in range(26):
            print(sim_list[i])




if __name__=="__main__":
    get_top_similar_texts("I want to plan a surprise trip for me and my family. My husband is a hiking lover and my children adore long walks in the forest. "
                          "I want to go in a new place like Califoria to see giant sequoia trees for the first time. There is no budget limit. ")