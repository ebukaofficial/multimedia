from django.shortcuts import render
# from .models import Image

def multimedia(request):
  # images = Image.objects.all()
  return render (request, 'multimedia/index.html')

# from django.shortcuts import render
# from .models import Image

# def image_list(request):
#     images = Image.objects.all()
#     return render(request, 'image_list.html', {'images': images})
