from django.urls import path
from .views import create_product,product_details,product_update_view,product_delete_view
from .views import SearchView,add_saved,get_saved_products,new_comment,delete_comment


urlpatterns = [
    path('add/', create_product, name='create'),
    path('product/<int:product_id>/', product_details, name='product_details'),
    path('product/<int:product_id>/update/', product_update_view, name='update'),
    path('product/<int:product_id>/delete/', product_delete_view, name='delete'),
    path('search/results/',SearchView.as_view(), name='search'),  
    path('saved/add/<int:product_id>/', add_saved, name='add_saved'),
    path('saved/products', get_saved_products, name='get_saved_products'),
    path('<int:product_id>/comments/new/', new_comment, name='comment_new'),
    path('<int:product_id>/comments/<int:comment_id>/delete', delete_comment, 
                                                                name='comment_delete'),
]

