def index():
    return {
            'page':'new and improved home Page',
            'page2':'new and improved home Page2'
            }

def a():
    return 'you are on the A page'

def name(name):
    return 'Hey {}, Nice Meeting you here!!'.format(name)

def fun(amountPerMonth, years):
    sum = amountPerMonth
    i = 0
    eachyear = []
    
    while (i < years):
        sum = sum + amountPerMonth * 12
        sum = sum + sum * 0.1
        eachyear.insert(i, int(sum))
        
        i = i + 1
    
    return {
        'Amount per month' : amountPerMonth,
        'years' : years,
        'Princibol' : amountPerMonth * 12 * years,
        'sum' : sum,
        'sum each year' : eachyear
    }



