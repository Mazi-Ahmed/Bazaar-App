from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product
from .models import Dialogue
from .forms import DialogueTextStart

@login_required
def new_dialogue(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    if product.created_by == request.user:
        return redirect('userprofile:index')
    
    dialogues = Dialogue.objects.filter(product=product, messengers__in=[request.user.id])
    
    if dialogues:
        return redirect('dialogue:detail', pk=dialogues.first().id)
    
    if request.method == 'POST':
        form = DialogueTextStart(request.POST)

        if form.is_valid():
            dialogue = Dialogue.objects.create(product=product)
            dialogue.messengers.add(request.user)
            dialogue.messengers.add(product.created_by)
            dialogue.save()
            
            dialogue_text = form.save(commit=False)
            dialogue_text.dialogue = dialogue
            dialogue_text.created_dialogue = request.user
            dialogue_text.save()

            return redirect('product:detail', pk=product_pk)
    else:
        form = DialogueTextStart()
    return render(request, 'dialogue/new.html', {
        'form': form
    })

@login_required
def inbox(request):
    dialogues = Dialogue.objects.filter(messengers__in=[request.user.id])
    return render(request, 'dialogue/inbox.html', {
        'dialogues': dialogues
    })

@login_required
def detail(request, pk):
    dialogue = Dialogue.objects.filter(messengers__in=[request.user.id]).get(pk=pk)
    if request.method == 'POST':
        form = DialogueTextStart(request.POST)
        if form.is_valid():
            dialogue_message = form.save(commit=False)
            dialogue_message.dialogue = dialogue
            dialogue_message.created_dialogue = request.user
            dialogue_message.save()
            dialogue.save()
            return redirect('dialogue:detail', pk=pk)
    else:
        form = DialogueTextStart()
    return render(request, 'dialogue/detail.html', {
        'dialogue': dialogue,
        'form': form
    })