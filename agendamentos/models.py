from django.db import models
from django.core.validators import MinValueValidator

class modelo_pagamento(models.Model):
    data_pagamento = models.DateField()
    permite_recorrencia = models.BooleanField()
    quantidade_recorrencia = models.IntegerField(validators=[MinValueValidator(0)])
    intervalo_recorrencia = models.IntegerField(validators=[MinValueValidator(1)])
    status_recorrencia = models.CharField(max_length=50)
    agencia = models.IntegerField(validators=[MinValueValidator(1)])
    conta = models.IntegerField(validators=[MinValueValidator(1)])
    valor_pagamento = models.IntegerField(validators=[MinValueValidator(1)])

    def campos(self):
        return {
            'id': self.id,
            'data_pagamento': self.data_pagamento.isoformat(),
            'permite_recorrencia': self.permite_recorrencia,
            'quantidade_recorrencia': self.quantidade_recorrencia,
            'intervalo_recorrencia': self.intervalo_recorrencia,
            'status_recorrencia': self.status_recorrencia,
            'agencia': self.agencia,
            'conta': self.conta,
            'valor_pagamento': self.valor_pagamento,
        }