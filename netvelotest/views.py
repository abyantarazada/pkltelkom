import speedtest as st

from django.shortcuts import render
from django.http import JsonResponse

from .models import Netvelocity



# Create your views here.
def netvelocity_view(request):
	obj = Netvelocity.objects.all()

	context = {
		'objects': obj
	}
	return render(request, 'netvelotest/netvelotest_view.html', context)

def speed_count(request):
	if request.method == 'GET':
		print(request.GET['server'])
		server_id = request.GET['server']
		obj = Netvelocity.objects.filter(server = server_id)
		for item in obj:
			test = st.Speedtest()
			server = [item.server]
			test.get_servers(server)
			data = {
				"download":round(test.download()/1000000),
				"upload":round(test.upload()/1000000),
				"ping":round(test.results.ping),
				"isp":test.results.client['isp']
			}
			return JsonResponse(data)
