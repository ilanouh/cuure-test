from rest_framework import serializers

from core.models import Note, Patient


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('id', 'description', 'patient', 'nutritionist', 'date')
        read_only_fields = ('nutritionist',)

    def create(self, validated_data):
        return Note.objects.create(nutritionist=self.context.get('request').user, **validated_data)


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = ('id', 'first_name', 'last_name', 'email', 'notes')
        depth = 1

    def create(self, validated_data):
        user = self.context.get('request').user
        return user.patients.create(**validated_data)
