from .base import BaseModel
from django.db import models

class Country(BaseModel):
    name = models.CharField(
        max_length=255, unique=True, db_index=True, help_text=("Country Name")
    )
    code = models.CharField(
        max_length=3, unique=True, db_index=True, help_text=("Country Code")
    )


    class Meta:
        db_table = "countries"
        ordering = ["name"]
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name

class State(BaseModel):
    name = models.CharField(
        max_length=255, unique=True, db_index=True, help_text=("State Name")
    )
    code = models.CharField(
        max_length=3, unique=True, db_index=True, help_text=("State Code")
    )
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=False, blank=False
    )

    class Meta:
        db_table = "states"
        ordering = ["name"]
        verbose_name_plural = "States"
    def __str__(self):
        return self.name

class Zone(BaseModel):
    name = models.CharField(
        max_length=255, unique=True, db_index=True, help_text=("Zone Name")
    )
    code = models.CharField(
        max_length=3, unique=True, db_index=True, help_text=("Zone Code")
    )
    state = models.ForeignKey(
        State, on_delete=models.CASCADE, null=False, blank=False
    )

    def save(self, *args, **kwargs):  ##before insert process data
        # self.name = "test nm1"
        super().save(*args, **kwargs)

    class Meta:
        db_table = "zones"
        ordering = ["name"]
        verbose_name_plural = "Zones"

    @property
    def egtext(self):  ##getter with customization
        return "test"
    def __str__(self):
        return self.name
