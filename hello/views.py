from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import SessionForm
# Create your views here.

class HelloView(TemplateView):

  def __init__(self):
    self.params = {
      'title': 'Hello',
      'form': SessionForm(),
      'result': None
    }
  
  def get(self, request):
    self.params['result'] = request.session.pop('last_msg', 'なにもないよ')
    return render(request, 'hello/index.html', self.params)
  
  def post(self, request):
    ses = request.POST['session']
    self.params['result'] = f'{ses}'
    request.session['last_msg'] = ses
    self.params['form'] = SessionForm(request.POST)
    return render(request, 'hello/index.html', self.params)
  
# def sample_middleware(get_response):
#   def middleware(request):
#     counter = request.session.get('counter', 0)
#     request.session['counter'] = counter + 1
#     response = get_response(request)
#     print(f'count: {str(counter)}')
#     return response
#   return middleware