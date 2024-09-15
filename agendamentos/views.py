import json
from decimal import Decimal
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from .models import modelo_pagamento
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
@require_http_methods(["POST"])
def criar_agendamento(request):
    try:
        dados = json.loads(request.body)
        
        # Convertendo a string da data para um objeto date
        data_pagamento = datetime.strptime(dados['data_pagamento'], '%Y-%m-%d').date()
        
        valor_pagamento = int(Decimal(str(dados['valor_pagamento'])) * 100)
        
        agendamento = modelo_pagamento.objects.create(
            data_pagamento=data_pagamento,  # Usando o objeto date
            permite_recorrencia=dados['permite_recorrencia'],
            quantidade_recorrencia=dados['quantidade_recorrencia'],
            intervalo_recorrencia=dados['intervalo_recorrencia'],
            status_recorrencia=dados['status_recorrencia'],
            agencia=dados['agencia'],
            conta=dados['conta'],
            valor_pagamento=valor_pagamento
        )
        return JsonResponse(agendamento.campos(), status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@require_http_methods(["GET"])
def listar_agendamentos(request):
    agendamentos = modelo_pagamento.objects.all()
    return JsonResponse([agendamento.campos() for agendamento in agendamentos], safe=False)

@require_http_methods(["GET"])
def consultar_agendamento(request, id):
    agendamento = get_object_or_404(modelo_pagamento, id=id)
    return JsonResponse(agendamento.campos())

@csrf_exempt
@require_http_methods(["DELETE"])
def deletar_agendamento(request, id):
    try:
        agendamento = get_object_or_404(modelo_pagamento, id=id)
        agendamento.delete()
        return JsonResponse({'message': 'Agendamento deletado com sucesso'}, status=200)
    except modelo_pagamento.DoesNotExist:
        logger.warning(f"Tentativa de deletar agendamento inexistente. ID: {id}")
        return JsonResponse({'error': 'Agendamento não encontrado'}, status=404)
    except Exception as e:
        logger.error(f"Erro ao deletar agendamento {id}: {str(e)}")
        return JsonResponse({'error': 'Ocorreu um erro ao deletar o agendamento'}, status=500)

