from django.db import models

# Create custom models for Henry Books.
class Book(models.Model):
    # Properties: Author, Title, Description, ThumbnailUrl, Price
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail_url = models.URLField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title

class Branch(models.Model):
    # Properties: BranchName, Address, City, State, Zip, Phone
    branch_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.branch_name

class Inventory(models.Model):
    # Properties: Book, Branch, Quantity
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.branch.branch_name} - {self.book.title} (Qty: {self.quantity})"