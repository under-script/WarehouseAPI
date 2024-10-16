from drf_spectacular.utils import extend_schema
from icecream import ic
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Product, Warehouse
from api.serializers import PurchaseSerializer

@extend_schema(
    request=PurchaseSerializer(many=True),
    responses={204: None},
    methods=["POST"]
)
@api_view(['POST'])
def snippet_list(request):
    if request.method == 'POST':
        products = Product.objects.all()
        warehouse = Warehouse.objects.all()
        # ic(products[0].name)
        purchases = request.data
        # ic(purchases)
        serializer = PurchaseSerializer(data=purchases, many=True)
        for index, purchase in enumerate(purchases):
            # ic(products[index].pm.all())
            for p in products[index].pm.all():
                ic(p.material.name)
                ic(p.quantity)
        if serializer.is_valid():
            result = {
                'result': [
                    {
                        "product_name": products[index].name,
                        "product_qty": purchase["quantity"],
                        "product_materials": [
                            {
                                "material_name": a.material.name,
                                "material_qty": a.quantity * purchase["quantity"],
                                "batches": [
                                    {
                                        "warehouse_id": b.id,
                                        "material_name": b.material.name,
                                        # "qty": b.remainder if b.remainder <= a.quantity * purchase["quantity"] else a.quantity * purchase["quantity"] - warehouse.filter(material__name=a.material.name)[j - 1 if j > 0 else j].remainder,
                                        "qty": b.remainder if b.remainder <= a.quantity * purchase[
                                            "quantity"] else a.quantity * purchase["quantity"] -
                                                             warehouse.filter(material__name=a.material.name)[
                                                                 j - 1 if j > 0 else j].remainder,
                                        "price": b.price
                                    } for j, b in enumerate(warehouse.filter(material__name=a.material.name))
                                ]
                            } for a in products[index].pm.all()
                        ],
                    } for index, purchase in enumerate(purchases)
                ]
            }
            return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
