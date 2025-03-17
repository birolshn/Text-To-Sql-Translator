import os
import torch
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import render

# Modeli yükle
MODEL_PATH = os.path.join(os.path.dirname(__file__), "sql-translator-model")
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = TFAutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)

@api_view(["GET","POST"])
def translate(request):
    if request.method == "GET":
        return JsonResponse({"message": "Use POST request with 'question' and 'context' fields"}, status=400)
    
    """Kullanıcının doğal dilde yazdığı sorguyu SQL'e çevirir"""
    data = request.data
    question = data.get("question", "")
    context = data.get("context", "")

    if not question or not context:
        return JsonResponse({"error": "Lütfen soru ve şema bilgilerini girin"}, status=400)

    input_text = f"translate English to SQL: Schema: {context} Question: {question}"
    inputs = tokenizer(input_text, return_tensors="tf")

    outputs = model.generate(
        inputs["input_ids"],
        max_length=128,
        num_beams=4,
        early_stopping=True
    )

    generated_sql = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return JsonResponse({"sql_query": generated_sql})

def index(request):
    return render(request, "index.html")