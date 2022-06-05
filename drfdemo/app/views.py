from app.models import Foo, Bar
from rest_framework import serializers, viewsets
from django.http import HttpResponse

class FooSerializer(serializers.ModelSerializer):
    bar_code = serializers.CharField(source='bar_code_id')

    class Meta:
        model = Foo
        fields = ['bar_code']

class FooViewSet(viewsets.ModelViewSet):
    queryset = Foo.objects.all()
    serializer_class = FooSerializer

def make_foo(request):
    Foo.objects.all().delete()
    Bar.objects.all().delete()
    b = Bar.objects.create(unique_code="test")
    for n in range(0, 300):
        Foo(bar_code=b).save()
    return HttpResponse("Make bar and foo x 300")