from django.core.mail import EmailMessage
msg = EmailMessage(to=["foo@bar"])
msg.template_name = "test-email"  # slug from Mandrill
msg.global_merge_vars = {
    'foo': "bar",
    'url': "tivix.com"
}
msg.use_template_subject = True
msg.use_template_from = True
msg.send()