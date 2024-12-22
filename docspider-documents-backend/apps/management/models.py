from django.db import models
from django_prometheus.models import ExportModelOperationsMixin
from utils.models import BaseModel

class Documents(ExportModelOperationsMixin("documents"), BaseModel):
  title = models.CharField(
    max_length=100,
    unique=True,
    verbose_name="Título do Documento",
    help_text="Título do Documento com até 100 caractéres" 
  )
  description = models.TextField(
    max_length=2000,
    blank=True,
    null=True,
    verbose_name="Descrição do documento",
    help_text="Descrição do documento não obrigatória",
  )
  document = models.FileField(
    verbose_name="Documento",
    help_text="Proibido o upload de arquivos dos tipos: .exe, .zip e .bat"
  )
  filename = models.CharField(
    max_length=100,
    verbose_name="Nome do arquivo",
    help_text="Nome do arquivo com até 100 caractéres",
    default="",
  )
  is_active = models.BooleanField(
    verbose_name="Ativo",
    help_text="Ativo",
    default=False,
  )
  
  def __str__(self):
      return f"Documento | {self.title}"
  
  class Meta:
      verbose_name = "Documento"
      verbose_name_plural = "Documentos"