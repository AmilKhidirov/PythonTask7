from django.shortcuts import render

# Create your views here.


def index(request):
    kimdir = ''
    if request.method == 'POST':
        if request.POST['name'] == 'Aslan':
            kimdir = 'Aslan emi ogludur'

        elif request.POST['name'] == 'Imran':
            kimdir = 'Imran dayi ogludur'

        elif request.POST['name'] == 'Afaq':
            kimdir = 'Afaq bibi qizidir'

        elif request.POST['name'] == 'Uzeyir':
            kimdir = 'Uzeyir xala ogludur'

        elif request.POST['name'] == 'Sahin':
            kimdir = 'Sahin yaxin dostdur'

        elif request.POST['name'] == '':
            kimdir = 'Ad daxil etmediniz'

        else:
            kimdir = f'{request.POST['name']} kimdir men onu tanimadim'
            
    return render(request, 'index.html', {'ad': kimdir})


def index(request):
        isci = ''
        if request.method == 'POST':
            if request.POST['Vezife'] == 'Vekil':
                isci = 'Vekil'

            elif request.POST['Vezife'] == 'Hekim':
                isci = 'Hekim'

            elif request.POST['Vezife'] == 'Polis':
                isci = 'Polis'
    
        return render(request, 'index.html', {'vezife': isci})


def index(request):
    soz = ''
    if request.method == 'POST':
        soz = len(request.POST['b'])

    return render(request, 'index.html', {'soz': soz})


def index(request):
    cumle = ''
    if request.method == 'POST':
        cumle = len(request.POST['a2'].split())

    return render(request, 'index.html', {'cumle': cumle})