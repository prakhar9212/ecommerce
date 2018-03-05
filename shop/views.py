from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Buyer, Product, AllMobilePhoneSpecification, ProductCatagory, ProductSubcatagory, Order
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
@login_required(login_url='/login')
def index(request):
    user = request.user
    all_products = Product.objects.filter(seller = user.seller)
    all_buyers = Buyer.objects.filter(seller= user.seller)
    all_orders = Order.objects.all()
    product_count = len(all_products)
    buyer_count = len(all_buyers)
    order_count = len(all_orders)


    context = {
        'product_count':product_count,
        'buyer_count': buyer_count,
        'order_count': order_count,
        'user':user

    }

    return render(request,'index.html',context)

@login_required(login_url='/login')
def products(request):
    user = request.user
    all_products = Product.objects.filter(seller=user.seller)


    context = {
        'user':user,
        'all_products':all_products,

    }

    return render(request,'products.html',context)
@login_required(login_url='/login')
def productDetail(request,pk):
    product = Product.objects.get(pk = pk)
    user = request.user

    try:
        if product.allmobilephonespecification:
            specification = product.allmobilephonespecification.__dict__

    except:
        specification = None
    context = {
        'user':user,
        'product':product,
        'specification':specification
    }
    return render(request,'e_commerce.html',context)

class ProductCreate(CreateView):
    model = Product
    template_name = 'product_form.html'
    success_url = reverse_lazy('products')
    fields = ['product_subcatagory', 'product_id', 'brand', 'name', 'mrp', 'price', 'short_desc', 'full_desc', 'image']

    def form_valid(self, form):
        form.instance.seller = self.request.user.seller
        form.instance.discount = ((form.instance.mrp - form.instance.price)/form.instance.mrp)*100
        print(form.instance.seller)
        return super(ProductCreate, self).form_valid(form)

class ProductUpdate(UpdateView):
    model = Product
    template_name = 'product_form.html'
    success_url = reverse_lazy('products')
    fields = ['product_subcatagory', 'product_id', 'brand', 'name', 'mrp', 'price', 'short_desc', 'full_desc', 'image']

    def form_valid(self, form):

        if form.instance.seller == self.request.user.seller:
            form.instance.seller = self.request.user.seller
            form.instance.discount = ((form.instance.mrp - form.instance.price) / form.instance.mrp) * 100
            print(form.instance.seller)
            return super(ProductUpdate, self).form_valid(form)



class ProductDelete( DeleteView):
    model = Product

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        obj = super(ProductDelete, self).get_object()
        if not obj.seller == self.request.user.seller:
            raise Http404

        return obj

    def get_success_url(self):
        return reverse_lazy('products')




class SubcatagoryCreate(CreateView):
    model = ProductSubcatagory
    fields = '__all__'
    template_name = 'SubcatagoryCreate.html'
    success_url = reverse_lazy('products')

def orders(request):
    user = request.user
    all_orders = Order.objects.filter(seller=user.seller)


    context = {
        'user':user,
        'all_orders':all_orders,

    }

    return render(request,'orders.html',context)

class OrderUpdate(UpdateView):
    model = Order
    fields =['Order_id', 'buyer', 'product', 'total_cost', 'shipping_address', 'city', 'pin_code', 'payment_status', 'order_status','payment_mode']
    template_name = 'orderUpdate.html'
    success_url = reverse_lazy('orders')

    def form_valid(self, form):
        if form.instance.seller == self.request.user.seller:

            print(form.instance.seller)
            return super(OrderUpdate, self).form_valid(form)


class OrderDelete( DeleteView):
    model = Order

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        obj = super(OrderDelete, self).get_object()
        if not obj.seller == self.request.user.seller:
            raise Http404

        return obj

    def get_success_url(self):
        return reverse_lazy('orders')

class BuyerList(ListView):

    model = Buyer
    template_name = 'buyers.html'

    context_object_name = 'buyer_list'
    def get_queryset(self):
        return Buyer.objects.filter(seller=self.request.user.seller).order_by('name')


class BuyerDetail(DetailView):
    model = Buyer
    template_name = 'profile.html'
    context_object_name = 'buyer'
    def get_context_data(self, **kwargs):
        context = super(BuyerDetail, self).get_context_data(**kwargs)
        context['order'] = Order.objects.filter(buyer = Buyer.objects.get(pk=self.kwargs['pk']))
        return context


