class HandlerGET:
    def __init__(self, func):
        self.func = func

    def __call__(self, request: dict, *args, **kwargs):
        if 'method' in request.keys() and request['method'] != "GET":
            return None
        return self.get(self.func, request)

    def get(self, func, request: dict, *args, **kwargs):
        return f"GET: {func(request)}"


@HandlerGET
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "GET", "url": "contact.html"})
print(res)