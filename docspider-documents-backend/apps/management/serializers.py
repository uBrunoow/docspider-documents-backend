from .models import Documents
from rest_framework import serializers
import six
import uuid
import base64
import imghdr
from rest_framework import serializers
from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError

class Base64FileField(serializers.FileField):
    ALLOWED_EXTENSIONS = ["jpeg", "jpg", "png", "gif", "pdf"]
    MAX_FILE_SIZE_MB = 5

    def to_internal_value(self, data):
        if isinstance(data, six.string_types):
            if "data:" in data and ";base64," in data:
                header, data = data.split(";base64,")

            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                raise ValidationError("Arquivo inválido")

            file_name = str(uuid.uuid4())[:12]
            file_extension = self.get_file_extension(file_name, decoded_file)

            if file_extension not in self.ALLOWED_EXTENSIONS:
                raise ValidationError("Extensão de arquivo não permitida")

            complete_file_name = "%s.%s" % (file_name, file_extension)

            if len(decoded_file) > self.MAX_FILE_SIZE_MB * 1024 * 1024:
                raise ValidationError(
                    "O arquivo excede o tamanho máximo permitido")

            return ContentFile(decoded_file, name=complete_file_name)

        raise ValidationError("Arquivo inválido")

    def get_file_extension(self, file_name, decoded_file):
        extension = imghdr.what(file_name, decoded_file)
        if extension is None:
            if decoded_file[:4] == b'%PDF':
                return "pdf"
            raise ValidationError("Arquivo não é uma imagem válida ou PDF")
        return extension


class DocumentsSerializer(serializers.ModelSerializer):
  document = Base64FileField()
  
  class Meta:
    model = Documents
    fields = "__all__"
    
class DocumentsFlatSerializer(serializers.ModelSerializer):
  class Meta:
    model = Documents
    fields = ["id", "title"]