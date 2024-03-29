from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Your Account has been created! you are Now able to Login')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})


@login_required
def profile(request):
    if request.method=="POST":
            u_form = UserUpdateForm(request.POST, instance=request.user)
            pr_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

            if u_form.is_valid() and pr_form.is_valid():
                 u_form.save()
                 pr_form.save()
                 messages.success(request, f'Your Account has been Updated!')
                 return redirect('profile')


    else:
            u_form = UserUpdateForm(instance=request.user)
            pr_form = ProfileUpdateForm(instance=request.user.profile)





    context={
    'u_form': u_form,
    'pr_form': pr_form
    }
    return render(request,'users/profile.html',context)







#
# messages.info
# messages.debug
# messages.success
# messages.warning
# messages.error
