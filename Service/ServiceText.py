from NLPAylienAndWatson.TextRecognition import getFeatFromText, getLocationDateAndMoney

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

    def LabelToLabelComparison(self, labelList):
        pass
