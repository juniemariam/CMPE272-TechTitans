from django.db import models

from datetime import date

# Create the Task class to describe the model.
class CarList(models.Model):
    """Stores a task."""                                                
    car_tile = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    # Date the car details was uploaded was created.
    created_on = models.DateField(default=date.today)

    # Meta data about the database table.
    class Meta:
        # Set the table name.
        db_table = 'car_list'

        # Set default ordering
        ordering = ['id']                                                                                                                                                                                                                           # Define what to output when the model is printed as a string.
    def __str__(self):
        return self.car_title

