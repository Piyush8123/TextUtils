# I have created this file - Piyush
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
    # s =  "Home"'''<br> <h1>Hello Piyush</h1><br>
    #         Your course of Django is:-
    #     &nbsp&nbsp<a href = "https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">Django Course </a><br><br>
    #     Your courses in udemy are:-
    #     &nbsp&nbsp<a href = "https://www.udemy.com/home/my-courses/learning/">Udemy Learning</a><br><br>
    #     Your class link is :-
    #     &nbsp&nbsp<a href = "https://zoom.us/j/96884117597?pwd=bEtQU1NCMW1iT3ZBM1Z6OWl4M0xpZz09">Zoom Meeting</a><br><br>
    #     Your search engine:-
    #     &nbsp&nbsp<a href = "https://www.google.com/">Google</a>'''
    # return HttpResponse(s)


# def about(request):
#     return HttpResponse("About Piyush")

def analyze(request):
    #Get the Text
    djtext = request.POST.get('text','default')

    #Check the checkbox values
    removepunc = request.POST.get('removepunc','off')
    capital = request.POST.get('capital','off')
    line = request.POST.get('line','off')
    space = request.POST.get('space','off')
    count = request.POST.get('count', 'off')

    #Checking which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        a = ""
        for char in djtext:
            if char not in punctuations:
                a = a + char
        t = {'purpose': 'Removed Punctuations','analyzed_text': a}
        djtext = a

        #Analyzing the text
        # return render(request,'analyze.html',t)
    if (capital == "on"):
            a = ""
            for char in djtext:
                a = a + char.upper()
            t = {'purpose': 'Changed to UpperCase', 'analyzed_text': a}
            djtext = a
            # return render(request, 'analyze.html', t)

    if(line == "on"):
            a = ""
            for char in djtext:
                  if char != "\n" and char != "\r":
                    a = a + char
            t = {'purpose': 'New Line Remover', 'analyzed_text': a}
            # return render(request, 'analyze.html', t)
            djtext = a
    if(space == "on"):
            a = ""
            for char in djtext:
                char = char.replace(" ","")
                a = a + char

            t = {'purpose': 'Space Remover', 'analyzed_text': a}
            djtext = a
            # return render(request, 'analyze.html', t)
    if(count == "on"):
        a = ""
        a = len(djtext)
        t = {'purpose': 'Count of Charater', 'analyzed_text': a}
        djtext = a
        # return render(request, 'analyze.html', t)

    if(removepunc!="on" and capital!="on" and line!="on" and space!="on" and count!="on"):
        return HttpResponse("You haven't select anything.")

    return render(request, 'analyze.html', t)


# def capital(request):
#     return HttpResponse("Capital First &nbsp&nbsp&nbsp<a href = '/'> back </a>")
#
# def remover(request):
#     return HttpResponse("New Line Remover &nbsp&nbsp&nbsp<a href = '/'> back </a>")
#
# def spaceremove(request):
#     return HttpResponse("Space Remover &nbsp&nbsp&nbsp<a href = '/'> back </a>")
#
# def count(request):
#     return HttpResponse("Count of character &nbsp&nbsp&nbsp<a href = '/'> back </a>")