# coding: utf-8
import shelve

DATA_FILE = 'guestbook.dat'

def save_data(name, comment, create_at):
    """Save Posted Data
    """

    # open database file with shelve module
    database = shelve.open(DATA_FILE)

    # create new list unless greeting_list exists in database
    if 'greeting_list' not in database:
        greeting_list = []
    else:
        # Fetch data from database
        greeting_list = database['greeting_list']

    # Add Posted data at the top of the list
    greeting_list.insert(0, {
        'name':      name,
        'comment':   comment,
        'create_at': create_at
    })

    # Reload database
    database['greeting_list'] = greeting_list

    # Close database file
    database.close()


def load_data():
    """Return Posted data
    """

    # Open database file with shelve module
    database = shelve.open(DATA_FILE)

    # Return greeting_list.
    # Return empty list if there is no data
    greeting_list = database.get('greeting_list', [])
    database.close()
    return greeting_list
