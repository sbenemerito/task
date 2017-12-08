# task

Customizing Django admin's ManyToManyFields

### How it works:

Considering the following models:
  - **ModelA** (name \<CharField\>)
  - **ModelB** (name \<CharField\>, related_a \<ForeignKey\>)
  - **ModelC** (name \<CharField\>, related_a \<ForeignKey\>)
  - **MainModel** (name \<CharField\>, model_a \<ManyToManyField\>, model_b \<ManyToManyField\>, model_c \<ManyToManyField\>)

For **MainModel**, choices for *model_a* must be limited to those related with selected instances of *model_b* and *model_c*.

When you open the admin page for **MainModel**, selecting items for model_b and model_c will automatically show allowed choices for model_a.

Read more:
  - Django Admin: https://docs.djangoproject.com/en/1.11/ref/contrib/admin/
  - Overriding CSS and JS in Django Admin: https://docs.djangoproject.com/en/1.11/topics/forms/media/
  - Javascript customization: https://docs.djangoproject.com/en/1.11/ref/contrib/admin/javascript/
  - Admin widgets: https://github.com/django/django/blob/master/django/contrib/admin/widgets.py
