from django.db import models
import uuid
from django.utils import timezone

class LoanApplication(models.Model):
    EDUCATION_CHOICES = (
        ('graduate', 'Graduate'),
        ('not_graduate', 'Not Graduate'),
    )
    
    EMPLOYMENT_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    
    application_id = models.CharField(max_length=20, unique=True, editable=False)
    no_of_dependents = models.IntegerField()
    education = models.CharField(max_length=20, choices=EDUCATION_CHOICES)
    self_employed = models.CharField(max_length=5, choices=EMPLOYMENT_CHOICES)
    income_annum = models.DecimalField(max_digits=12, decimal_places=2)
    loan_amount = models.DecimalField(max_digits=12, decimal_places=2)
    loan_term = models.IntegerField(help_text="Term in years")
    cibil_score = models.IntegerField()
    residential_assets_value = models.DecimalField(max_digits=12, decimal_places=2)
    commercial_assets_value = models.DecimalField(max_digits=12, decimal_places=2)
    luxury_assets_value = models.DecimalField(max_digits=12, decimal_places=2)
    bank_asset_value = models.DecimalField(max_digits=12, decimal_places=2)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    def save(self, *args, **kwargs):
        if not self.application_id:
            # Generate application ID (SB + random numbers)
            self.application_id = f"SB{uuid.uuid4().hex[:6].upper()}"
            
            # Determine loan approval
            self.determine_approval()
            
        super().save(*args, **kwargs)
    
    def determine_approval(self):
        """
        Simple loan approval logic based on the provided parameters.
        This is a simplified version - in a real system this would be more complex.
        """
        # Calculate total assets
        total_assets = (
            self.residential_assets_value + 
            self.commercial_assets_value + 
            self.luxury_assets_value + 
            self.bank_asset_value
        )
        
        # Asset to loan ratio
        asset_to_loan_ratio = total_assets / self.loan_amount if self.loan_amount > 0 else 0
        
        # Income to loan ratio (annual)
        income_to_loan_ratio = self.income_annum / self.loan_amount if self.loan_amount > 0 else 0
        
        # Calculate a score
        score = 0
        
        # CIBIL score factor
        if self.cibil_score >= 750:
            score += 30
        elif self.cibil_score >= 700:
            score += 25
        elif self.cibil_score >= 650:
            score += 15
        elif self.cibil_score >= 600:
            score += 10
        
        # Asset coverage
        if asset_to_loan_ratio >= 2:
            score += 25
        elif asset_to_loan_ratio >= 1.5:
            score += 20
        elif asset_to_loan_ratio >= 1:
            score += 15
        elif asset_to_loan_ratio >= 0.5:
            score += 5
        
        # Income factor
        if income_to_loan_ratio >= 0.5:  # Can repay loan in 2 years of full income
            score += 25
        elif income_to_loan_ratio >= 0.3:
            score += 20
        elif income_to_loan_ratio >= 0.2:
            score += 15
        elif income_to_loan_ratio >= 0.1:
            score += 10
        
        # Dependents factor
        if self.no_of_dependents <= 1:
            score += 10
        elif self.no_of_dependents <= 3:
            score += 5
        
        # Education factor
        if self.education == 'graduate':
            score += 5
        
        # Self-employment factor
        if self.self_employed == 'yes':
            score += 5
        
        # Approve if score is high enough
        self.is_approved = score >= 60
        
        return self.is_approved
    
    def total_assets(self):
        return (
            self.residential_assets_value + 
            self.commercial_assets_value + 
            self.luxury_assets_value + 
            self.bank_asset_value
        )
    
    def __str__(self):
        return f"Loan Application {self.application_id}"