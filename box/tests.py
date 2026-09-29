from django.test import TestCase

from .models import Product, Box, Order, OrderItem
from .services import findPerfactBox


class BoxSelectionTest(TestCase):

    def setUp(self):

        self.product = Product.objects.create(name="Laptop",length=30,width=20,height=5,weight=2)
        self.smallBox = Box.objects.create(name="Small Box",internal_length=40,internal_width=30,internal_height=10,max_weight=5,cost=50)
        self.largeBox = Box.objects.create(name="Large Box",internal_length=60,internal_width=50,internal_height=30,max_weight=20,cost=100)

    def test_perfect_box_selection(self):

        order = Order.objects.create()
        OrderItem.objects.create(order=order,product=self.product,quantity=1)
        result = findPerfactBox(order)
        self.assertEqual(result["box_id"],self.smallBox.id)

    def test_multiple_quantity(self):

        order = Order.objects.create()
        OrderItem.objects.create(order=order,product=self.product,quantity=2)
        result = findPerfactBox(order)
        self.assertEqual(result["product_weight"],4)

    def test_no_box_for_weight(self):

        heavyProduct = Product.objects.create(name="Heavy Product",length=10,width=10,height=10,weight=100)
        order = Order.objects.create()
        OrderItem.objects.create(order=order,product=heavyProduct,quantity=1)
        result = findPerfactBox(order)
        self.assertEqual(result["error"],"You don't have any suitable box")

    def test_product_does_not_physically_fit(self):

        product = Product.objects.create(name="Large Product",length=100,width=100,height=100,weight=1)

        order = Order.objects.create()

        OrderItem.objects.create(order=order,product=product,quantity=1)

        result = findPerfactBox(order)

        self.assertEqual(
            result["error"],
            "You don't have any suitable box"
        )