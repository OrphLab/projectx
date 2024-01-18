from django.db import models
import pycountry
from talent.models import Talent


#Create your models here.

COUNTRY_CHOICES = [(country.alpha_2, country.name) for country in pycountry.countries]

class Country(models.Model):
    country_code = models.CharField(max_length=2, choices=COUNTRY_CHOICES)

    def __str__(self):
        return self.country_code
  
   
class Industries(models.TextChoices):
    AGR = 'AGR', 'Agriculture and Agribusiness' 
    MAN = 'MAN', 'Manufacturing'
    IT = 'IT', 'Technology and Information Technology (IT)'
    HEA = 'HEA', 'Healthcare and Pharmaceuticals'
    FIN = 'FIN', 'Finance and Banking'
    AOU = 'AOU', 'Accounting and Auditing'
    ENE = 'ENE', 'Energy and Utilities'
    CON = 'CON', 'Construction and Real Estate'
    TRA = 'TRA', 'Transportation and Logistics'
    RET = 'RET', 'Retail'
    HOS = 'HOS', 'Hospitality and Tourism'
    TEL = 'TEL', 'Telecommunications'
    EDU = 'EDU', 'Education'
    ENT = 'ENT', 'Entertainment and Media'
    AUT = 'AUT', 'Automotive'
    DEF = 'DEF', 'Defense and Aerospace'
    ENV = 'ENV', 'Environmental Services'
    LEG = 'LEG', 'Legal Services'
    CON_SERV = 'CON_SERV', 'Consulting Services'
    NON = 'NON', 'Nonprofit and Social Services'
    MIN = 'MIN', 'Mining and Extractive Industries'

class BusinessOperations(models.TextChoices):
    OPS = 'OPS', 'Operations and Production'
    SALES = 'SALES', 'Sales'
    MARKETING = 'MARKETING', 'Marketing'
    FINANCE = 'FINANCE', 'Finance and Accounting'
    HR = 'HR', 'Human Resources'
    IT = 'IT', 'Information Technology'
    CUSTOMER_SERVICE = 'CUSTOMER_SERVICE', 'Customer Service'
    SUPPLY_CHAIN = 'SUPPLY_CHAIN', 'Supply Chain and Logistics'
    R_AND_D = 'R_AND_D', 'Research and Development'
    LEGAL = 'LEGAL', 'Legal and Compliance'
    QUALITY_ASSURANCE = 'QUALITY_ASSURANCE', 'Quality Assurance and Control'
    ADMINISTRATION = 'ADMINISTRATION', 'Administration and Support Services'
    STRATEGIC_PLANNING = 'STRATEGIC_PLANNING', 'Strategic Planning and Business Development'
    CORPORATE_COMMUNICATIONS = 'CORPORATE_COMMUNICATIONS', 'Corporate Communications'
    PROJECT_MANAGEMENT = 'PROJECT_MANAGEMENT', 'Project Management'
    RISK_MANAGEMENT = 'RISK_MANAGEMENT', 'Risk Management'

class Skill(models.Model):
    id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f"{self.name}"

class UserSkill(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE) 
    talentcard = models.ForeignKey('TalentCard', on_delete=models.CASCADE)
    skill_level = models.IntegerField( default=1, choices=[(i,i) for i in range(1,6)])
    skill_years = models.IntegerField(default=5, choices=[(i,i) for i in range(3,10)])
    
    def __str__(self):
        return f"{self.talentcard}"

class TalentCard(models.Model):
    talent = models.OneToOneField(Talent, on_delete=models.CASCADE, null=False, blank=False)
    industry = models.CharField(max_length=8, choices=Industries.choices, default=Industries.IT)
    operations = models.CharField(max_length=24, choices=BusinessOperations.choices)    
    origin_country = models.CharField(max_length=4, choices=COUNTRY_CHOICES, default='US')  
    relocation_countries = models.ManyToManyField(Country, default=Country.objects.filter(country_code__in=['US', 'CA']))
    open_to_relocation = models.BooleanField(default=False)
    expertice = models.CharField(max_length=24, choices=BusinessOperations.choices, default=BusinessOperations.OPS)  
    skills = models.ManyToManyField(Skill, through=UserSkill)
    linkedin = models.URLField(max_length=200, blank=True)
    github = models.URLField(max_length=200, blank=True)
    personal_website = models.URLField(max_length=200, blank=True)
    summary = models.TextField(max_length=500, blank=True)
    
    def __str__(self) -> str:
        return f'{self.talent}-talentcard'

