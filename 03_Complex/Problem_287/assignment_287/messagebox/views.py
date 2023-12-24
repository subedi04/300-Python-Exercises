from django.shortcuts import render
from django.http import JsonResponse
from .models import MessageBox

def message_box(request, box_type):
    if box_type == 'yes_no':
        title = 'Yes/No Message Box'
        message = 'Do you want to proceed?'
    elif box_type == 'info':
        title = 'Information Message Box'
        message = 'This is an informative message.'
    else:
        return JsonResponse({'error': 'Invalid message box type'})

    return render(request, 'messagebox_app/message_box.html', {'title': title, 'message': message, 'box_type': box_type})

