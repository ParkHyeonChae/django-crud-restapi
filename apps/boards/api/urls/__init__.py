from .boards import urlpatterns as board_urlpatterns  # noqa
from .comments import urlpatterns as comment_urlpatterns  # noqa
from .posts import urlpatterns as post_urlpatterns  # noqa

urlpatterns = []
urlpatterns += board_urlpatterns
urlpatterns += post_urlpatterns
urlpatterns += comment_urlpatterns
