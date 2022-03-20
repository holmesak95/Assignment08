#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# AKHolmes, 2022-Mar-19, created CD object, added
# AKHolmes, 2022-Mar-20, added validation/error handling code I created from previous assignment
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []
YES_NO_LIST = ['y','n']
MENU_LIST = ['l', 'a', 'i', 'd', 's', 'x']

class CD():
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # TODONE Add Code to the CD class
    # -- Constructor -- #
    def __init__(self, intID, strTitle, strArtist):
        self.__cd_id = intID
        self.__cd_title = strTitle
        self.__cd_artist = strArtist

    # -- Properties (Getters) -- #
    @property
    def cd_id(self):
        return self.__cd_id
    
    @property
    def cd_title(self):
        return self.__cd_title.title()
    
    @property
    def cd_artist(self):
        return self.__cd_artist.title() 
    
    # -- Properties (Setters) -- #
    @cd_id.setter
    def cd_id(self, intID):
        """
        Parameters
        ----------
        value : TYPE = INTEGER
            DESCRIPTION = the value that user wants to assign for cd_id
        Raises
        ------
        Exception
            DESCRIPTION = if value is not an integer

        Returns
        -------
        value : TYPE = STRING
            DESCRIPTION = returns ID of CD
        """
        while True:
            try:
                intID = int(input('Enter ID: ').strip())
                return intID
            except:
                print('Please only enter whole numbers.')
                
    @cd_title.setter
    def cd_title(self, value):
        """
        Parameters
        ----------
        value : TYPE = STRING
            DESCRIPTION = the value that user wants to assign for cd_title
        Raises
        ------
        Exception
            DESCRIPTION = if value is null

        Returns
        -------
        value : TYPE = STRING
            DESCRIPTION = returns title of CD
        """
        while True:
            try:
                value = str(input('Enter title of CD: ').strip())
                if not value:
                    raise Exception('Empty string. Please enter value.')
                return value
            except:
                print('Please enter a string.')
    
    @cd_artist.setter
    def cd_artist(self, value):
        """
        Parameters
        ----------
        value : TYPE = STRING
            DESCRIPTION = the value that user wants to assign for cd_artist
        Raises
        ------
        Exception
            DESCRIPTION = if value is null

        Returns
        -------
        value : TYPE = STRING
            DESCRIPTION = returns artist of CD
        """
        while True:
            try:
                value = str(input('Enter artist of CD: ').strip())
                if not value:
                    raise Exception('Empty string. Please enter value.')
                return value
            except:
                print('Please enter a string.')
                
    # -- Methods -- #
    def write_to_file(self):
        """
        Returns
        -------
        TYPE = STRING
            DESCRIPTION = formats the values for writing to a .csv file
        """
        return (str(self.cd_id) + ',' + self.cd_title + ',' + self.cd_artist + '\n')

class ErrorProcessor:
    def valid_int():
        """
        Returns
        -------
        intID : TYPE = INTEGER
            DESCRIPTION = returns a valid integer
        """
        while True:
            try:
                intID = int(input('Enter ID: ').strip())
                return intID
            except:
                print('Please only enter whole numbers.')
    
    def valid_str(strQuestion, answers = []):
        """
        Parameters
        ----------
        strQuestion : TYPE = string
            DESCRIPTION = displays the question that the user will respond to
        answers : TYPE, optional = list
            DESCRIPTION. The default is []. displays the possible answers

        Raises
        ------
        Exception
            DESCRIPTION = if user enters without typing anything

        Returns
        -------
        strAnswer : TYPE = string
            DESCRIPTION = the user's response to strQuestion
        """
        while True:
            try:
                if len(answers) > 0:
                    strAnswer = str(input(strQuestion).strip().lower())
                    if (strAnswer not in answers):
                        raise Exception('Please enter a valid choice: ' + print(answers))
                else:
                    strAnswer = str(input(strQuestion).strip())
                if not strAnswer:
                    raise Exception('Empty string. Please enter value.')
                return strAnswer
            except:
                print('Please enter a string.')

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TODONE Add code to process data from a file
    def load_inventory(file_name):
        """
        Parameters
        ----------
        strQuestion : TYPE = string
            DESCRIPTION = displays the question that the user will respond to
        answers : TYPE, optional = list
            DESCRIPTION. The default is []. displays the possible answers

        Raises
        ------
        Exception
            DESCRIPTION = if user enters without typing anything

        Returns
        -------
        strAnswer : TYPE = string
            DESCRIPTION = the user's response to strQuestion
        """
        
        try:
            lstOfCDObjects.clear()
            objFile = open(file_name, 'r')
            try:
                for line in objFile:
                    data = line.strip().split(',')
                    objCD = CD(int(data[0]), data[1], data[2])
                    lstOfCDObjects.append(objCD)
                objFile.close()
                if len(lstOfCDObjects) > 0:
                    return False
                else:
                    return True
            except:
                print('File is probably empty. Can\'t load data.')
                return False
        except FileNotFoundError:
            strAnswer = ErrorProcessor.valid_str('File was not found. Do you want to create a new file? ', YES_NO_LIST)
            if (strAnswer == 'y'):
                objFile = open(strFileName, 'a')
                return True
            else:
                print('There is no inventory to load.')
                return True
                
    # TODONE Add code to process data to a file
    def save_inventory(file_name, lst_Inventory):
        try:
            objFile = open(file_name, 'w')
            for obj in lstOfCDObjects:
                line = obj.write_to_file()
                objFile.write(line)
            objFile.close()  
            if len(lstOfCDObjects) > 0:
                return False
            else:
                return True
        except FileNotFoundError:
            strAnswer = ErrorProcessor.valid_str('File was not found. Do you want to create a new file? ', YES_NO_LIST)
            if (strAnswer == 'y'):
                objFile = open(strFileName, 'a')
                return True
            else:
                print('There is no file to save inventory to.')
                return True
    pass

# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODONE add docstring
    """Acts as interface of CD inventory for user

    properties:
    methods:
        print_menu() --> None
        menu_choice() --> (a character of the user's menu choice')

    """
    # TODONE add code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user
        Args:
            None.
        Returns:
            None.
        """

        print('Menu\n')
        print('[L] Load Inventory from file')
        print('[A] Add CD')
        print('[I] Display Current Inventory')
        print('[D] Delete CD from Inventory')
        print('[S] Save Inventory to file')
        print('[X] Exit\n')
        
    # TODONE add code to captures user's choice
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection
        Args:
            None.
        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x
        """
        choice = ' '
        while choice not in MENU_LIST:
            choice = ErrorProcessor.valid_str('Which operation would you like to perform? [l, a, i, d, s or x]: ', MENU_LIST)
        print()  # Add extra space for layout
        return choice
    
    # TODONE add code to display the current data on screen
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table
        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for obj in lstOfCDObjects:
            print('{}\t{} (by: {})'.format(obj.cd_id, obj.cd_title, obj.cd_artist))
        print('======================================')
        
    # TODONE add code to get CD data from user
    def add_inventory():
        """
        Returns
        -------
        resultID : TYPE = int
            DESCRIPTION = the ID number for the CD (inputted from user)
        strTitle : TYPE = string
            DESCRIPTION = the title of the CD (inputted from user)
        strArtist : TYPE = string
            DESCRIPTION = the artist for the CD (inputted from user)

        """
        intID = ErrorProcessor.valid_int()
        strTitle = ErrorProcessor.valid_str('What is the CD\'s title? ')
        strArtist = ErrorProcessor.valid_str('What is the Artist\'s name? ')
        objCD = CD(intID, strTitle, strArtist)
        lstOfCDObjects.append(objCD)
        IO.show_inventory(lstOfCDObjects)
        
    def delete_CD(intIDDel):
        """
        Parameters
        ----------
        intIDDel : TYPE = int
        DESCRIPTION = the ID number of the CD user wants to delete

        Returns
        -------
        None.

        """
        intRowNr = -1
        blnCDRemoved = False
        for obj in lstOfCDObjects:
            intRowNr += 1
            if obj.cd_id == intIDDel:
                del lstOfCDObjects[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')

# -- Main Body of Script -- #
# TODONE Add Code to the main body
# Load data from file into a list of CD objects on script start
FileEmptyInd = FileIO.load_inventory(strFileName)
while True:
    # Display menu to user
    IO.print_menu()
    # show user current inventory
    strChoice = IO.menu_choice()
    
    # let user exit program
    if strChoice == 'x':
        break
    
    # let user add data to the inventory
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        IO.add_inventory()
        continue  # start loop back at top.
        
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
        
    elif strChoice == 'd':
        IO.show_inventory(lstOfCDObjects)
        # 3.5.1.2 ask user which ID to remove
        intIDDel = ErrorProcessor.valid_int()
        # 3.5.2 search thru table and delete CD
        IO.delete_CD(intIDDel)
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    # let user save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strAnswer = ErrorProcessor.valid_str('Save this inventory to file? [y/n] ', YES_NO_LIST)
        # 3.6.2 Process choice
        if strAnswer == 'y':
            # 3.6.2.1 save data
            FileEmptyInd = FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
        
    # let user load inventory from file
    if strChoice == 'l':
        if (FileEmptyInd is True):
            print('It\'s not possible to load data from the file right now.')
            continue
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strAnswer = ErrorProcessor.valid_str('type \'y\' to continue and reload from file. otherwise reload will be canceled', YES_NO_LIST)
        if (strAnswer == 'y'):
            print('reloading...')
            FileIO.load_inventory(strFileName)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    

