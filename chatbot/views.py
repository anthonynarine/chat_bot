
from decouple import config
SECRET_KEY = config('SECRET_KEY')

import openai
from rest_framework.views import APIView
from rest_framework.response import Response

class ChatbotView(APIView):
    def post(self, request):
        user_input = request.data.get('message')
        
        # Call OpenAI API to generate chatbot response
        openai.api_key = SECRET_KEY  
        response = openai.Completion.create(
            engine="davinci",
            prompt=user_input,
            max_tokens=50  
        )
        
        chatbot_response = response.choices[0].text.strip()
        return Response({'message': chatbot_response})
