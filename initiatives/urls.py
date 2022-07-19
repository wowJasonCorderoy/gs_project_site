from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='initiatives_home'),
    path('channel_strategy/', views.channel_strategy, name='channel_strategy'),
    path('demand_forecasting/', views.demand_forecasting, name='demand_forecasting'),
    path('livestock_sourcing/', views.livestock_sourcing, name='livestock_sourcing'),
    path('supplementary_sourcing/', views.supplementary_sourcing, name='supplementary_sourcing'),
    path('primary_processing/', views.primary_processing, name='primary_processing'),
    path('inv_and_prod/', views.inv_and_prod, name='inv_and_prod'),
    path('secondary_processing/', views.secondary_processing, name='secondary_processing'),
    path('retail_and_b2b_sales/', views.retail_and_b2b_sales, name='retail_and_b2b_sales'),
    path('demand_as_cattle/', views.demand_as_cattle, name='demand_as_cattle'),
    path('yield_trees/', views.yield_trees, name='yield_trees'),
    path('news/', views.news, name='news'),
    path('plan/', views.plan, name='plan'),
    path('buy/', views.buy, name='buy'),
    path('make/', views.make, name='make'),
    path('sell/', views.sell, name='sell'),
]
