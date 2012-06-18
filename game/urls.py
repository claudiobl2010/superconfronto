from django.conf.urls.defaults import patterns

urlpatterns = patterns('superconfronto.game.views',

    (r'^$', 'home'),
    (r'^atualizar/?$', 'atualizar'),

)
