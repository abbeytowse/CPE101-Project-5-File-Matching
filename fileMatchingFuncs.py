# Project 5 – File Matching
# Name: Abbey Towse
# Section: 11
# Instructor: Clark Turner

class Entry:

    def __init__(self, account_num, name, balance, phone, city):

        self.account_num = account_num
        self.name = name
        self.balance = balance
        self.phone = phone
        self.city = city

    def __eq__(self, other):     # not confident that this is correct, so TBD

        if isinstance(other, Entry):

            if self.account_num == other.account_num and \
                    self.name == other.name and \
                    self.balance == other.balance and \
                    self.phone == other.phone and \
                    self.city == other.city:

                return True

        return False


def sort_entry_list(entry_list):    # insertion sort

    """
    Input type: list
    Output type: list
    Function: uses insertion sort algorithm to sort entry lists
    in ascending order
    """

    # got base of this code from in class example

    # for each list in the list of entries
    for i in range(1, len(entry_list)):

        current_list = entry_list[i]    # the list of interest
        # the element of the list used for sorting
        account_num = entry_list[i].account_num

        while i > 0 and entry_list[i - 1].account_num > account_num:

            # insert list of interest to new location
            entry_list[i] = entry_list[i - 1]
            i = i - 1    # update the value of i
            entry_list[i] = current_list

    return entry_list


def sort_transaction_list(transaction_list):    # insertion sort

    """
    Input type: list
    Output type: list
    Function: uses insertion sort algorithm to sort transaction lists
    in ascending order
    """

    # got base of this code from in class example

    # for each list in the list of entries
    for i in range(1, len(transaction_list)):

        # if the transaction entry isn't blank
        if transaction_list[i] != []:

            current_list = transaction_list[i]    # the list of interest
            # the element of the list used for sorting
            account_num = transaction_list[i][0]

            while i > 0 and transaction_list[i - 1][0] > account_num:

                # insert list of interest to new location
                transaction_list[i] = transaction_list[i - 1]
                i = i - 1    # update the value of i
                transaction_list[i] = current_list

    return transaction_list


def binary_search(entry_list, transaction_num):

    """
    Input type: list and string, respectively
    Output type: integer
    Function: finds the index of transaction number match in entry list
    """

    # declare variables
    low = 0
    high = len(entry_list) - 1
    mid = 0

    iteration = 0

    # if low is greater than high then there is no match
    while low <= high:

        iteration = iteration + 1
        mid = (high + low) // 2    # get the middle number of the range

        # move search up the list
        if int(entry_list[mid].account_num) < int(transaction_num):

            low = mid + 1    # update search range

        # move search down the list
        elif int(entry_list[mid].account_num) > int(transaction_num):

            high = mid - 1    # update search range

        else:    # if match is found

            return mid    # index of the match

    return -1    # no match is found


def read_file(file_name):

    """
    Input type: file
    Output type: list
    Function: opens a files and parses it as a list
    """

    entry_list = []    # create empty list to store entries in
    file = open(file_name, "r")    # open file and read in

    # create an entry from each line in the file
    for line in file:

        values_list = line.split()    # make each line a list splitting at " "
        # merge first and last name into one list element
        # code from GeeksForGeeks
        values_list[1: 3] = [' '.join(values_list[1: 3])]
        # this only works because occurrence order in file is constant
        entry = Entry(str(values_list[0]), str(values_list[1]), float(values_list[2]),
                      str(values_list[3]), str(values_list[4]))
        entry_list.append(entry)    # update entry list

    file.close()

    return entry_list


def write_file(file_name, entry_list):

    """
    Input: list
    Output: file
    Function: takes sorted entries and writes a new file
    """

    file = open(file_name, "w")    # open file

    for element in entry_list:    # for each element in the list

        # separate the first and last name string
        name = str(element.name)
        first_name, last_name = name.split(' ', 1)

        # write in and format
        file.write('{:<4}'.format(str(element.account_num)) + " ")
        file.write('{:<6}'.format(first_name) + " ")
        file.write('{:<7}'.format(last_name) + " ")
        file.write('{:<7}'.format(str('{:.2f}'.format(element.balance))) + " ")
        file.write('{:<15}'.format(str(element.phone)) + " ")
        file.write(str(element.city))
        file.write("\n")    # go to newline after each entry

    file.close()


def account_balance_update(entry_list, file_name):

    """
    Input type: list and file, respectively
    Output type: list
    Function: finds matching account numbers and adds transaction to
    balances in entry list
    """

    transaction_list = []    # create empty list to store sorted list in
    transaction_file = open(file_name, "r")

    # get transaction records as a list
    for line in transaction_file:

        values_list = line.split()    # turn each line in a list
        # if list is not blank, accounts for blank lines at end of file
        if values_list != []:

            transaction_list.append(values_list)

    transaction_list = sort_transaction_list(transaction_list)    # sort

    # use binary search on each transaction
    for transaction in transaction_list:

        index = binary_search(entry_list, float(transaction[0]))
        if index > -1:    # if match is found update balance

            entry_list[index].balance += float(transaction[1])

        else:    # if not match is found

            print("Unmatched transaction record for account number",
                  transaction[0])

    transaction_file.close()
    return entry_list


def main():

    # read in unsorted, unupdated account records
    file_name = "oldMaster.dat"
    entry_list = read_file(file_name)

    # sort account records and create new file
    sorted_entry_list = sort_entry_list(entry_list)
    sorted_file_name = "sorted_oldMaster.dat"
    write_file(sorted_file_name, sorted_entry_list)

    # update account balances and create new file
    updated_account_balances = account_balance_update(sorted_entry_list,
                                                      "transaction.dat")
    master_file = "newMaster.dat"
    write_file(master_file, updated_account_balances)


main()
