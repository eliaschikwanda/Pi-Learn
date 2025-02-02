from django.contrib import admin
from .models import *

# Register your models here.

    
admin.site.register([
    Year,
    ExamBoard,
    Session,
    Subject,
    Paper, BoardSubTopic,
    QuestionAnswer,
    FullQuestionAnswer,
    ReportThreshPrep,
    PossibleLetters,
    PossibleQuestionNumber,
    PaperOneAnswers,
    website_pics,
    home_image,
    people_image,
    UserProgressRecord,
    ContactUsInfo,
    BlogPost,
])

