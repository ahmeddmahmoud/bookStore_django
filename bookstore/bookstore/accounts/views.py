from django.shortcuts import render, redirect, reverse

# Create your views here.


def profile_view(request):
    url = reverse("homedatabase")
    return redirect(url)


# def create_user(request):
#     form = RegisterationForm()
#     if request.method == 'POST':
#         form= RegisterationForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             login_url = reverse("login")
#             return redirect(login_url)

#     return render(request, 'accounts/register.html', {'form':form})