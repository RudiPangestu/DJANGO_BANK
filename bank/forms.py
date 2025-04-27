from django import forms
from .models import LoanApplication
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div

class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = LoanApplication
        fields = [
            'no_of_dependents',
            'education',
            'self_employed',
            'income_annum',
            'loan_amount',
            'loan_term',
            'cibil_score',
            'residential_assets_value',
            'commercial_assets_value',
            'luxury_assets_value',
            'bank_asset_value',
        ]
        labels = {
            'no_of_dependents': 'Number of Dependents',
            'education': 'Education',
            'self_employed': 'Are you Self-employed?',
            'income_annum': 'Annual Income ($)',
            'loan_amount': 'Loan Amount ($)',
            'loan_term': 'Loan Term (Years)',
            'cibil_score': 'CIBIL Score (300-900)',
            'residential_assets_value': 'Value of Residential Assets ($)',
            'commercial_assets_value': 'Value of Commercial Assets ($)',
            'luxury_assets_value': 'Value of Luxury Assets ($)',
            'bank_asset_value': 'Value of Bank Assets ($)',
        }
        widgets = {
            'no_of_dependents': forms.NumberInput(attrs={'class': 'form-control'}),
            'education': forms.Select(attrs={'class': 'form-control'}),
            'self_employed': forms.Select(attrs={'class': 'form-control'}),
            'income_annum': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'loan_amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'loan_term': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '30'}),
            'cibil_score': forms.NumberInput(attrs={'class': 'form-control', 'min': '300', 'max': '900'}),
            'residential_assets_value': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'commercial_assets_value': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'luxury_assets_value': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'bank_asset_value': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('no_of_dependents', css_class='form-group col-md-6'),
                Column('education', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('self_employed', css_class='form-group col-md-6'),
                Column('income_annum', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('loan_amount', css_class='form-group col-md-6'),
                Column('loan_term', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('cibil_score', css_class='form-group col-md-12'),
                css_class='form-row'
            ),
            Div(
                Div('Asset Information', css_class='card-header'),
                Div(
                    Row(
                        Column('residential_assets_value', css_class='form-group col-md-6'),
                        Column('commercial_assets_value', css_class='form-group col-md-6'),
                        css_class='form-row'
                    ),
                    Row(
                        Column('luxury_assets_value', css_class='form-group col-md-6'),
                        Column('bank_asset_value', css_class='form-group col-md-6'),
                        css_class='form-row'
                    ),
                    css_class='card-body'
                ),
                css_class='card mb-4'
            ),
            Submit('submit', 'Submit Application', css_class='btn btn-primary btn-lg')
        )