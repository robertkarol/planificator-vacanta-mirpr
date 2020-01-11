from NLPAylienAndWatson.TextRecognition import getFeatFromText, getLocationDateAndMoney
from NLPAylienAndWatson.TextObj import TextObj
class ServiceText:
    def __init__(self):
        pass



    def TextToTextAlgorithm(self, userText):
        pass

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

        result = getLocationDateAndMoney(text)

        location = result[0]
        date = result[1]
        money = result[2]

        print()
        print()
        print()

        print("Final Keywords:")
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
    def pushToFile(extension, list_objects, list_cities):
        for city in list_cities:
            with open(city + extension, 'r', encoding="utf8") as content_file:
                content = content_file.read()
                # print(content)
                obj = textToLabel(content)
                list_objects.append(obj)

        with open('labelsFromWebTexts', 'wb') as f:
            pickle.dump(list_objects, f)


    def extractFromWebFiles(onParagraphs=False):
        extension = '.txt'
        list_objects = []
        list_cities = ['Vienna', 'London', 'Lisbon', 'Berlin', 'Bucharest', 'Copenhagen', 'Edinburgh', 'Athens',
                       'Barcelona', 'Bern', 'St.Petersburg']
        if not onParagraphs:
            pushToFile(extension, list_objects, list_cities)
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
                        objT.setList(objT.getListOfObjectsWithProb() + obj.getListOfObjectsWithProb())
                        objT.setBudget(objT.getBudget() + obj.getBudget())
                        objT.setDate(objT.getDate() + obj.getDate())
                        objT.setLocation(objT.getLocation() + obj.getLocation())
                        list_objects.append(obj)

                else:
                    obj = textToLabel(content)
                    list_objects.append(obj)

            with open('labelsFromWebTexts', 'wb') as f:
                pickle.dump(list_objects, f)


    def getSavedLabelsFromFile():
        with open('labelsFromWebTexts', 'rb') as f:
            listTextObjs = pickle.load(f)
        list_cities = ['Vienna', 'London', 'Lisbon', 'Berlin', 'Bucharest', 'Copenhagen', 'Edinburgh', 'Athens',
                       'Barcelona', 'Bern', 'St.Petersburg']
        return [listTextObjs, list_cities]


    def LabelToLabelComparison(self, labelList):
        pass
