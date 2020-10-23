from django.shortcuts import render,redirect
from .forms import CreatePollForm
from .models import Poll
def home (request):
    polls=Poll.objects.all()
    context={'polls':polls}
    return render(request,'poll/home.html',context)

def create (request):
    if request.method =='POST':
        form=CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=CreatePollForm()
    context={'form':form}
    return render(request,'poll/create.html',context)

def vote (request,poll_id):
    poll=Poll.objects.get(pk=poll_id)
    if request.method =='POST':
        print(request.POST['pooll'])
        if request.POST['pooll']=='option1':
            poll.option1_count +=1
        elif request.POST['pooll'] =='option2':
            poll.option2_count +=1
        elif request.POST['pooll'] =='option3':
            poll.option3_count +=1
        poll.save()
        return redirect('results',poll_id)
    context={'poll':poll}
    return render(request,'poll/vote.html',context)

def results (request,poll_id):
    poll=Poll.objects.get(pk=poll_id)
    context={'poll':poll}
    return render(request,'poll/results.html',context)
