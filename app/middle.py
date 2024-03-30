from django.http import HttpResponse


class FirstMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response

    def process_exception(self,request,exception):
        return HttpResponse("<center><h2>Currently we are facing technical issues, Please visit after some time.</h2></center>")

