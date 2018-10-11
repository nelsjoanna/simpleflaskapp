"""define a function called articles and create variable called articles.
Each article goes inside the braces
Each article will have an 'id'
"""
def Articles():
    articles = [
        {
            'id':1,
            'title':'Article One',
            'body':'lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                   'labore et dolore magna aliqua.',
            'author':'Joanna Nelson',
            'create_date':'10-10-18'
        },
        {   'id': 1,
            'title':'Article Two',
            'body':'lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                    'labore et dolore magna aliqua.',
            'author': 'Joanna Nelson',
            'create_date': '10-10-18'
        },
        {
            'id': 1,
            'title':'Article Two',
            'body':'lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                 'labore et dolore magna aliqua.',
            'author':'Joanna Nelson',
            'create_date': '10-10-18'
        }
    ]
    #to use this data you have to export it (or return). so
    return articles