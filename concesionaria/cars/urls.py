from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from cars.views.car_views import (
    CarView,
    CarFilter,
    CarDetail,
    )

from cars.views.comment_views import(
    CommentUpdate,
    CommentDelete,
)

from cars.views.reivew_views import(
    ReviewCreate,
    ReviewUpdate,
)

from cars.views.sales_views import(
    SaleView,
    SaleList,
)

urlpatterns = [
    path(route='', view=CarView.as_view(), name='car_list'),
    path(route='<int:price_gte>/<int:price_lte>/<int:brand_id>/<int:used>/<int:category_id>/<int:year_gte>/<int:year_lte>/list/', view=CarFilter.as_view(), name='car_filter'),
    path(route='<int:id>/detail/', view=CarDetail.as_view(), name='car_detail'),
    path(route='comment/<int:id>/update/', view=login_required(CommentUpdate.as_view(), login_url=('login')), name='comment_update'),
    path(route='comment/<int:id>/delete/', view=login_required(CommentDelete.as_view(), login_url=('login')), name='comment_delete'),
    path(route='review/<int:id>/', view=login_required(ReviewCreate.as_view(), login_url=('login')), name='review_create'),
    path(route='review/<int:id>/update/', view=login_required(ReviewUpdate.as_view(), login_url=('login')), name='review_update'),
    path(route='sale/<int:id>/create/', view=login_required(SaleView.as_view(), login_url=('login')), name='sale_create'),
    path(route='sale/list/', view=staff_member_required(SaleList.as_view(), login_url=('index')), name='sale_list'),
]