from django.shortcuts import render

# 404 error view (Page Not Found)
def custom_page_not_found_view(request, exception):
    return render(request, 'error/404.html', status=404)

# 500 error view (Server Error)
def custom_server_error_view(request):
    return render(request, 'error/500.html', status=500)

# 403 error view (Forbidden)
def custom_permission_denied_view(request, exception):
    return render(request, 'error/403.html', status=403)

# 400 error view (Bad Request)
def custom_bad_request_view(request, exception):
    return render(request, 'error/400.html', status=400)
