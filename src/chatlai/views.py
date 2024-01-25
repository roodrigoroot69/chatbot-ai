from rest_framework.views import APIView

TOKEN = ""

class ChatBotWebHookAPIView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        try:
            token = request.data.get('hub.verify_token')
            challenge = request.data.get('hub.challenge')

            if token == TOKEN and challenge != None:
                return challenge
            else:
                return 'token incorrecto', 403
        except Exception as e:
            return e, 403


