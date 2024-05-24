from django.core.management.base import BaseCommand
import stripe
from django.conf import settings
from bakeryapp.models import Product

class Command(BaseCommand):
    help = "Sync our bakery website products with Stripe's product catalog"

    def handle(self, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY

        products = Product.objects.filter(stripe_product_id__isnull=True)
        for product in products:
            try:
                stripe_product = stripe.Product.create(
                    name=product.item_name,
                    description=product.item_description,
                    default_price_data={
                        'currency': 'USD',
                        'unit_amount': int(product.price * 100),  # Stripe expects the amount in cents
                    },
                    images=[product.image_url] if product.image_url else []
                )
                product.stripe_product_id = stripe_product.id
                product.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully synced product {product.item_name}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error syncing product {product.item_name}: {e}'))