from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def Register(request):
    errors = User.objects.reg_validation(request.POST, request.session)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, key)
        return redirect('/new')
    return redirect('/')

def Login(request):
    errors = User.objects.login_val(request.POST, request.session)
    if len(errors):
        for key, value in errors.items():
            print(key)
            messages.warning(request, value, key)
        return redirect('/')
    return redirect('/')

def Logout(request):
    request.session.clear()
    return redirect('/')

def Show(request, id):
    context = {
        'user' : User.objects.get(id = id)
    }
    return render(request, 'draft_app/show.html', context)

def My_Lineup(request, id):
    if 'position' in request.session:
        if request.session['position'] in ['RBONE', 'RBTWO']:
            position = "RB"
        if request.session['position'] in ['WRONE', 'WRTWO']:
            position = "WR"
        if request.session['position'] == 'QB':
            position = "QB"
        if request.session['position'] == 'TE':
            position = "TE"
        if request.session['position'] == 'DST':
            position = "DST"
        if request.session['position'] == 'K':
            position = "K"
        if request.session['position'] == 'FLEX':
            position = ["RB", "WR", "TE"]
        if request.session['position'] in ["BEONE", "BETWO", "BETHREE", "BEFOUR", "BEFIVE", "BESIX", "BESEVEN"]:
            position = ["QB", "RB", "WR", "TE", "DST", "K"]
        if 'picks' in request.session:
            if position == ["RB", "WR", "TE"] or position == ["QB", "RB", "WR", "TE", "DST", "K"]:
                pool = Player.objects.filter(position__in = position).exclude(id__in = request.session['picks']).order_by('pos_rank')
            else:
                pool = Player.objects.filter(position = position).exclude(id__in = request.session['picks']).order_by('pos_rank')
        else:
            if position == ["RB", "WR", "TE"] or position == ["QB", "RB", "WR", "TE", "DST", "K"]:
                pool = Player.objects.filter(position__in = position).order_by('pos_rank')
            else:
                pool = Player.objects.filter(position = position).order_by('pos_rank')
    else:
        pool = ''

    if 'lineup' in request.session:
        if 'QB' in request.session['lineup']:
            qb = Player.objects.get(id = request.session['lineup']['QB'])
        else:
            qb = ''
    else:
        qb = ''
    if 'lineup' in request.session:
        if 'RBONE' in request.session['lineup']:
            rb1 = Player.objects.get(id = request.session['lineup']['RBONE'])
        else:
            rb1 = ''
    else:
        rb1 = ''
    if 'lineup' in request.session:
        if 'RBTWO' in request.session['lineup']:
            rb2 = Player.objects.get(id = request.session['lineup']['RBTWO'])
        else:
            rb2 = ''
    else:
        rb2 = ''
    if 'lineup' in request.session:
        if 'WRONE' in request.session['lineup']:
            wr1 = Player.objects.get(id = request.session['lineup']['WRONE'])
        else:
            wr1 = ''
    else:
        wr1 = ''
    if 'lineup' in request.session:
        if 'WRTWO' in request.session['lineup']:
            wr2 = Player.objects.get(id = request.session['lineup']['WRTWO'])
        else:
            wr2 = ''
    else:
        wr2 = ''
    if 'lineup' in request.session:
        if 'TE' in request.session['lineup']:
            te = Player.objects.get(id = request.session['lineup']['TE'])
        else:
            te = ''
    else:
        te = ''
    if 'lineup' in request.session:
        if 'FLEX' in request.session['lineup']:
            flex = Player.objects.get(id = request.session['lineup']['FLEX'])
        else:
            flex = ''
    else:
        flex = ''
    if 'lineup' in request.session:
        if 'DST' in request.session['lineup']:
            dst = Player.objects.get(id = request.session['lineup']['DST'])
        else:
            dst = ''
    else:
        dst = ''
    if 'lineup' in request.session:
        if 'K' in request.session['lineup']:
            k = Player.objects.get(id = request.session['lineup']['K'])
        else:
            k = ''
    else:
        k = ''
    if 'lineup' in request.session:
        if 'BEONE' in request.session['lineup']:
            be1 = Player.objects.get(id = request.session['lineup']['BEONE'])
        else:
            be1 = ''
    else:
        be1 = ''
    if 'lineup' in request.session:
        if 'BETWO' in request.session['lineup']:
            be2 = Player.objects.get(id = request.session['lineup']['BETWO'])
        else:
            be2 = ''
    else:
        be2 = ''
    if 'lineup' in request.session:
        if 'BETHREE' in request.session['lineup']:
            be3 = Player.objects.get(id = request.session['lineup']['BETHREE'])
        else:
            be3 = ''
    else:
        be3 = ''
    if 'lineup' in request.session:
        if 'BEFOUR' in request.session['lineup']:
            be4 = Player.objects.get(id = request.session['lineup']['BEFOUR'])
        else:
            be4 = ''
    else:
        be4 = ''
    if 'lineup' in request.session:
        if 'BEFIVE' in request.session['lineup']:
            be5 = Player.objects.get(id = request.session['lineup']['BEFIVE'])
        else:
            be5 = ''
    else:
        be5 = ''
    if 'lineup' in request.session:
        if 'BESIX' in request.session['lineup']:
            be6 = Player.objects.get(id = request.session['lineup']['BESIX'])
        else:
            be6 = ''
    else:
        be6 = ''
    if 'lineup' in request.session:
        if 'BESEVEN' in request.session['lineup']:
            be7 = Player.objects.get(id = request.session['lineup']['BESEVEN'])
        else:
            be7 = ''
    else:
        be7 = ''

    context = {
        'user' : User.objects.get(id = id),
        'my_team' : Lineup.objects.filter(user = User.objects.get(id = id)),
        'length' : len(Lineup.objects.filter(user = User.objects.get(id = id))),
        'pool' : pool,
        'qb' : qb,
        'rb1' : rb1,
        'rb2' : rb2,
        'wr1' : wr1,
        'wr2' : wr2,
        'te' : te,
        'flex' : flex,
        'dst' : dst,
        'k' : k,
        'be1' : be1,
        'be2' : be2,
        'be3' : be3,
        'be4' : be4,
        'be5' : be5,
        'be6' : be6,
        'be7' : be7,
    }
    return render(request, 'draft_app/lineup.html', context)

