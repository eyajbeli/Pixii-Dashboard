from django.db import models

class JobCategory(models.Model):
    """
    Model for job categories.

    This model represents the different categories of job offers.

    Attributes:
        category_name (str): The name of the job category.

    Methods:
        __str__(): Returns a string representation of the job category.

    Example Usage:
    ```
    category = JobCategory.objects.create(category_name='IT')
    ```

    Note: Each job category should have a unique name.
    """
    category_name=models.CharField(max_length=255,unique=True) 
    
    def __str__(self):
        
        return self.category_name
  
  
class JobContract(models.Model):
    """
    Model for job contracts.

    This model represents the different types of job contracts.

    Attributes:
        contract_type (str): The type of the job contract.

    Example Usage:
    ```
    contract = JobContract.objects.create(contract_type='Full-Time')
    ```

    Note: Each job contract type should have a unique name.
    """
    contract_type = models.CharField(max_length=255,unique=True) 
   
    
class JobOffer(models.Model):
    """
    Model for job offers.

    This model represents individual job offers.

    Attributes:
        title (str): The title of the job offer.
        details (str): Additional details about the job offer.
        category (ForeignKey): The category of the job offer (linked to JobCategory).
        contract_type (ForeignKey): The type of the job contract (linked to JobContract).

    Methods:
        __str__(): Returns a string representation of the job offer.

    Example Usage:
    ```
    offer = JobOffer.objects.create(title='Software Engineer', details='Join our IT team', category=category, contract_type=contract)
    ```

    Note: Each job offer is associated with a specific category and contract type.
    """
    title=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
    category=models.ForeignKey(JobCategory, on_delete=models.CASCADE,to_field='category_name') #to_field='category_name'
    contract_type=models.ForeignKey(JobContract, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
  