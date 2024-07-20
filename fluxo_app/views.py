from django.shortcuts import render, redirect,get_object_or_404

from django.http import HttpResponse
import math
from .models import Tabela
                  
                  


def Lista_projetos():    
    lista_projetos = Tabela.objects.values_list('projeto', flat=True).distinct()
    return lista_projetos

def dados_grafico(nome_proj_selecionado):
    soma_projetos_1 = Tabela.objects.filter(projeto=nome_proj_selecionado , fase=1).count()
    soma_projetos_2 = Tabela.objects.filter(projeto=nome_proj_selecionado , fase=2).count()
    soma_projetos_3 = Tabela.objects.filter(projeto=nome_proj_selecionado , fase=3).count()
    soma_projetos_4 = Tabela.objects.filter(projeto=nome_proj_selecionado , fase=4).count()
    soma_projetos_5 = Tabela.objects.filter(projeto=nome_proj_selecionado , fase=5).count()
    soma_projetos_6 = Tabela.objects.filter(projeto=nome_proj_selecionado , fase=6).count()
    soma_projetos_7 = Tabela.objects.filter(projeto=nome_proj_selecionado , fase=7).count()
    soma_concluido_1 = Tabela.objects.filter(projeto=nome_proj_selecionado, status='Concluido', fase=1).count()
    soma_concluido_2 = Tabela.objects.filter(projeto=nome_proj_selecionado, status='Concluido', fase=2).count()
    soma_concluido_3 = Tabela.objects.filter(projeto=nome_proj_selecionado, status='Concluido', fase=3).count()
    soma_concluido_4 = Tabela.objects.filter(projeto=nome_proj_selecionado, status='Concluido', fase=4).count()
    soma_concluido_5 = Tabela.objects.filter(projeto=nome_proj_selecionado, status='Concluido', fase=5).count()
    soma_concluido_6 = Tabela.objects.filter(projeto=nome_proj_selecionado, status='Concluido', fase=6).count()
    soma_concluido_7 = Tabela.objects.filter(projeto=nome_proj_selecionado, status='Concluido', fase=7).count()
    print(soma_projetos_1,soma_projetos_2,soma_projetos_3,soma_projetos_4,soma_projetos_5,soma_projetos_6,soma_projetos_7)
    print(soma_concluido_1,soma_concluido_2,soma_concluido_3,soma_concluido_4,soma_concluido_5,soma_concluido_6,soma_concluido_7)
    if soma_projetos_1 == 0: 
        razao_1 = 0
    else:
        razao_1 = int((soma_concluido_1/soma_projetos_1)*100)
    if soma_projetos_2 == 0: 
        razao_2 = 0
    else:
        razao_2 = int((soma_concluido_2/soma_projetos_2)*100)
    if soma_projetos_3 == 0:
        razao_3 = 0    
    else:     
        razao_3 = int((soma_concluido_3/soma_projetos_3)*100)
    if soma_projetos_4 == 0: 
        razao_4 = 0
    else:     
        razao_4 = int((soma_concluido_4/soma_projetos_4)*100)
    if soma_projetos_5 == 0: 
        razao_5 = 0
    else:     
        razao_5 = int((soma_concluido_5/soma_projetos_5)*100)
    if soma_projetos_6 == 0:
        razao_6 = 0
    else:     
        razao_6 = int((soma_concluido_6/soma_projetos_6)*100)
    if soma_projetos_7 == 0: 
        razao_7 = 0
    else:     
        razao_7 = int((soma_concluido_7/soma_projetos_7)*100)
    
    return  soma_projetos_1,soma_projetos_2,soma_projetos_3,soma_projetos_4,soma_projetos_5,soma_projetos_6,soma_projetos_7,razao_1,razao_2,razao_3,razao_4,razao_5,razao_6,razao_7

def home(request):

    nome_proj_selecionado=request.POST.get('proj_selecionado') #pega o projeto selecionado no botao invisivel
    if nome_proj_selecionado == None:
        nome_proj_selecionado =request.session.get('valor')
    print(f'botao invisivel botao invisivel botao invisivel= {nome_proj_selecionado} ')
    request.session['valor']=nome_proj_selecionado# salva o nome do projeto na variavel valor

    if Tabela.objects.exists():
       lista_projetos = Lista_projetos()
    else:
        return render(request, 'criar_proj.html')

    if request.method == "POST":
        print(f'IF IF IF IF IF IF IF IF IF IF IF IF IF IF IF IF IF IF IF IF IF IF IF I VEM DO BOTAO ATT PROJETO ')
        
        nome_proj_selecionado = request.session.get('valor')  # Recupera o valor da session
        
        print(f' nome_proj_selecionado nome_proj_selecionado nome_proj_selecionado {nome_proj_selecionado}')
        soma_proj_fase = dados_grafico(nome_proj_selecionado) # quantidade total de fases de cada projeto e a razão de soma/soma_projeto
        dados= Tabela.objects.order_by('fase').filter(projeto =nome_proj_selecionado)#pega os dados filtrados pela projeto selecionado pelo usuario
        return render(request,'home.html',{
            'lista_projetos':lista_projetos,
            'nome_proj_selecionado':nome_proj_selecionado,
            'soma_proj_fase':soma_proj_fase,
            'dados':dados})
    else:
        
        print('else else else else else else else else else else else else else else  VEM DA PÁGINA NOVA ')
        print(nome_proj_selecionado)
        if nome_proj_selecionado is None:
            nome_proj_selecionado=Tabela.objects.order_by('id').last().projeto
            request.session['valor']=nome_proj_selecionado
            
        soma_proj_fase = dados_grafico(nome_proj_selecionado) # quantidade total de fases de cada projeto e a razão de soma/soma_projeto
        dados= Tabela.objects.order_by('fase').filter(projeto =nome_proj_selecionado)
        return render(request,'home.html',{
            'lista_projetos':lista_projetos,
            'nome_proj_selecionado':nome_proj_selecionado,
            'soma_proj_fase':soma_proj_fase,
            'dados':dados})

