from django.shortcuts import render, redirect
from django.views import View
from .models import Products,Category,Search
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status


class CategoryListView(View):
    def get(self,request):
        category = Category.objects.all()
        contex = {
            'category':category,
        }
        return render(request, 'main/shop.html',contex)

    @action(detail=True, methods=['GET'])
    def look(self, request, *args, **kwargs):
        category = self.get_object()
        category.watched += 1
        category.save()
        return Response(category.watched, status=status.HTTP_200_OK)


class ProductsListView(View):
    def get(self,request):
        products = Products.objects.all()
        contex = {
            'product':products
        }
        return render(request, 'main/shop-detail.html',contex)

    @action(detail=True, methods=['GET'])
    def buy_counter(self,request,*args,**kwargs):
        product = self.get_object()
        product.buy_count+= 1
        product.save()
        return Response(product.buy_count,status=status.HTTP_200_OK)




class SearchResultsView(View):
    def get(self, request):
        query = request.GET.get('query')
        results = Products.objects.filter(title=query)
        return render(request, 'search_results.html', {'results': results, 'query': query})





