from tortoise import fields, models

from src.domain.information.model import Information


class InformationModelMapper(models.Model):
    id = fields.IntField(pk=True)
    family_background_note = fields.CharField(max_length=150)
    expectation_note = fields.CharField(max_length=150)
    wears_coat = fields.BooleanField(default=False)
    wears_hijab = fields.BooleanField(default=True)
    willingness_to_relocate = fields.CharField(max_length=50)
    preferred_living_arrangement = fields.CharField(max_length=50)
    health_note = fields.CharField(max_length=50)

    def cast(self):
        Information(
            id=self.id,
            family_background_note=self.family_background_note,
            expectation_note=self.expectation_note,
            wears_coat=self.wears_coat,
            wears_hijab=self.wears_hijab,
            willingness_to_relocate=self.wears_hijab,
            preferred_living_arrangement=self.willingness_to_relocate,
            health_note=self.health_note,
        )
