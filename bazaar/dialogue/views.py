from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product
from .models import Dialogue
from .forms import DialogueTextStart

def new_dialogue(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    if product.created_by == request.user:
        return redirect('userprofile:index')
    
    dialogues = Dialogue.objects.filter(product=product).filter(messengers__in=[request.user.id])
    
    if dialogues:
        pass 
    if request.method == 'POST':
        form = DialogueTextStart(request.POST)

        if form.is_valid():
            dialogue = Dialogue.objects.create(product=product)
            dialogue.messengers.add(request.user)
            dialogue.messengers.add(product.created_by)
            dialogue.save()
            
            dialogue_text = form.save(commit=False)
            dialogue_text.dialogue = dialogue
            dialogue_text.created_by = request.user
            dialogue_text.save()

            return redirect('product:detail', pk=product_pk)
        else:
            form = DialogueTextStart()
        return render(request, 'dialogue/new.html', {
            'form': form
        })
