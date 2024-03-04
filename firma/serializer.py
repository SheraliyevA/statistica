from rest_framework import serializers
from .models import Xodim


class XodimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xodim
        fields = ('id', 'first_name', 'last_name', 'phone', 'ish_turi', 'id_raqam', 'gender', 'bulim')
        read_only_fields = ('created', 'updated')
