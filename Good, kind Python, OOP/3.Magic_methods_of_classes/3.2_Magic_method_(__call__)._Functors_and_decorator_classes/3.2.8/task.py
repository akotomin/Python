class Handler:
    def __init__(self, methods):
        self.methods = methods

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            method = request.get('method', 'GET')
            if method in self.methods:
                if method == 'GET':
                    return self.get(func, request)
                else:
                    return self.post(func, request)
            return None
        return wrapper

    def get(self, func, request: dict, *args, **kwargs):
        return f"GET: {func(request)}"

    def post(self, func, request: dict, *args, **kwargs):
        return f"POST: {func(request)}"

@Handler(methods=('GET', 'POST'))  # по умолчанию methods = ('GET',)
def contact(request):
    return "Сергей Балакирев"
