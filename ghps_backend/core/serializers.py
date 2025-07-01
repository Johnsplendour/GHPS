from rest_framework import serializers
from core.models import LearningMaterial, Order, OrderItem, Product, AIQuestion

class LearningMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningMaterial
        fields = ['id', 'title', 'content', 'stage']

class OrderItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    
    class Meta:
        model = OrderItem
        fields = ['product_id', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'farm', 'items', 'total', 'status', 'created_at']
        read_only_fields = ['id', 'total', 'status', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = self.context['request'].user
        order = Order.objects.create(user=user, **validated_data)

        total = 0
        for item in items_data:
            product = Product.objects.get(id=item['product_id'])
            quantity = item['quantity']
            price = product.price
            total += price * quantity
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=price
            )

            # Optionally reduce stock
            product.stock -= quantity
            product.save()

        order.total = total
        order.save()
        return order

class AIQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIQuestion
        fields = ['id', 'question', 'response', 'created_at']
        read_only_fields = ['id', 'response', 'created_at']
