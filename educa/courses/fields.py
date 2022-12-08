from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class OrderField(models.PositiveIntegerField):
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is None:
            value = self.get_next_order_value(model_instance)
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)

    def get_next_order_value(self, model_instance):
        query_set = self.model.objects.all()
        try:
            if self.for_fields:
                query = {
                    field: getattr(model_instance, field)
                    for field in self.for_fields
                }
                query_set = query_set.filter(**query)
                last_item = query_set.latest(self.attname)
                return last_item.order + 1
        except ObjectDoesNotExist:
            return 0
