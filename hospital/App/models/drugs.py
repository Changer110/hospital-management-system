from django.db import models


class Drugs(models.Model):
    DRUG_TYPES = (
        ('Tablet', 'Tablet'),
        ('Capsule', 'Capsule'),
        ('Liquid', 'Liquid'),
        ('Injection', 'Injection'),
        ('Cream', 'Cream'),
        ('Spray', 'Spray'),
    )

    name = models.CharField(max_length=100, unique=True)
    drug_type = models.CharField(max_length=20, choices=DRUG_TYPES,default='Tablet')
    quantity = models.PositiveIntegerField()
    expiry_date = models.DateField()
    dosage_issued = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_drug = models.DecimalField(max_digits=10, decimal_places=2)
    imported_from = models.CharField(max_length=100)

    def __str__(self):
        return self.name
