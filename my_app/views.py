from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from .forms import SignUpForm
from django.contrib.auth import login, authenticate

class SignUpView(FormView):
	form_class = SignUpForm
	success_url = '/thanks/'
	template_name = 'my_app/signup.html'

	def form_valid(self, form):
		user = form.save()
		user.is_active = False
		user.save()
		username = form.cleaned_data['username']
		password = form.cleaned_data['password1']
		current_site = get_current_site(request)
		mail_subject = 'Activate your blog account.'
		message = render_to_string('confirmation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activation_token.make_token(user),
        })
		to_email = form.cleaned_data['email']
		email = EmailMessage(
                        mail_subject, message, to=[to_email]
        )
		email.send()
		user = authenticate(username=username, password=password)
		login(self.request, user)

		return super(SignUpView, self).form_valid(form)

class HomeView(TemplateView):

	def get(self, request):
		return render(request, self.template_name)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')