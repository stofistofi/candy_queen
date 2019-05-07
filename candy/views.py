from django.shortcuts import render, get_object_or_404, redirect

from candy.froms.candy_form import CandyCreateForm
from candy.models import Candy, CandyImage


# Create your views here.


def index(request):
    context = {'candies': Candy.objects.all().order_by('name')}
    return render(request, 'candy/index.html', context)

# /candies/3
def get_candy_by_id(request, id):
    return render(request, 'candy/candy_details.html', {
        'candy': get_object_or_404(Candy, pk=id)
    })

def create_candy(request):
    if request.method == 'POST':
        form = CandyCreateForm(data=request.POST)
        if form.is_valid():
            candy = form.save()
            candy_image = CandyImage(image=request.POST['image'], candy=candy)
            candy_image.save()
            return redirect('candy-index')
    else:
        form = CandyCreateForm()
    return render(request, 'candy/create_candy.html',{
        'form': form
    })