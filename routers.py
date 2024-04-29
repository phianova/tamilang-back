from rest_framework import routers

from tamilangLetters.viewsets import LetterViewSet, UserLearningViewSet

router = routers.SimpleRouter()

router.register(r'letter', LetterViewSet, basename="letter")
router.register(r'userlearning', UserLearningViewSet, basename="userlearning")

urlpatterns = router.urls