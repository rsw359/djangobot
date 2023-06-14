from django.shortcuts import render, redirect
from django.http import JsonResponse
from .config import API_KEY
import openai

from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat

from django.utils import timezone

openai.api_key = API_KEY

#Use with gpt-3 model
# def ask_gpt3(message): 
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=message,
#         max_tokens=150,
#         n=1,
#         stop=None,
#         temperature=0.7,
#     )
#     print(response)
#     # strips formatting from the response
#     answer = response.choices[0].text.strip()
#     return answer

#for use with gpt-4 chat completion model
def ask_gpt4(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': 'system', 'content':"you are a helpful assistant"},
            {'role':'user', 'content': message}
        ]

    )
    print(response)
    # define the answer and strip formatting from the response
    answer = response.choices[0].message.content.strip()
    return answer


def chatbot(request):

    chats = Chat.objects.filter(user=request.user).order_by('-created_at')[:10]
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_gpt4(message)#change to ask_gpt3 if using the older model

        # save the message and response object to the database
        chat = Chat(user=request.user, message=message,
                    response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({"message": message, 'response': response})

    return render(request, 'chatbot.html', {'chats': chats})


def login(request):
    if request.method == 'POST':
        usernames = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(
            request, username=usernames, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('chatbot')
        else:
            error_message = 'Invalid credentials'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('chatbot')
            except:
                error_message = "Error. Couldn't register"
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Passwords do not match'
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')
