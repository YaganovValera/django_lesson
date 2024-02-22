import logging
from datetime import timedelta

from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from lessonapp.forms import PhotoUploadForm
from lessonapp.models import User, Order, Product

logger = logging.getLogger(__name__)


# List of user orders
def user_orders(request, pk_user):
    try:
        user = User.objects.get(pk=pk_user)
    except User.DoesNotExist:
        logger.error(f"User with id {pk_user} does not exist.")
        raise Http404("User does not exist")

    logger.info(f"A user with ID {pk_user} is logged in.")
    current_date = timezone.now()

    orders_7_days = Order.objects.\
        filter(customer=user, formation_date__gte=current_date - timedelta(days=7)).\
        order_by('formation_date')
    orders_30_days = Order.objects.\
        filter(customer=user, formation_date__gte=current_date - timedelta(days=30)).\
        order_by('formation_date')
    orders_365_days = Order.objects.\
        filter(customer=user, formation_date__gte=current_date - timedelta(days=365)).\
        order_by('formation_date')

    context = {
        'username': user.name,
        'orders_data': {
            '7 дней': orders_7_days,
            '30 дней': orders_30_days,
            '365 дней': orders_365_days,
        }
    }

    return render(request, "lessonapp/user_orders.html", context)


# start page
def base_page(request):
    return render(request, "lessonapp/base.html")


# uploading product photos
def upload_photo(request, pk_products):
    product = get_object_or_404(Product, pk=pk_products)

    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.cleaned_data['img_product']
            # Сохранить фото в файловой системе
            fs = FileSystemStorage()
            filename = fs.save(f'{photo.name}', photo)
            # Связать фото с продуктом и сохранить изменения
            product.img_product = filename
            product.save()
            return redirect('show_products')
    else:
        form = PhotoUploadForm()

    return render(request, 'lessonapp/upload_photo.html', {'form': form, 'product': product})


def show_products(request):
    products = Product.objects.all()
    return render(request, 'lessonapp/show_products.html', {'products': products})


def show_users(request):
    users = User.objects.all()
    return render(request, 'lessonapp/show_users.html', {'users': users})

