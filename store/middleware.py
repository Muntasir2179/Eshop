from django.shortcuts import redirect


def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        return_url = request.META['PATH_INFO']
        if not request.session.get('customer'):
            return redirect(f'login?return_url={return_url}')
            # return redirect(f'login?return_url={return_url}')
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
