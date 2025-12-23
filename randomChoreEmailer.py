#! python3
# a program that takes a list of people’s email addresses and a list of chores that need to be done
# and randomly assigns chores to people. Email each person their assigned chores.
import random, smtplib, pprint, chore

def choreEmailer(email, password, date):
    chores = ['Wash the dishes', 'Wash the bathroom', 'Vacuum the house', 'Walk the dog']
    emailList = ['Eric@gmail.com', 'tabitha@yahoo.com', 'Medussa@venicom.com', 'Micheal@gmail.com']
    choredict = chore.choreData
    choredict.setdefault(date, {})
    for i in range(len(chores)):
        randomChore = random.choice(chores)
        chores.remove(randomChore)

        smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtpObj.ehlo()
        smtpObj.login(email, password)
        print('Sending chore to %s' % emailList[i])
        smtpObj.sendmail(email, emailList[i], 'Subject: Chore Assignment\nYour chore this week is %s.. Sincerely, Bolu' % randomChore)

        choredict[date].setdefault(emailList[i], randomChore)

    print('saving weeks chores...')
    choreFile = open('chore.py', 'w')
    choreFile.write('choreData = ' + pprint.pformat(choredict))
    choreFile.close()
    smtpObj.quit()
    print('Done')

date = input('Enter in the date: ')
e_mail = input('Enter your email: ')
psswrd = input('Enter your password: ')
choreEmailer(e_mail, psswrd, date)