def editar_proj(request):
    projetos = Tabela.objects.values_list('projeto', flat=True).distinct()
    

        
    return render(request, 'editar_proj.html',{'projetos':projetos})

def delete(request):
    metodo = request.method
    print(f'method delete = {metodo} method delete = {metodo} method delete = {metodo} method delete = {metodo} method delete = {metodo} ')
    id= request.POST.get('num_botao')
    nome_proj_selecionado=request.POST.get('proj_selecionado')
    print(nome_proj_selecionado)
    item= Tabela.objects.get(id=id)
    item.delete()
        
    print(f'O NOME DO PROJETO APAGADO É: {nome_proj_selecionado}')
    request.session['valor']=nome_proj_selecionado# salva o nome do projeto na variavel valor
    if Tabela.objects.filter(projeto=nome_proj_selecionado).exists():
        print('if delete if delete if delete if delete if delete if delete if delete if delete if delete if delete if delete if delete if delete if delete ')
        lista_projetos = Lista_projetos()
        soma_proj_fase = dados_grafico(nome_proj_selecionado) # quantidade total de fases de cada projeto e a razão de soma/soma_projeto
        dados= Tabela.objects.order_by('fase').filter(projeto =nome_proj_selecionado)#pega os dados filtrados pela projeto selecionado pelo usuario
        print('oi oi oi oi oi oi oi oi oi oi oi oi oiFOI PARA O QUEST DO HOME oi oi oi oi oi oi oi oi oi oi oi oi oi oi oi oi oi oi oi oi oi oi oi ')
        return redirect('home')
def home2(request):
    
    return redirect('home')
def salvar(request):
    nome_fase=request.POST.get('nome_fase')
    nome_descricao=request.POST.get('nome_descricao')
    nome_inicio_data=request.POST.get('nome_inicio_data')
    nome_fim_data=request.POST.get('nome_fim_data')
    nome_responsavel=request.POST.get('nome_responsavel')
    nome_status=request.POST.get('nome_status')
    nome_proj_selecionado=request.POST.get('nome_projeto_btn')
    if nome_inicio_data == "":
        nome_inicio_data=None
    if nome_fim_data =="":
        nome_fim_data=None
        
    dados=Tabela(fase=nome_fase,descricao=nome_descricao,inicio_data=nome_inicio_data,fim_data=nome_fim_data,responsavel=nome_responsavel,status=nome_status,projeto=nome_proj_selecionado)
    dados.save()
    lista_projetos = Lista_projetos()
    soma_proj_fase = dados_grafico(nome_proj_selecionado) # quantidade total de fases de cada projeto e a razão de soma/soma_projeto
    dados= Tabela.objects.order_by('fase').filter(projeto =nome_proj_selecionado)

    return redirect('home')    
def edit(request):

    indice = request.POST.get('num_botao')
    dados=Tabela.objects.get(id =indice)
    projetos = Tabela.objects.values_list('projeto', flat=True).distinct()
    
    return render(request, 'edit.html',{'projetos':projetos,'dados':dados})
def alter(request):

    nome_id=request.POST.get('nome_id_btn')
    nome_fase=request.POST.get('nome_fase')
    nome_descricao=request.POST.get('nome_descricao')
    nome_inicio_data=request.POST.get('nome_inicio_data')
    nome_fim_data=request.POST.get('nome_fim_data')
    nome_responsavel=request.POST.get('nome_responsavel')
    nome_status=request.POST.get('nome_status')
    nome_proj_selecionado=request.POST.get('nome_projeto_btn')
    if nome_inicio_data == "":
        nome_inicio_data=None
    if nome_fim_data =="":
        nome_fim_data=None
    dados=Tabela(id=nome_id, fase=nome_fase,descricao=nome_descricao,inicio_data=nome_inicio_data,fim_data=nome_fim_data,responsavel=nome_responsavel,status=nome_status,projeto=nome_proj_selecionado)
    dados.save()
    return redirect ('home')
def apaga_projeto(request):
    nome_projeto = request.POST.get('num_botao')
    print(f'o nome do projeto é {nome_projeto} o nome do projeto é {nome_projeto} o nome do projeto é {nome_projeto} o nome do projeto é {nome_projeto} o nome do projeto é {nome_projeto} o nome do projeto é {nome_projeto} ')
    Tabela.objects.filter(projeto=nome_projeto).delete()
    request.session['valor']=''
    return redirect('editar_proj')
def criar_proj(request):
    proj_adicionado=request.POST.get('proj_adicionado')
    request.session['valor']=proj_adicionado
    dados=Tabela(projeto=proj_adicionado)
    dados.save()
    return redirect('home')
def duplicar_projeto(request):
    proj_adicionado = request.POST.get('proj_selecionado')
    
    return render(request, 'duplicar_projeto.html',{'proj_adicionado':proj_adicionado})
def duplicar_dados(request):
    proj_adicionado = request.POST.get('proj_selecionado')
    projeto_duplicado = request.POST.get('projeto_duplicado')
    
    print(proj_adicionado)
    dados=Tabela.objects.filter(projeto = proj_adicionado)
    
    for dado in dados:
        dados_novo=Tabela(fase=dado.fase,descricao=dado.descricao,inicio_data=dado.inicio_data,fim_data=dado.fim_data,responsavel=dado.responsavel,status=dado.status,projeto=projeto_duplicado)
        dados_novo.save()

    return redirect('home')
