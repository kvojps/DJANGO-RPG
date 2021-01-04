from django.shortcuts import render,redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages

# Create your views here.
def home(request):
    all_members = Member.objects.all
    return render(request, 'home.html', {'all':all_members})

def join(request) :
    if request.method == 'POST':
        form =  MemberForm(request.POST or None)
        if form.is_valid():
            form.save()

        else :
            nome = request.POST['nome']
            nivel = request.POST['nivel']
            raca = request.POST['raca']
            vida = request.POST['vida']
            mana = request.POST['mana']
            poder = request.POST['poder']
            dificuldade = request.POST['dificuldade']

            messages.success(request,("Tente novamente !"))
            #return redirect('join')
            return render(request, 'join.html', {'nome': nome,
                'nivel': nivel,
                'raca': raca,
                'vida': vida,
                'mana': mana,
                'poder': poder,
                'dificuldade': dificuldade,
                })

        messages.success(request, ('Seu personagem foi criado com sucesso !'))
        return redirect('home')
    else :
        return render(request, 'join.html', {})
    