def index(request):
    if 'id' in request.session:
        user = User.objects.get(id = request.session['id'])
    else:
        user = ''
    # Player.objects.create(first_name="Keenan", last_name="Allen", position = 'WR', pos_rank=8, depth = 1, team= Team.objects.get(id=3))
    # p = Player.objects.get(first_name = "Michael")
    # p.last_name = "Tomas"
    # p.save()
    if 'team' in request.session:
        rank = Player.objects.filter(team_id = request.session['team']).order_by('position')
    elif 'position' not in request.session:
        rank = Player.objects.order_by('last_name')
    else:
        rank = Player.objects.filter(position = request.session['position']).order_by('pos_rank')
    context = {
        'conference' : 
            {'NFC' : 
                {'NFC North' : Team.objects.filter(conference= "NFC North").order_by('name'), 
                'NFC East' : Team.objects.filter(conference= "NFC East").order_by('name'), 
                'NFC South' : Team.objects.filter(conference= "NFC South").order_by('name'), 
                'NFC West' : Team.objects.filter(conference= "NFC West").order_by('name')}, 
            'AFC' :    
                {'AFC North' : Team.objects.filter(conference= "AFC North").order_by('name'),  
                'AFC East' : Team.objects.filter(conference= "AFC East").order_by('name'), 
                'AFC South' : Team.objects.filter(conference= "AFC South").order_by('name'), 
                'AFC West' : Team.objects.filter(conference= "AFC West").order_by('name')}},
        'rank' : rank,
        'user' : user
    }
    return render(request, 'draft_app/index.html', context)

def Position(request, id):
    if 'team' in request.session:
        del request.session['team']
    request.session['position'] = id
    return redirect("/")

def Home(request):
    if 'position' in request.session:
        del request.session['position']
    if 'team' in request.session:
        del request.session['team']
    return redirect('/')

def Team_id(request, id):
    if 'position' in request.session:
        del request.session['position']
    request.session['team'] = id
    return redirect("/")

def New(request):
    return render(request, 'draft_app/new.html')

def Lineup_position(request, id, pos):
    request.session['position'] = pos
    return redirect(f'/user/{id}/lineup')

def Add(request, id, p_id):
    p = Player.objects.get(id = p_id)
    if 'lineup' in request.session:
        request.session['lineup'][f"{request.session['position']}"] = p_id
    else:
        request.session['lineup'] = {f"{request.session['position']}" : p_id}
    if 'picks' in request.session:
        request.session['picks'].append(p_id)
    else:
        request.session['picks'] = [p_id]
    if 'position' in request.session:
        del request.session['position']
    return redirect(f'/user/{id}/lineup')

def Lineup_create(request, id):
    Lineup.objects.create(
        user = User.objects.get(id = id),
        qb = Player.objects.get(id = request.session['lineup']['QB']),
        rb1 = Player.objects.get(id = request.session['lineup']['RBONE']),
        rb2 = Player.objects.get(id = request.session['lineup']['RBTWO']),
        wr1 = Player.objects.get(id = request.session['lineup']['WRONE']),
        wr2 = Player.objects.get(id = request.session['lineup']['WRTWO']),
        te = Player.objects.get(id = request.session['lineup']['TE']),
        flex = Player.objects.get(id = request.session['lineup']['FLEX']),
        dst = Player.objects.get(id = request.session['lineup']['DST']),
        k = Player.objects.get(id = request.session['lineup']['K']),
        be1 = Player.objects.get(id = request.session['lineup']['BEONE']),
        be2 = Player.objects.get(id = request.session['lineup']['BETWO']),
        be3 = Player.objects.get(id = request.session['lineup']['BETHREE']),
        be4 = Player.objects.get(id = request.session['lineup']['BEFOUR']),
        be5 = Player.objects.get(id = request.session['lineup']['BEFIVE']),
        be6 = Player.objects.get(id = request.session['lineup']['BESIX']),
        be7 = Player.objects.get(id = request.session['lineup']['BESEVEN'])
    )
    # del request.session['lineup']
    # del request.session['picks']
    return redirect(f'/user/{id}/lineup')