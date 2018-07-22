from django.shortcuts import render, HttpResponse, redirect
import random
import datetime

#from flask import Flask, render_template, request, redirect, request.session
#app.yourgold = 0

def generate_gold(request, loc):
    newgold = 0
    winlose = 0
    if loc == "farm":
        newgold = random.randrange(10,21)
        request.session['yourgold'] = request.session['yourgold'] + newgold
        request.session['activity'].insert(0, 'Earned ' + str(newgold) + ' golds from the farm! (' + datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p)"))
    elif loc == "cave":
        newgold = random.randrange(5,11)
        request.session['yourgold'] = request.session['yourgold'] + newgold
        request.session['activity'].insert(0, 'Earned ' + str(newgold) + ' golds from the cave! (' + datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p)"))
    elif loc == "house":
        newgold = random.randrange(2,6)
        request.session['yourgold'] = request.session['yourgold'] + newgold
        request.session['activity'].insert(0, 'Earned ' + str(newgold) + ' golds from the house! (' + datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p)"))
    elif loc == "casino":
        winlose = random.randrange(1,3)
        if winlose == 1:
            newgold = random.randrange(0,51)
            request.session['yourgold'] = request.session['yourgold'] + newgold
            request.session['activity'].insert(0, 'Earned ' + str(newgold) + ' golds from the casino! (' + datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p)"))
        else:
            newgold = random.randrange(10,21)
            request.session['yourgold'] = request.session['yourgold'] - newgold
            request.session['activity'].insert(0, 'Entered a casino and lost ' + str(newgold) + ' golds.. Ouch.. (' + datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p)"))

def index(request):
    if 'yourgold' not in request.session:
        request.session['yourgold'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = []

    yourgold = request.session['yourgold']
    activity = request.session['activity']
    return render(request, 'ninja_gold/index.html')

# @app.route('/process_money', methods = ['POST'])
def process_money(request, location):
#    your_location = request.form.get('building')
    yourgold = request.session['yourgold']
    generate_gold(request, location)

    return redirect('/')