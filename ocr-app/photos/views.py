from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, TemplateView
from .models import Image



class GalleryView(ListView):
    model = Image
    context_object_name = 'images'
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['images'] = context['images'].filter(recognized_text__icontains=search_input)
        
        
        context['search_input'] = search_input
        return context
    


class PhotoView(DetailView):
    model = Image
    context_object_name = 'image'
    template_name = 'photo.html'


def make_prediction(request):
    if request.method == 'GET':
        for image in Image.objects.all():
            if Image.objects.filter(pk=image.pk).filter(recognized_text='').exists():
                 
                photo = Image.objects.get(pk=image.pk)

                print(photo.image) #получаем название фотки, далее с помошью нее можно пройти по статику

                Image.objects.filter(pk=image.pk).update(recognized_text='test3')
    
    return redirect('gallery')



def delete_images(request):
    Image.objects.all().delete()
    return redirect('gallery')

def addPhoto(request):
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('image')


        for image in images:
            print(image)
            photo = Image.objects.create(
                name=data['name'],
                image=image,
                recognized_text='',
            )
            
        # print(images)
        return redirect('gallery')

    return render(request, 'add.html')

