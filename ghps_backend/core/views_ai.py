from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from core.models import AIQuestion
from core.serializers import AIQuestionSerializer
from django.conf import settings
import openai

class AskAIQuestionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AIQuestionSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.validated_data['question']

            try:
                openai.api_key = settings.OPENAI_API_KEY
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a poultry expert."},
                        {"role": "user", "content": question}
                    ]
                )

                answer = response['choices'][0]['message']['content']

                ai_question = AIQuestion.objects.create(
                    user=request.user,
                    question=question,
                    response=answer
                )

                return Response(AIQuestionSerializer(ai_question).data, status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
