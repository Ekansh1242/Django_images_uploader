from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator

from .models import UploadedImage
from .forms import ImageUploadForm


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                image_instance = form.save(commit=False)
                image_instance.full_clean()
                image_instance.save()
                messages.success(request, f'Image "{image_instance}" uploaded successfully!')
                return redirect('gallery:gallery')
            except ValidationError as e:
                messages.error(request, f'Upload failed: {e}')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = ImageUploadForm()

    return render(request, 'gallery/upload.html', {'form': form})


def gallery_view(request):
    images_list = UploadedImage.objects.all()
    paginator = Paginator(images_list, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'gallery/gallery.html', {
        'page_obj': page_obj,
        'total_images': images_list.count(),
    })


@require_POST
def delete_image(request, pk):
    image = get_object_or_404(UploadedImage, pk=pk)
    title = str(image)
    image.delete()
    messages.success(request, f'Image "{title}" was deleted successfully.')
    return redirect('gallery:gallery')
