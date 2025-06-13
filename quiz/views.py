from django.shortcuts import render
from .utils import fetch_countries_from_api
import random

def quiz_view(request):

    if "used_countries" not in request.session:
        request.session["used_countries"] = []
    if "countries" not in request.session:
        api_data = fetch_countries_from_api()
        if "error" in api_data:
            return render(request, "quiz/index.html", {"error": api_data["error"]})
        request.session["countries"] = api_data

    used = request.session["used_countries"]
    countries = request.session["countries"]
    remaining = [c for c in countries if c["name"] not in used]

    if not remaining:
        request.session["used_countries"] = []
        remaining = countries

    country = random.choice(remaining)
    request.session["current_country"] = country["name"]
    request.session["current_capital"] = country["capital"]

    return render(request, "quiz/index.html", {
        "country": country["name"]
    })

def check_answer(request):
    if request.method == "POST":
        user_answer = request.POST.get("answer", "").strip().lower()
        correct_capital = request.session.get("current_capital", "").strip().lower()
        country = request.session.get("current_country", "")

        is_correct = user_answer == correct_capital

        if country and country not in request.session["used_countries"]:
            request.session["used_countries"].append(country)

        return render(request, "quiz/index.html", {
            "country": country,
            "user_answer": user_answer,
            "correct_capital": correct_capital,
            "is_correct": is_correct
        })
    return render(request, "quiz/index.html", {"error": "Invalid request"})
