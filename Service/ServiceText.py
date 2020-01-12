from NLPAylienAndWatson.TextRecognition import getFeatFromText, getLocationDateAndMoney
from NLPAylienAndWatson.TextObj import TextObj
from NLPAylienAndWatson.main import textToLabel
from Scrapping.textData import *
import pickle

#from TextSimilarity.text_sim_api import get_top_similar_texts


class ServiceText:
    def __init__(self):
        pass

    # def TextToTextAlgorithm(self, userText):
    #     return get_top_similar_texts(userText)

    def extractLabelsAlgorithm(self, userText):
        # text = "I wish to go with my family in a warm place where my children can go to the pool and where my husband
        # can " \ "play poker. Also I want this place to be in Paris, near eiffel tower. Somewhere in California should
        # do the " \ "trick. We would like to spend 10 thousand dollars and we want to go this summer. "

        list_searchEntities = getFeatFromText(userText)
        # thisset = {'apple'}
        #
        # q = ""
        # texts = text.split(".")
        # print(texts)
        # for txt in texts:
        #     if txt:
        #         list_searchEntities = getFeatFromText(txt)
        #         print("Keywords:")
        #         print(list_searchEntities)
        #         for el in list_searchEntities:
        #             thisset.add(el)

        result = getLocationDateAndMoney(userText)

        location = result[0]
        date = result[1]
        money = result[2]

        print("\n\n\nFinal Keywords:")
        # print(thisset)

        print("Keywords:")
        print(list_searchEntities)
        print()

        q = ""

        locationStr = "-"
        dateStr = "-"
        moneyStr = "-"
        if location:
            print("Location: ")
            print(location[0])
            locationStr = location[0]
        if date:
            print("Date: ")
            print(date[0])
            dateStr = date[0]
        if money:
            print("Budget: ")
            print(money[0])
            moneyStr = money[0]

        objReturned = TextObj(list_searchEntities, locationStr, dateStr, moneyStr)
        print(objReturned)
        for label in objReturned.getListOfObjectsWithProb():
            print(label)
        return objReturned

    def pushToFile(self, extension, list_objects, list_cities):
        for city in list_cities:
            with open("C:\\Users\\ptido\\PycharmProjects\\MIRrepo\\planificator-vacanta-mirpr\\planificator-vacanta-mirpr\\Scrapping\\textData\\" + city + extension, 'r', encoding="utf8") as content_file:
                content = content_file.read()
                # print(content)
                obj = textToLabel(content)
                list_objects.append(obj)

        with open('labelsFromWebTexts', 'wb') as f:
            pickle.dump(list_objects, f)

    def extractFromWebFiles(self, onParagraphs=False):
        extension = '.txt'
        list_objects = []
        list_cities = ['Vienna', 'London', 'Lisbon', 'Berlin', 'Bucharest', 'Copenhagen', 'Edinburgh', 'Athens',
                       'Barcelona', 'Bern', 'St.Petersburg']
        if not onParagraphs:
            self.pushToFile(extension, list_objects, list_cities)
        else:
            for city in list_cities:
                with open(city + extension, 'r', encoding="utf8") as content_file:
                    content = content_file.read()
                t = content.split(".")
                if len(t) > 8:
                    print(len(t))
                    texts = []
                    txt = ""
                    for i in range(len(t)):
                        txt = txt + t[i] + "."
                        if (i % 4 == 0 and i != 0) or i == len(t) - 1:
                            if i == len(t) - 1:
                                txt = txt[:-1]
                            texts.append(txt)
                            txt = ""

                    print(texts)
                    list_labelsForTextContent = []
                    for text in texts:
                        list_labelsForTextContent.append(textToLabel(text))

                    objT = TextObj([], '', '', '')
                    for obj in list_labelsForTextContent:
                        objT.setEntities(objT.getListOfObjectsWithProb() + obj.getListOfObjectsWithProb())
                        objT.setBudget(objT.getBudget() + obj.getBudget())
                        objT.setDate(objT.getDate() + obj.getDate())
                        objT.setLocation(objT.getLocation() + obj.getLocation())
                        list_objects.append(obj)

                else:
                    obj = textToLabel(content)
                    list_objects.append(obj)

            with open('labelsFromWebTexts', 'wb') as f:
                pickle.dump(list_objects, f)

    def getSavedLabelsFromFile(self):
        with open('labelsFromWebTexts', 'rb') as f:
            listTextObjs = pickle.load(f)
        list_cities = ['Vienna', 'London', 'Lisbon', 'Berlin', 'Bucharest', 'Copenhagen', 'Edinburgh', 'Athens',
                       'Barcelona', 'Bern', 'St.Petersburg']
        return [listTextObjs, list_cities]

    def LabelToLabelComparison(self, labelList):
        pass


# s = ServiceText()
# s.extractFromWebFiles()
# [listTextObjs, list_cities] = s.getSavedLabelsFromFile()
# print("-------------------------------")
# print(listTextObjs)
# print(listTextObjs[0])
# print(list_cities)


# list_cities = ['Vienna', 'London', 'Lisbon', 'Berlin', 'Bucharest', 'Copenhagen', 'Edinburgh', 'Athens',
#                        'Barcelona', 'Bern', 'St.Petersburg']
#
# extension = ".txt"
#
# for i in range(0, len(list_cities)):
#     with open('C:\\Users\\ptido\\PycharmProjects\\MIRrepo\\planificator-vacanta-mirpr\\planificator-vacanta-mirpr\\Scrapping\\labels\\' + list_cities[i]+extension, 'wb') as f:
#         pickle.dump(listTextObjs[i], f)





