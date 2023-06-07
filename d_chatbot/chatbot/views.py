from django.shortcuts import render
from django.http import JsonResponse
from .config import API_KEY
import openai


openai.api_key = API_KEY


def ask_gpt3(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    print(response)
    # strips formatting from the response
    answer = response.choices[0].text.strip()
    return answer


def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_gpt3(message)
        return JsonResponse({"message": message, 'response': response})
    return render(request, 'chatbot.html')
