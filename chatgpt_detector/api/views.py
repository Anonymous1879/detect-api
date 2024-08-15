# import requests
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class GPTDetectorView(APIView):
#     def post(self, request):
#         text = request.data.get('text')
#         if not text:
#             return Response({"error": "No text provided"}, status=status.HTTP_400_BAD_REQUEST)

#         # Hugging Face model API endpoint
#         url = "https://api-inference.huggingface.co/models/Hello-SimpleAI/chatgpt-detector-roberta"
#         headers = {"Authorization": f"Bearer hf_...OPCw	"}  # Replace with your Hugging Face API Key

#         response = requests.post(url, headers=headers, json={"inputs": text})
#         if response.status_code != 200:
#             return Response({"error": "Failed to get a response from the model"}, status=response.status_code)

#         result = response.json()
#         return Response(result, status=status.HTTP_200_OK)

import requests
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class GPTDetectorView(APIView):
    def post(self, request):
        text = request.data.get('text')
        if not text:
            return Response({"error": "No text provided"}, status=status.HTTP_400_BAD_REQUEST)

        url = "https://api-inference.huggingface.co/models/Hello-SimpleAI/chatgpt-detector-roberta"
        headers = {
            "Authorization": f"Bearer Hugging Face API",  # Replace with your Hugging Face API key
            "Content-Type": "application/json"
        }

        payload = {"inputs": text}
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(result, status=status.HTTP_200_OK)
