from django.urls import path
from .views import SurveyPrivate, OptionPublic, OptionPrivate, survey_list

urlpatterns = [
     # lista todas as enquetes (GET) OU cria uma nova enquete (POST)
     path('survey/', SurveyPrivate.as_view(), {'pk': None}, name="survey-general"),
     # Mostra uma enquete específica (GET), modifica uma enquete (PUT), remove uma enquete (DELETE)
     path('survey/<int:pk>', SurveyPrivate.as_view(), name="survey-specific"),
     # faz um unico voto (POST)
     path('vote/', OptionPublic.as_view(), name="vote"),
     # Modifica uma opção (PUT)
     path('option/<int:pk>', OptionPrivate.as_view(), name="option-specific"),
     # Cria uma nova opção (POST)
     path('option/', OptionPrivate.as_view(), name="option-general"),
     # Template com as enquetes
     path('surveys/', survey_list)

]
