from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    ############# Function based ##############
    # path("menu-items/", views.menu_items),
    # path("menu-items/<int:id>", views.single_item),
    
    ############# Class based ###################
    # path('menu-items/', views.MenuItemsViewSet.as_view({'get':'list'})),
    # path('menu-items/<int:pk>', views.MenuItemsViewSet.as_view({'get':'retrieve'})),
    
    #### Getting Auth tokens of a specific user from an API endpoint
    #### You can also GENERATE a user's Token
    #### Token_based_Authentication
    path('api-token-auth/', obtain_auth_token), # This endpoint only accepts HTTP Post calls.
    path('secret/', views.secret),

    ############ Class based using Generics from rest_framework #############
    path('category/', views.CategoriesView.as_view()),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('manager-view/', views.manager_view),
    path('throttle-check/', views.throttle_check),
    path('throttle-check-auth/', views.throttle_check_auth),
    # path('me/', views.me),
    path('groups/manager/users/', views.managers),

]