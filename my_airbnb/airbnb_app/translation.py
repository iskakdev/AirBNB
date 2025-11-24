from .models import (Country, City, Rules, Property,
                     Review)
from modeltranslation.translator import TranslationOptions,register

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)


@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city_name',)


@register(Rules)
class RulesTranslationOptions(TranslationOptions):
    fields = ('rules',)


@register(Property)
class PropertyTranslationOptions(TranslationOptions):
    fields = ('property_name', 'description', 'address',
              'property_type')


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('comment',)