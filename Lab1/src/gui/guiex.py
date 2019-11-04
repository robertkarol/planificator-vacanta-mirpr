import PySimpleGUI as sg
import os





def searchByTextAlgorithm(text):
    # do stuff
    print("RUNNING ALGORITHM FOR :")
    print(text)
    #get result
    locations=["Malibu","California","Sri Lanka"]
    searchByTextResultWindow(locations)


def searchByImageAlgorithm(imageLocation):

    # do stuff
    print("RUNNING ALGORITHM FOR :")
    print(imageLocation)
    # get result
    locations = ["Malibu", "California", "Sri Lanka"]
    searchByTextResultWindow(locations)

def searchRouteByLocationAlgorithm(location,filters):
    # does magic
    print("WE ARE SEARCHING VISITING ROUTES IN ",location)
    print(filters)

    param=["Eiffel Tour","Louvre Museum","Sena cruise"]
    searchByLocationRouteResult(param)





def searchByLocationRouteResult(param):

    layout = [
        [sg.Text('We found an amazing route for you..')],
        [sg.Listbox(values=param, size=(30, 3))],
        [sg.Button("Show me on map"), sg.Button('Cancel')]
    ]

    windowTextResults = sg.Window('HOLIday').Layout(layout)
    while True:
        event, values = windowTextResults.Read()
        if event in (None, 'Cancel'):
            windowTextResults.close()
            main()
            print("Goodbye")
            break
        elif event in ("Show me on map"):
            windowTextResults.close()


# Very basic window.  Return values as a list
def searchByTextResultWindow(locations):
    layout = [
        [sg.Text('We found some great places for you..')],
        [sg.Listbox(values=locations, size=(30, 3))],
        [sg.Button("Find visiting route"),sg.Button('Cancel')]
    ]

    windowTextResults = sg.Window('HOLIday').Layout(layout)
    while True:
        event, values = windowTextResults.Read()
        if event in (None, 'Cancel'):
            windowTextResults.close()
            main()
            print("Goodbye")
            break
        elif event in ("Find visiting route"):
            windowTextResults.close()
            searchRouteByLocationWindow(values[0])








def searchRouteByLocationWindow(location):
    layoutOperation = [
        [sg.Text('What place do you want to explore ?')],
        [sg.InputText(location)],[],
        [sg.Text('By what do you want to travel ?')],
        [sg.Checkbox('Personal car'), sg.Checkbox('On foot', default=True),sg.Checkbox("Public transportation")],
        [sg.Text('What are your interests ?')],
        [sg.Checkbox('Arts'), sg.Checkbox('Arhitectural'), sg.Checkbox("Entertainment")],
        [ sg.Button('Search for me'),sg.Button('Cancel')]
    ]
    windowOperation = sg.Window('Text it out').Layout(layoutOperation)

    while True:
        eventOperation, valuesOperation = windowOperation.Read()
        if eventOperation in (None, 'Cancel'):
            windowOperation.close()
            main()
            break
        else :
            windowOperation.close()

            print(valuesOperation)
            searchRouteByLocationAlgorithm(valuesOperation[0],valuesOperation)






def openWindowTextSearch():
    print('Text search')
    layoutOperation = [
        [sg.Text('A few words to guide us..')],
        [sg.InputText('Couple of words')],
        [sg.Button('Search for me'), sg.Button('Cancel')]
    ]
    windowOperation = sg.Window('Text it out').Layout(layoutOperation)

    while True:
        eventOperation, valuesOperation = windowOperation.Read()
        if eventOperation in (None, 'Cancel'):
            windowOperation.close()
            main()
            break
        else:
            windowOperation.close()
            searchByTextAlgorithm(valuesOperation[0])


def openWindowImageSearch():
    print('Image search')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))[0:-7]+"\\data\\blohsaved.png"
    print(ROOT_DIR)
    image_elem = sg.Image(ROOT_DIR)
    layoutOperation = [
        [sg.Text('An image says what a thousand words can\'t..')],
        [sg.Text('The image :'),sg.InputText('path'), sg.FileBrowse()],
        [image_elem],
        [sg.Button('Search for me'), sg.Button('Cancel')]
    ]
    windowOperation = sg.Window('Text it out').Layout(layoutOperation)

    while True:
        eventOperation, valuesOperation = windowOperation.Read(timeout=50)
        if eventOperation in (None, 'Cancel'):
            windowOperation.close()
            main()
            break
        elif eventOperation in ('Search for me'):
            windowOperation.close()
            searchByImageAlgorithm(valuesOperation[0])

        if valuesOperation[0]!="path":
            image_elem.update(valuesOperation[0])



def openWindowRoutesSearch():
    print('Route search')
    layoutOperation = [
        [sg.Text('What place do you want to explore ?')],
        [sg.InputText('location')],
        [sg.Button('HERE !'), sg.Button('Cancel')]
    ]
    windowOperation = sg.Window('Where ?').Layout(layoutOperation)

    while True:
        eventOperation, valuesOperation = windowOperation.Read()
        if eventOperation in (None, 'Cancel'):
            windowOperation.close()
            main()
            break
        else:
            windowOperation.close()
            searchRouteByLocationWindow(valuesOperation[0])



sg.ChangeLookAndFeel('Dark')
sg.SetOptions(element_padding=(5, 5), button_element_size=(15, 2), auto_size_buttons=False,button_color=('white', 'firebrick4'))
layout = [
              [sg.Text('Let us plan an awesome holiday for you..')],
              [sg.Button('Search with text'), sg.Button('Search with image'),sg.Button('Create a route')],
              [sg.Button('Cancel')]
             ]
window= sg.Window('HOLIday').Layout(layout)

def main():

    try:
        window.enable()
    except(Exception):
        print("NOW")


    while True:
        event, values = window.Read()
        if event in (None,'Cancel'):
            print("Goodbye")
            break

        if event in ('Search with text'):
            window.disable()
            openWindowTextSearch()


        if event in ('Search with image'):
            window.disable()
            openWindowImageSearch()

        if event in ('Create a route'):
            window.disable()
            openWindowRoutesSearch()



main()


