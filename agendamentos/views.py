import json
from decimal import Decimal
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from .models import modelo_pagamento

@csrf_exempt
@require_http_methods(["POST"])
def criar_agendamento(request):
    dados = json.loads(request.body)
    valor_pagamento = int(Decimal(dados['valor_pagamento']) * 100)
    agendamento = modelo_pagamento.objects.create(
        data_pagamento=dados['data_pagamento'],
        permite_recorrencia=dados['permite_recorrencia'],
        quantidade_recorrencia=dados['quantidade_recorrencia'],
        intervalo_recorrencia=dados['intervalo_recorrencia'],
        status_recorrencia=dados['status_recorrencia'],
        agencia=dados['agencia'],
        conta=dados['conta'],
        valor_pagamento=valor_pagamento
    )
    return JsonResponse(agendamento.campos(), status=201)

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
    agendamento = get_object_or_404(modelo_pagamento, id=id)
    agendamento.delete()
    return JsonResponse({}, status=204)
