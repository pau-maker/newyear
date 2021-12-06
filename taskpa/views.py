from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

def greets(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request,"add/index.html",{
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        formss = newtaskform(request.POST)

        # Check if form data is valid (server-side)
        if formss.is_valid():

            # Isolate the task from the 'cleaned' version of form data
            task = formss.cleaned_data["task"]

            # Add the new task to our list of tasks
            request.session["tasks"] += [task]

            # Redirect user to list of tasks
            return HttpResponseRedirect(reverse("adds:greet"))

        else:

            # If the form is invalid, re-render the page with existing information.
            return render(request, "add/add.html", {
                "form": formss
            })
    return render(request,"add/add.html",{
    "form":newtaskform()
    })

class newtaskform(forms.Form):
    task = forms.CharField(label="New Task")
