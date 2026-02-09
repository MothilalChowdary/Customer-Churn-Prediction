from django import forms

class ChurnForm(forms.Form):
    gender = forms.ChoiceField(
        choices=[('Male', 'Male'), ('Female', 'Female')],
        widget=forms.RadioSelect
    )
    SeniorCitizen = forms.ChoiceField(
        choices=[(0,'No'), (1,'Yes')], 
        widget=forms.RadioSelect
        )
    Partner = forms.ChoiceField(
        choices=[('Yes','Yes'), ('No','No')],
        widget=forms.RadioSelect
    )
    Dependents = forms.ChoiceField(
        choices=[('Yes','Yes'), ('No','No')],
        widget=forms.RadioSelect
    )
    tenure = forms.IntegerField(
        min_value=0, 
        label="Tenure (months)"
        )
    PhoneService = forms.ChoiceField(
        choices=[('Yes','Yes'), ('No','No')],
        widget=forms.RadioSelect
    )
    MultipleLines = forms.ChoiceField(
        choices=[('Yes','Yes'), ('No','No'), ('No phone service','No phone service')],
        widget=forms.RadioSelect
    )
    InternetService = forms.ChoiceField(
        choices=[('DSL','DSL'), ('Fiber optic','Fiber optic'), ('No','No')],
        widget=forms.Select
    )
    OnlineSecurity = forms.ChoiceField(
        choices=[('Yes','Yes'), ('No','No'), ('No internet service','No internet service')],
        widget=forms.RadioSelect
    )
    OnlineBackup = forms.ChoiceField(
        choices=[('Yes','Yes'), ('No','No'), ('No internet service','No internet service')],
        widget=forms.RadioSelect
    )
    DeviceProtection = forms.ChoiceField(
        choices=[('Yes','Yes'), ('No','No'), ('No internet service','No internet service')],
        widget=forms.RadioSelect
    )
    TechSupport = forms.ChoiceField(
        choices=[('Yes','Yes'), ('No','No'), ('No internet service','No internet service')],
        widget=forms.RadioSelect
    )
    StreamingTV = forms.ChoiceField(
        choices=[('Yes','Yes'), ('No','No'), ('No internet service','No internet service')],
        widget=forms.RadioSelect
    )
    StreamingMovies = forms.ChoiceField(
        choices=[('Yes','Yes'), ('No','No'), ('No internet service','No internet service')],
        widget=forms.RadioSelect
    )
    Contract = forms.ChoiceField(
        choices=[('Month-to-month','Month-to-month'), ('One year','One year'), ('Two year','Two year')],
        widget=forms.Select
    )
    PaperlessBilling = forms.ChoiceField(
        choices=[('Yes','Yes'), ('No','No')],
        widget=forms.RadioSelect
    )

    PaymentMethod = forms.ChoiceField(
        choices=[
            ('Electronic check','Electronic check'),
            ('Mailed check','Mailed check'),
            ('Bank transfer (automatic)','Bank transfer (automatic)'),
            ('Credit card (automatic)','Credit card (automatic)')
        ],
        widget=forms.Select
    )
    MonthlyCharges = forms.FloatField(
        min_value=0, 
        label="Monthly Charges"
        )

    MODEL_CHOICES = [
        ('rf', 'Random Forest'),
        ('xgb', 'XGBoost')
    ]
    selected_model = forms.ChoiceField(
        choices=MODEL_CHOICES,
        label="Select Model",
        widget=forms.Select
    )
