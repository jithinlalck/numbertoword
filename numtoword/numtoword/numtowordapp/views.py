from audioop import reverse

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from num2words import num2words
from gtts import gTTS
import os
import pyttsx3
# Create your views here.



def fn_index(request):
    return render(request,'index.html')
def fn_convert(request):
    if request.method == 'POST':
        Number = request.POST.get('txtNumber')
        word = num2words(Number)
        return render(request,'index.html',{'num':word})

def fn_play(request):
    text1=request.GET.get('txtWord')
    print(text1)
    text=pyttsx3.init()
    text.say(text1)
    text.runAndWait()
    return redirect('/')
    # text=gTTS(text=text1,lang=language, slow=False)
    # text.save("speech.mp3")
    # os.system('start speech.mp3')
