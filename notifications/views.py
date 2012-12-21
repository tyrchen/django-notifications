# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template.context import RequestContext
from .utils import slug2id
from notifications.models import Notification

@login_required
def list(request):
    """
    Index page for authenticated user
    """
    Notification.objects.mark_all_as_visited(request.user)
    actions = Notification.objects.filter(recipient=request.user)

    paginator = Paginator(actions, 12) # Show 16 notifications per page
    page = request.GET.get('p')
    if not isinstance(page, int) and page is not None:
      page = int(page)

    try:
        action_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = 1
        action_list = paginator.page(page)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        action_list = paginator.page(paginator.num_pages)

    return render_to_response('notifications/list.html', {
        'member': request.user,
        'unread_count': Notification.objects.unread_count(request.user),
        'action_list': action_list,
        'total_page': paginator.num_pages,
        'current_page': page,
        'current_url': '/notifications/?p=',
    }, context_instance=RequestContext(request))

@login_required
def read_all(request):
    Notification.objects.mark_all_as_read(request.user)

    return redirect('notifications_list')

@login_required
def read(request, slug=None):
    id = slug2id(slug)

    notification = get_object_or_404(Notification, recipient=request.user, id=id)
    notification.mark_as_read()

    next = request.REQUEST.get('next')

    if next:
        return redirect(next)

    return redirect('notifications_list')
