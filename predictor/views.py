from django.shortcuts import render, redirect

# Create your views here.
from .forms import ChurnForm
from Machine_Learning.preprocess_input import preprocess_input
import joblib

rf_model = joblib.load("Machine_Learning/churn_random_forest.pkl")
xgb_model = joblib.load("Machine_Learning/churn_xgboost_model.pkl")

rf_features = joblib.load("Machine_Learning/feature_columns_rf.pkl")
xgb_features = joblib.load("Machine_Learning/feature_columns_xgb.pkl")

rf_threshold = joblib.load("Machine_Learning/churn_threshold_rf.pkl")
xgb_threshold = joblib.load("Machine_Learning/churn_threshold_xgb.pkl")

MODEL_THRESHOLDS = {'rf': rf_threshold, 'xgb': xgb_threshold}
MODEL_FEATURES = {'rf': rf_features, 'xgb': xgb_features}
MODEL_OBJECTS = {'rf': rf_model, 'xgb': xgb_model}

def input_view(request):
    if request.method == "POST":
        form = ChurnForm(request.POST)
        if form.is_valid():
           
            request.session['form_data'] = form.cleaned_data
            return redirect('output')  
    else:
        form = ChurnForm()

    return render(request, "input.html", {"form": form})

def output_view(request):
    form_data = request.session.get('form_data', None)
    if not form_data:
        return redirect('input') 

    selected_model = form_data.pop('selected_model').lower().strip()

    if selected_model not in MODEL_OBJECTS:
        return render(request, "output.html", {"error": "Invalid model selected."})

    model = MODEL_OBJECTS[selected_model]
    features = MODEL_FEATURES[selected_model]
    threshold = MODEL_THRESHOLDS[selected_model]

    df = preprocess_input(form_data,selected_model)

    prob = model.predict_proba(df)[:,1][0]

    pred = int(prob > threshold)

    probability = round(prob, 2)

    return render(request, "output.html", {
        "prediction": pred,
        "probability": probability,
        "model": selected_model.upper()
    })


